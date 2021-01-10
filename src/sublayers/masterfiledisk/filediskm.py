#!/usr/bin/python3
#coding: utf-8
# =====================================
import numpy as np
import time
import os
def decode_taille(taille_code,verbose=1,allow_raw=True):
    if taille_code.count(".") > 1:
        if verbose: print("ERROR: TOO MANY DOT INTO SIZE_CODE")
        return None
    units = {"P":10**15,"T":10**12,"G":10**9,"M":10**6,"K":10**3,"O":10**0}
    consider_num = "0123456789."
    acc=""
    for i in taille_code:
        if i in consider_num:
            acc=acc+i
        else:
            try:
                return float(acc)*units[i]
            except expression as identifier:
                if verbose: print("ERROR: {}".format(identifier))
                return None
    if allow_raw: return float(acc)
    if verbose: print("NOT DECODABLE")
    return None
# =====================================
# =====================================
# ===================================== 
"""
Un disk_manager par disque
Le reste viendra après pour plus de .... complexité mouhahahahahahahahahahahahah
"""
class disk_manager(object):
    def __init__(self):
        pass
    # =====================================
    def make_disk_zero(self,filepath,size_oct="1G",cut_oct="100M",property_root=True):
        cut_oct_taille = decode_taille(cut_oct)
        with open(filepath,"wb") as f:
            taille=decode_taille(size_oct)
            if "." in size_oct:
                cut_digits=str(taille).split(".")[1]
                for i in np.arange(0,taille,float(cut_digits)+float(cut_oct_taille)):
                    if i+float(cut_digits)+float(cut_oct_taille)>=taille:
                        cut_oct_taille = float(taille - i)
                    print("\r{:>10}%\r".format((i/taille)*100.0),end="\r")
                    f.write((chr(0)*int(cut_oct_taille)).encode())
                f.close()
            else:
                for i in range(0,int(taille),int(cut_oct_taille)):
                    if i+int(cut_oct_taille)>=taille:
                        cut_oct_taille = int(taille - i)
                    print("\r{:>10}%\r".format((i/taille)*100.0),end="\r")
                    f.write((chr(0)*int(cut_oct_taille)).encode())
                f.close()
        if property_root:
            os.system("chmod a-rwx {} && chmod g-rwx {}".format(filepath,filepath))
    # =====================================
    def make_ext4(self,filepath):
        os.system("mkfs.ext4 {}".format(filepath))
    # =====================================
    def mount(self,filepath,folderpath,
            access_for_all=False,access_for_spe_user="$USER"):
        os.system("mkdir -p {}".format(folderpath))
        os.system("mount -t ext4 {} {}".format(filepath,folderpath))
        if access_for_all:
            os.system("chmod a+rwx {}".format(folderpath))
        else:
            os.system("chown {} {}".format(access_for_spe_user,folderpath))
    # =====================================
    def unmount(self,folderpath):
        os.system("umount {}".format(folderpath))
    # =====================================
# =====================================
# =====================================
# =====================================
class AskedSpace(object):
    def __init__(self,namedisk,mnt_folder_path="/tmp/mnt",space_code="1G",buffer_size="200M",for_user="$USER",disk_folder_path="/tmp/disks"):
        self.DMAN = disk_manager()
        self.user = for_user
        self.space_code = space_code
        self.disk_folder_path = disk_folder_path
        self.mnt_folder_path = mnt_folder_path
        self.namedisk = namedisk
        self.buffer_size = buffer_size
    # =====================================
    def ask(self):
        self.DMAN.make_disk_zero("{}/{}".format(self.disk_folder_path,self.namedisk),self.space_code,self.buffer_size)
    # =====================================   
    def format(self):
        self.DMAN.make_ext4("{}/{}".format(self.disk_folder_path,self.namedisk))
    # =====================================
    def mount(self):
        self.DMAN.mount("{}/{}".format(self.disk_folder_path,self.namedisk),self.mnt_folder_path,access_for_spe_user=self.user)
    # ===================================== 
    def unmount(self):
        self.DMAN.unmount(self.mnt_folder_path)
    # ===================================== 

"""
AS = AskedSpace("disk1.img","/tmp/mnt1","10G","300M","ricksanchez","disks")
AS.ask()
AS.format()
AS.mount()
time.sleep(120)
AS.unmount()
"""