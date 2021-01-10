#coding: utf-8

import os
import random
from multiprocessing import Pool
import json
class sumrnd(object):
	def __init__(self, seed=0, B=7, n_max=4 , salt=""):
		self.seed = seed
		random.seed(seed)
		self.salt = salt
		#CONST
		self.B, self.n_max = B, n_max
		self.C=1
	def random_uppercase(self,i):
		if random.randint(0,100) < 40: return str(i).upper()
		else: return i
	
	def constant_mod(self,y,mode="alpha"):
		keycar = {"alpha": "azertyuiopqsdfghjklmwxcvbn" , "num":"0123456789", "special":"/*])@^\|[({#&>" }
		possible = keycar[mode]
		if mode == "alpha":  possible = self.random_uppercase(possible)
		return possible[y%len(possible)]
		
	def have_minimal_secure(self,data,minlen=12):
		keycar = {"alpha": "azertyuiopqsdfghjklmwxcvbn" , "num":"0123456789", "special":"/*-+=])@à^ç\_`è|-[({'#~é»&<«≤²>" }	
		have_alpha, have_uppercase, have_num, have_special = False, False, False, False
		for i in data:
			if i in keycar["alpha"]: have_alpha = True
			if i in keycar["alpha"].upper(): have_uppercase = True
			if i in keycar["num"]: have_num = True
			if i in keycar["special"]: have_special = True
		return {"have":{"alpha":have_alpha,"uppercase":have_uppercase,"num":have_num,"special":have_special},"minlen":minlen,"len":len(data),"minrespectedlen":len(data)>=minlen}

	def random_determinist(self, data, salt):
		self.n_max = len(data)
		random.seed(str(self.seed)+str(salt))
		self.blocks = []
		for x in range(0,self.C):
			block = []
			for y in range(0,self.n_max):
				 block.append(self.constant_mod(random.randint(0,255),random.choice(["alpha","num","special"])))
			self.blocks.append("".join(block))
			block = []
		return self.blocks
	
	def indetity_mode(self, car):
		for k,v in keycar.items():
			if car in v:
				return k
				
	def getter(self):
		return self.blocks

	def getlenofmode(self,caract):
		return len(keycar[self.identity_mode(caract)])

	def format_func(self,separator="-"):
		FINAL = ""
		for block in self.blocks:
			FINAL = FINAL + "".join(block) + separator
		return FINAL[:-1]		

	def variator(self, proba=0.10, variation=(1,5)):
		ind_1 = -1
		for block in self.blocks:
			ind_1 += 1
			ind_2 = -1
			for i in block:
				ind_2 += 1
				if random.randint(0,100) < (proba * 100,0):
					self.blocks[ind_1][ind_2] = chr((ord(self.blocks[ind_1][ind_2]) + random.randint(variation[0], variation[1]))%self.getlenofmode(self.blocks[ind_1][ind_2]))
					
	def frequency_counter(self, data):
		freq = {}
		ratio = {}
		for i in data:
			if i not in freq.keys():
				freq[i] = 1
			else:
				freq[i] += 1
		
		for k,v in freq.items():
			ratio[k] = v / float(len(data))
		
		self.freq  = freq
		self.ratio = ratio

	def appair_more(self,morelvl=5,maxi=2):
		for k,v in self.freq.items():
			if v>=morelvl: maxi-=1
		return maxi<0


import zlib
def hacked_strong_check(data):
	sr = sumrnd()
	total = []
	maxlevelcompr = 9
	for i in range(0,9):
		total.append(len(zlib.compress(data.encode(),i)))
		if len(total)>1:
			if total[-1] == total[-2]:
				maxlevelcompr = i - 1
	IS_COMPRESSED = total[0] > total[8]
	sum_total, means_total = sum(total), (sum(total)/float(len(total))) 
	ratio_total = means_total / float(len(data))
	
	print("levels: ",total)
	print("total: ",sum_total)
	print("means: ",means_total)
	print("ratio: ",ratio_total)
	

	print("FREQ COUNT...:")
	
	sr.frequency_counter(data)
	
	print("\n","FREQUENCY: ",sr.freq)
	print("RATIO: ",sr.ratio)
	
	print ("TO MANY SAME CHAR: ",sr.appair_more(5,2))
	
	return {"declinate_optionzero":sr.random_determinist(data,data), "have_minimal_secure": sr.have_minimal_secure(data,minlen=14) ,"password": data, "ratio":ratio_total, "is_compressed":IS_COMPRESSED, "maxlevelzip": maxlevelcompr, "sum_total":sum_total,"means":means_total,"total_ratio":ratio_total,"frequency":sr.freq,"ratio":sr.ratio,"tomanysame":sr.appair_more(5,2)}
	"""
	# =====================================
			CONCLUSION:
				need params and rate system
	# =====================================
	"""

def testing(ss):
    try:
        print("test '{}'".format(ss.strip()))
        #ss=input("password for test>")
        d=hacked_strong_check(ss.decode().strip())
        return d
    except:
        for o in ss:
            d=hacked_strong_check(str(o))
            return d

with open("/usr/share/dirb/wordlists/big.txt","rb") as f:
    sss=f.readlines()
    with Pool(64) as p:
        data = p.map(testing,sss)
    f=open("output/out-big.json","w")
    f.write(json.dumps(data,indent=4,sort_keys=True))
    f.close()
        

with open("/usr/share/dirb/wordlists/common.txt","rb") as f:
    sss=f.readlines()
    with Pool(64) as p:
        data = p.map(testing,sss)
    f=open("output/out-common.json","w")
    f.write(json.dumps(data,indent=4,sort_keys=True))
    f.close()
        

with open("/usr/share/dirb/wordlists/others/names.txt","rb") as f:
    sss=f.readlines()
    with Pool(64) as p:
        data = p.map(testing,sss)
    f=open("output/out-name.json","w")
    f.write(json.dumps(data,indent=4,sort_keys=True))
    f.close()
        

with open("/usr/share/dirb/wordlists/others/best1050.txt","rb") as f:
    sss=f.readlines()
    with Pool(64) as p:
        data = p.map(testing,sss)
    f=open("output/out-best1050.json","w")
    f.write(json.dumps(data,indent=4,sort_keys=True))
    f.close()
