#!/usr/bin/python3
#coding: utf-8
# =====================================
import os
import random
import time
from base64 import b64decode as b64d
# =====================================SCRIPTS BEG
like_a_build = "c3VkbyBta2RpciBidWlsZApzdWRvIGNwIHJlYWRuY3V0X3N0cmVhbS5weSByZWFkbmN1dF9zdHJlYW0Kc3VkbyBjaG1vZCBhK3ggcmVhZG5jdXRfc3RyZWFtCnN1ZG8gY3AgcmVhZG5jdXRfc3RyZWFtIC91c3IvYmluL3JlYWRuY3V0X3N0cmVhbQpzdWRvIHJtIC1yZiBidWlsZA=="
# =====================================SCRIPTS END
def installself():
	os.system(b64d(like_a_build.encode()).decode())
# =====================================
# Fonctions extra
def transform2HumanCharset(randomdata):
	charset=[i for i in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789/*-+@()[]#€$%:;,?.!"]
	acc=[]
	#char 0-255
	for c in randomdata:
		acc.append(charset[int(c)%len(charset)])
	return acc
def reverse(item):
	return item[::-1]

def urandom_integer(min_=1,max_=2,loop=1000,START_=0,STOP_=None,IS_MODULO_MODE_FOR_MAX=False):
	number=START_
	for i in range(0,loop):
		number+=ord(os.urandom(1))
		if number == STOP_: break
	if IS_MODULO_MODE_FOR_MAX:
		return min(min_,number%max_)
	else:
		return min(min_,max(max_,number))
	return number
# =====================================
# =====================================
# ===================================== DEFAULTS VALUES ARGS KWARGS
SIZE_PASSWORD = 19
produce_hash_string=False
# =====================================
MODES_RND = ["seeded","urandom"]
#urandom can be made an stream pseudo-not-deterministic with an drive, disc or simple file
# =====================================
default_size_block,default_prefix_filename,default_stream_path = 2048, "/tmp/RCS_", "/dev/sr0"
# =====================================
default_reverse_read,default_random_read = False, False
default_mode_rnd = 0
default_mode_rand = default_mode_rnd
default_seed = time.time()
# =====================================
# =====================================
# =====================================
"""
note: 
	ajouter une fonction read-special: reverse-read, random-seeded-read
	ajouter une fonction de dispertion entre deux images
	ajouter une fonction de mixage par bit ou par blocks des images disques
"""

class ReadCutStream(object):
	def __init__(self,size_block=default_size_block,prefix_filename=default_prefix_filename,stream_path=default_stream_path):
		self.size_block,self.prefix_filename,self.stream_path = size_block,prefix_filename,stream_path

	def run(self, reverse_read=default_reverse_read, random_read=default_random_read, random_read_conf_mode_random=default_mode_rnd, SEED=default_seed,produce_hash_string=False):
		print("lecture de {} par blocs de {}".format(self.stream_path,self.size_block))
		blocks = []
		# =====================================
		# READ
		f = open(self.stream_path)
		f.seek(0, os.SEEK_END)
		sizef = f.tell()
		f.close()
		f = open(self.stream_path,"rb")
		if random_read:
			random.seed(SEED)
		while (True):
			if random_read: 
				if MODES_RND[random_read_conf_mode_urandom] == "seeded":
					f.seek(random.randint(0,sizef),0)
				elif MODES_RND[random_read_conf_mode_urandom] == "urandom":
					f.seek(urandom_integer(min_=1,max_=sizef-1),0)
			#self.size_block*len(blocks),0)
			data = f.read(self.size_block)
			if len(data)==0:
				if random_read:
					if len(blocks) >= (sizef/self.size_block):
						break
				else:
					break
			if produce_hash_string:
				data=hashlib.sha512(data).digest()
			if not reverse_read:
				blocks.append(data)
			elif reverse_read:
				blocks.append(reverse(data))
			if len(blocks) > 1000:
				if reverse_read: blocks=reverse(blocks)
				print("Ecriture des fichiers...")
				i=-1
				for item in blocks:
					i+=1
					filepath="{}-BLOCK({})_SIZE({}).img".format(self.prefix_filename,i,self.size_block)
					f2 = open(filepath,'wb')
					f2.write(item)
					f2.close()
				blocks = []
		f.close()
		if reverse_read: blocks=reverse(blocks)
		# =====================================
		print("OK.")
		print("Ecriture des fichiers...")
		i=-1
		for item in blocks:
			i+=1
			filepath="{}-BLOCK({})_SIZE({}).img".format(self.prefix_filename,i,self.size_block)
			f = open(filepath,'wb')
			f.write(item)
			f.close()
		print("OK.")
		return self
# =====================================# =====================================# =====================================
import argparse
# =====================================
random.seed(default_seed)
parser = argparse.ArgumentParser()
# =====================================
"""
parser.add_argument("-", "--", type=int,
                    help="")
                    MODES_RND
"""
# =====================================
# basic functions
parser.add_argument("-sb", "--size-block", type=int,
                    help="size of block read from stream(typicaly a device)")
parser.add_argument("-pf", "--prefix-filename", type=str,
                    help="prefix can be a name or a fullpath")
parser.add_argument("-sp", "--stream-path", type=str,
                    help="path of the stream for source of copy 'n cutting in parts")
# =====================================
# password generator
parser.add_argument("-pws", "--password-size", type=int,
                    help="")
parser.add_argument("-s", "--seed", type=str,
                    help="set the seed")
# =====================================
parser.add_argument("-drevr", "--default-reverse-read", action="store_true",
                    help="enable the default reverse read")
parser.add_argument("-drndr", "--default-random-read", action="store_true",
                    help="enable the default random read")
parser.add_argument("-dmdr", "--default-mode-rand", action="store_true",
                    help="enable the default mode random to urandom(from os)")
parser.add_argument("-hstr", "--produce-hash-string", action="store_true",
                    help="enable the production of the 'hash-string'(withconcatenation) of block")
# =====================================



parser.add_argument("COMMAND")
args = parser.parse_args()
# =====================================
# default configuration
# =====================================
COMMAND = args.COMMAND
cmdslst=["GENPASSWORD","RUN","MAKE","MAKE-YES-SURE","DEFAULT-TEST"]
if args.COMMAND == "help":
	print(str(cmdslst[0:2]))
	exit(0)
if args.COMMAND == "HELP":
	print(str(cmdslst))
	exit(0)
# =====================================
if (COMMAND.upper() == "MAKE") or (COMMAND.upper() == "MAKE-YES-SURE"):
	# =====================================
	if COMMAND.upper() == "MAKE":
		print("YOUR ARE NOT SURE I THINK...")
	elif (COMMAND.upper()) == "MAKE-YES-SURE":
		installself()
		os.remove("readncut_stream")
	else:
		print("Already installed!")
		exit(0)
	# =====================================
elif COMMAND.upper() == "GENPASSWORD":
	SIZE_PASSWORD = args.password_size
	print("".join(transform2HumanCharset(os.urandom(SIZE_PASSWORD))))
	exit(0)
# =====================================
elif COMMAND.upper() == "RUN":
	# =====================================
	# interpretation of configure
	# =====================================
	size_block = args.size_block
	if not size_block: size_block = default_size_block
	# =====================================
	prefix_filename = args.prefix_filename
	if not prefix_filename: prefix_filename = default_prefix_filename
	# =====================================
	stream_path = args.stream_path
	if not stream_path: stream_path = default_stream_path
	# =====================================
	if not default_reverse_read: default_reverse_read = False
	if not default_random_read: default_random_read = False
	# =====================================
	if args.default_mode_rand: default_mode_rnd = 1
	# =====================================
	if args.seed: default_seed = args.seed
	# =====================================
	"""	
	default_reverse_read,default_random_read = False, False
	default_mode_rnd = 0
	default_seed = time.time()
	"""
	# =====================================
	RCS = ReadCutStream(size_block,prefix_filename,stream_path)
	RCS.run(default_reverse_read,default_random_read,default_mode_rand,SEED=default_seed,produce_hash_string=produce_hash_string)
	# =====================================
# =====================================
elif COMMAND.upper() == "DEFAULT-TEST":
	RCS = ReadCutStream()
	RCS.run()
# =====================================