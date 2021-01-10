#!/usr/bin/python3
#coding: utf-8
# =====================================
import argparse
import os
import json
import ast
import hashlib
from base64 import b64encode as b64enc
from base64 import b64decode as b64dec
# =====================================
parser = argparse.ArgumentParser(
    description='Process checksum verification RAWKEYCDROM.')
parser.add_argument('COMMAND')
parser.add_argument('--fcheck', type=str,
                    help='file list with hash content.')
parser.add_argument('--symlink', type=str,
                    help='symlink path of CDROM.')
parser.add_argument('--sectors', action="store_true",
                    help='sectors by sectors mode.')
args = parser.parse_args()
# =====================================
class checksum_verificator(object):
    # =====================================
    def __init__(self, fcheck, symlink, sectors=False):
        self.fcheck = fcheck
        try:
            f=open(fcheck,'rb')
            self.listhash = f.read().decode().strip().split()
            f.close()
        except:
            self.listhash = []
        self.sectors = sectors
        # =====================================
        self.symlink = symlink
        # =====================================
        try:
            f=open("/var/pdtslsw/config.json","rb") 
            f.close()
        except:
            os.system("sudo mkdir -p /var/pdtslsw/")
            f=open("/var/pdtslsw/config.json","wb")
            f.write(json.dumps(b64dec(b'ewogICAgInByb2dyYW0iOiAidmVyaWZ5X3NlY3Rvcl9ieV9zZWN0b19maWxlc19jaGVja3N1bSIsCiAgICAiZm9sZGVyX2Zvcl9kdW1wIjogIi90bXAvZHVtcF9zcl9jaGVjay8iLAogICAgImRlc3Ryb3lfY29tbWFuZF90bXBfZGF0YSI6ICJzdWRvIHNocmVkIC0tZm9yY2UgLW4gNyAtLXJlbW92ZSAteiAtLXZlcmJvc2Uge30iLAogICAgImZvcm1hdF9jb21tYW5kIjogIm1rZnMuZXh0NCIsCiAgICAibmFtZV9pbWciOiAidGVtcG9yYXJ5LmltZyIsCiAgICAic2l6ZV9pbWFnZSI6IDgwMDAwMDAwMCwKICAgICJzcGxpdF9tZW1vcnkiOiA4MAp9Cg=='), sort_keys=True, indent=4))
            f.close()
            
        finally:
            with open("/var/pdtslsw/config.json", "rb") as f:
                self.config=json.loads(f.read())
                f.close()
    # =====================================
    def run(self,mode):
        # =====================================
        print("MAKE THE DISK FOR DATADUMP...")
        folder = self.config["folder_for_dump"]
        name_img = self.config["name_img"]
        format_command = self.config["format_command"]
        size_image = int(self.config["size_image"])
        split_memory = int(self.config["split_memory"])
        bs=int(split_memory)
        count=int(size_image/split_memory)
        script1="""
        sudo mkdir -p {}
        sudo dd if=/dev/zero of={} bs={} count={} iflag=fullblock status=progress
        sudo {} {}
        sudo mount {} {}
        """.format(folder+"mnt/", folder+name_img, bs, count, format_command, folder+name_img, folder+name_img, folder+"mnt/")
        os.system(script1)
        # =====================================
        # HERE PLACE THE CHECKSUM VERIFICATION OF ...
        if mode == "GET":
            if self.sectors:
                os.system("readncut_stream RUN -sb=2048 -pf=\"{}\" -sp=\"{}\" ".format(folder+"mnt/",self.symlink))
            else:
                os.system("readncut_stream RUN -sb={} -pf=\"{}\" -sp=\"{}\" ".format(size_image, folder+"mnt/", self.symlink))
            os.system("echo {}* > {}".format(folder+"mnt/", folder+"mnt/checksums.list"))
            bad_sectors = self.read_n_hash(self.fcheck, folder+"mnt/checksums.list")
            if len(bad_sectors)>0:
                print("! ERROR WITH DISK, CORRUPTED SECTORS DETECTED !")
                dumped_json = json.dumps(bad_sectors ,sort_keys=True, indent=4)
                print(dumped_json)
                name_file_report = "/var/pdtslsw/bad_sectors_{}_report.json".format(hashlib.sha224(os.urandom(512)).hexdigest())
                f = open(name_file_report,"wb")
                f.write(dumped_json.encode())
                f.close()
                print("! ERROR WITH DISK, CORRUPTED SECTORS DETECTED !\n\nreport saved to "+name_file_report)
            else:
                print("THE DISK IS CONFORM.")
        if mode == "SET":
            if self.sectors:
                os.system("readncut_stream RUN -sb=2048 -pf=\"{}\" -sp=\"{}\" ".format(folder+"mnt/",self.symlink))
            else:
                os.system("readncut_stream RUN -sb={} -pf=\"{}\" -sp=\"{}\" ".format(size_image, folder+"mnt/", self.symlink))
            os.system("echo {}* > {}".format(folder+"mnt/", folder+"mnt/checksums.list"))
            dumped_json = json.dumps(self.getHashWithThisListFile(folder+"mnt/checksums.list"), sort_keys=True, indent=4)
            f = open(self.fcheck, "wb")
            f.write(dumped_json.encode())
            f.close()
            print("Done. (saved to {})".format(self.fcheck))
        print("DESTRUCTION OF DATA DUMPED...")
        # =====================================
        os.system(self.config["destroy_command_tmp_data"].format(folder+name_img))
        os.system("sudo umount -f {}".format(folder+"mnt/"))
        os.system("rm -r {}".format(folder+"mnt/"))
        os.system("rm -r {}".format(folder))
    # =====================================
    def getHashWithThisListFile(self, verif_sum):
        with open(verif_sum,"rb") as f:
            data = f.read().strip().split()
            f.close()
        listhash=[]
        for i in data:
            try:
                with open(i, 'rb') as f:
                    rawdata = f.read()
                    listhash.append({
                                        "b64-hash": b64enc(hashlib.sha512(rawdata).digest()).decode(),
                                        "hex-hash": hashlib.sha512(rawdata).hexdigest(),
                                        "origin": i.decode()
                                    })
                    f.close()
            except:
                print("FOLDER {} SKIPPED...".format(i))
        return listhash
    # =====================================
    def read_n_hash(self,fcheck,verif_sums):
        listof_bad_sectors = []
        with open(fcheck, 'r') as f:
            listsums = json.loads(f.read())
            f.close()
        data = self.getHashWithThisListFile(verif_sums)
        for i in data:
            origin_,hashhex,hashb64 = i["origin"],i["hex-hash"],i["b64-hash"]
            for j in listsums:
                if origin_ == j["origin"]:
                    if not ((hashhex==j["hex-hash"]) and (hashb64==j["b64-hash"])):
                        listof_bad_sectors.append({
                            "b64-hash-source": hashb64,
                            "hex-hash-source": hashhex,
                            "source": origin_,
                            "b64-hash-sample": j["b64-hash"],
                            "hex-hash-sample": j["hex-hash"],
                            "sample": j["origin"]
                        })
        return listof_bad_sectors
    # =====================================
if args.COMMAND.upper() == "GET":
    CHKSUM = checksum_verificator(args.fcheck, args.symlink, args.sectors)
    CHKSUM.run(args.COMMAND.upper())
elif args.COMMAND.upper() == "SET":
    CHKSUM = checksum_verificator(args.fcheck, args.symlink, args.sectors)
    CHKSUM.run(args.COMMAND.upper())

