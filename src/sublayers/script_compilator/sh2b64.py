#coding: utf-8
from base64 import b64encode as b64
from base64 import b64decode as b64dec
from copy import copy
import os
import hashlib
import json
import ast
# =====================================
def str2quotes(str_):
	return "'"+str(str_)+"'"
# =====================================
# =====================================
class RocketRx(object):
	def __init__(self,suffix=".sh"):
		self.suffix = suffix
	# =====================================
	def list_n_read_all_with_suffix(self):
		self.quantic_carburator = []
		os.system("cd scripts/ && echo *{}> fileindex.txt".format(self.suffix))
		f=open("scripts/fileindex.txt","rb")
		for i in f.read().split():
			try:
				ff = open("scripts/"+i.decode(),'rb')
				info = ff.read()
				ff.close()
				self.quantic_carburator.append({
													"name_file": i.decode(),
													"data_file": info.decode(),
													"suffix": self.suffix,
													"sha512_file": hashlib.sha512(info).hexdigest()
												})
			except:
				print("{} cause une erreur...".format(i))
		f.close()
		os.remove("scripts/fileindex.txt")
		os.system("cd ..")
		return self.quantic_carburator
	# =====================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~===
# =========================================
# Rickest exec and hack like script
# =====================================
class sh2b64(object):
	def __init__(self, filepath):
		f = open(filepath,"rb")
		self.data = f.read()
		f.close()
	def get_cnt_opt_arg_cmd(self):
		return str(self.data.decode()).count("{}")
	# =====================================
	def code2b64(self):
		return b64("{}".format(self.data).encode())
	# =====================================
	def StartDance(self,*args):
		return (", ".join(["%s"] * len(args))+"!") % tuple(args)
	# =====================================
	def sh4hope(self,*args):
		#try:
		G1 = eval(list(map(str,args))[0])
		reargumentation = ("\""+str('","'.join(G1))+"\"").split(",")
		#print(self.get_cnt_opt_arg_cmd(), "<-----", len(reargumentation))
		reargumentation = str(self.StartDance(reargumentation))
		reargumentation = reargumentation[1:len(reargumentation)-2]
		_locals = locals()
		exec("reargumentation = self.data.decode().format("+reargumentation+")",globals(), _locals)
		regurgitation=_locals["reargumentation"]
		#except:
		#	future_formation = self.data.decode()
		#print ("####\n\n{}\n\n####".format(regurgitation))
		self.data = copy(regurgitation)
		return self.code2b64()
# =====================================
def I_WANNA_BE_A_ROBOT(pathnameofdisk):
	RRx = RocketRx()
	quantic_carburator = RRx.list_n_read_all_with_suffix()
	# =====================================
	cnt=0
	for QC in quantic_carburator:
		sh2b = sh2b64("scripts/"+QC["name_file"])
		b64_data = sh2b.sh4hope([pathnameofdisk]*sh2b.get_cnt_opt_arg_cmd())
		quantic_carburator[cnt]["b64_data"] = b64_data.decode()
		cnt+=1
	# =====================================
	f_qc=open("/tmp/quantic_carburator.json",'wb')
	f_qc.write(json.dumps(quantic_carburator, sort_keys=True, indent=4).encode())
	f_qc.close()
	exit(0)
# =====================================
I_WANNA_BE_A_ROBOT("")
