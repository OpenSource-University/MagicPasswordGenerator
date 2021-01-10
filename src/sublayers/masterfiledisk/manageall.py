#!/usr/bin/python3
#coding: utf-8
import masterfiledisk.filediskm as filediskm
import masterfiledisk.d_transformerz as d_transformerz
import json



class Customer(object):
    def __init__(self,user,namedisk,forfait = "10G",config_path="masterfiledisk/config.json"):
        with open(config_path,'rb') as f:
            config=json.loads(f.read())
            f.close()
        self.forfait = forfait
        self.jdb = None
        self.ASKED = filediskm.AskedSpace(namedisk,mnt_folder_path=config["mnt_folder_path"],space_code=forfait,buffer_size=config["buffer_size"],for_user=user,disk_folder_path=config["disk_folder_path"])
    def initialize(self):
        self.ASKED.ask()
        self.ASKED.format()
    def format(self):
        self.ASKED.format()
    def enable(self):
        self.ASKED.mount()
        self.jdb=jumpdb()
        self.jdb.load("fichiers.jdb")
    def disable(self):
        self.ASKED.unmount()
        self.jdb = None
    # =====================================
    def upload(self,data):
        ID=jdb.insert(data)
    
"""
C=Customer("rick","disk1","100G")
C.initialize()
C.enable()
C.upload(data)
"""
"""
j=jumpdb()
j.load("test.jdb")
#ID=j.insert({44:5,55:8})
#print(ID)
print(j.find({"44":8}))
#j.update(ID,{44:8})
#j.enumerate(ID)
#j.delete(ID)
#print(j.find({44:8}))
#j.save("test.jdb")
"""