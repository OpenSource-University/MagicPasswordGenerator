#coding: utf-8
import os

script = """udevadm info --query=all --name=/dev/sde | grep ID_SERIAL>>/tmp/querysnkey.txt""" 
os.system(script)
final_data={}
with open("/tmp/querysnkey.txt",'r') as f:
    data=f.read().replace("E: ","")
    data=data.strip().split("\n")
    for i in data:
        final_data[i.split("=")[0]] = i.split("=")[1]
    f.close()
os.remove("/tmp/querysnkey.txt")
print(final_data)