#coding: utf-8
import os
def get_serials(symlink,verbose=1):
    script = """udevadm info --query=all --name={} | grep ID_SERIAL>>/tmp/querysnkey.txt""".format(symlink) 
    os.system(script)
    final_data={}
    with open("/tmp/querysnkey.txt",'r') as f:
        data=f.read().replace("E: ","")
        data=data.strip().split("\n")
        for i in data:
            final_data[i.split("=")[0]] = i.split("=")[1]
        f.close()
    os.remove("/tmp/querysnkey.txt")
    if verbose: print(final_data)
    return final_data

class detector_insert(object):
    def __init__(self):
        pass


