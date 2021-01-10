#!/usr/bin/python3
#coding: utf-8
# =====================================
# =====================================
from urllib import request
from copy import copy
import os
import json
from base64 import b64encode as b64enc
from base64 import b64decode as b64dec
import hashlib
from os import urandom
import random
from multiprocessing import Pool
from datetime import datetime,timedelta
import sys
import getch#NEED TO INSTALL
import random
from termcolor import colored
# =====================================
# =====================================
# MODULE RULES DECODER
# CRYPTOGRAPHY USING A PASSWORD AS A KEY SELECTOR AND GENERATES AN ADDITIONAL CODE
# AS WELL AS A PASSWORD THAT CHANGES EVERYDAY ACCORDING TO UNIVERSAL TIME.
# So use:
# IN: password + key
#  +
# SALT: UNIVERSAL TEMPORALITY
# ||
# VV
# OUT: keys + code + password
# =====================================
# =====================================
class external_senses(object):
    def __init__(self):
        self.entropy = None
        self.ofthat=2
    # =====================================
    def is_pair(self,x):
        return not(x%2)
    def is_an_multiple(self,x,ofthat):
        return not(x%ofthat) # x suposition is an multiple ? modulo and not just that can help.
    def is_an_multiple__(self, x):
        if not(x % self.ofthat): return x
        return 0
    def found_multiples_of(self, ofthat, range_=range(0, 1000), max_range_=None, workers_=12):
        self.ofthat = ofthat
        liom__ = []
        list_of_multiples=[]
        with Pool(workers_) as p:
            if max_range_!=None:
                rng_=[1]
                c=-999
                while(rng_[-1]<=max_range_):
                    c+=1000
                    rng_ = [i*c for i in range(1,1000)]
                    list_of_multiples = p.map(self.is_an_multiple__, rng_)
                    for i in list_of_multiples:
                        if i != 0: 
                            print("({}) [{}%]".format(i, float(i/max_range_)*100.0 ))
                            liom__.append(i)
                return liom__
            elif range_!=None:
                list_of_multiples = p.map(self.is_an_multiple__,range_)
        for i in list_of_multiples:
            if i != 0: liom__.append(i)    
        return liom__
    # =====================================
    def get_entropy(self):
        with open("/proc/sys/kernel/random/entropy_avail",'r') as f:
            self.entropy = int(f.read().strip())
            f.close()
    # =====================================
    # =====================================
    # TEMPORALITY
    def get_time_from_internet(self):
        adrss = "http://worldtimeapi.org/api/timezone/Europe/Paris"
        response = request.urlopen("http://"+adrss)
        # set the correct charset below
        page_source = json.loads(response.read().decode())
        return page_source
        
        # exemple:
        # {
        #     "abbreviation": "CET",
        #     "client_ip": "92.148.203.126",
        #     "datetime": "2020-11-29T16:28:19.573036+01:00",
        #     "day_of_week": 0,
        #     "day_of_year": 334,
        #     "dst": false,
        #     "dst_from": null,
        #     "dst_offset": 0,
        #     "dst_until": null,
        #     "raw_offset": 3600,
        #     "timezone": "Europe/Paris",
        #     "unixtime": 1606663699,
        #     "utc_datetime": "2020-11-29T15:28:19.573036+00:00",
        #     "utc_offset": "+01:00",
        #     "week_number": 48
        # }
        
    # =====================================    
    def delta_countdown_oneshot(self,date_):
        return date_-datetime.now()
    # =====================================
    def get_StrDelta_later_at_precise(self,days=0,
                                    seconds=0,
                                    microseconds=1,
                                    milliseconds=0,
                                    minutes=0,
                                    hours=0,
                                    weeks=0):
        return str(timedelta(days=days, seconds=seconds, microseconds=microseconds, milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)+datetime.now())
    # =====================================
    def get_DayJ_Delta_precise(self,YYYY,MM,DD):
        return "J{}".format(str(datetime.now()-datetime(YYYY,MM,DD)))
    # =====================================
    # =====================================

# =====================================
# =====================================
# =====================================
class multi_stck(object):
    def __init__(self, s_start):
        #if s_start == None: s_start = {}
        self.keystormeds, self.RETRY_HASH_CONFIGs = copy(
            s_start["keystormed"]), copy(s_start["RETRY_HASH_CONFIG"])
        del s_start
        # =====================================
    def valueToUnpacked(self):
        res = []
        for i in range(0, len(self.keystormeds)):
            res.append([self.keystormeds[i], self.RETRY_HASH_CONFIGs[i]])
        return res
# =====================================
class TrueRandom_v1(object):
    def __init__(self):
        pass
        #to complete next
    # =====================================
    def truerand(self, size):
        f = open("/dev/urandom", "rb")
        d = f.read(size)
        f.close()
        return d
    # =====================================
    def generate_RnD_CSV(self, x0, x1, filepath="TrueRandom_v1[Cider].csv"):
        f = open(filepath, "w")
        for i in range(1, x0):
            for j in range(i, x1):
                key = b64enc(self.truerand(i)).decode()[0:j]
                f.write("{},{},{},{}\n".format(i, j, len(key), str(key).count("=")))
                print("({})% / [{}]%".format(((i/(x0*1.0))*100.0), ((j/(x1*1.0))*100.0)))
        f.close()
    # =====================================
    def generate_RnD_noend(self, x0, x1, filepath="keys.txt"):
        f = open(filepath, "w")
        for i in range(1, x0):
            for j in range(i, x1):
                key = b64enc(self.truerand(i)).decode()[0:j].replace(
                    "=", b64enc(self.truerand(i)).decode()[0])
                f.write("{}\n".format(key))
                #f.write("{},{},{},{}\n".format(i,j,len(key),str(key).count("=")))
                print("({})% / [{}]%".format(((i/(x0*1.0))*100.0), ((j/(x1*1.0))*100.0)))
        f.close()
    # =====================================
    def generate_fixed_noend(self, X, filepath="keys2.txt"):
        x0, x1 = X, X
        f = open(filepath, "w")
        for i in range(1, x0):
            for j in range(i, x1):
                key = b64enc(self.truerand(i)).decode()[0:j].replace(
                    "=", b64enc(self.truerand(i)).decode()[0])
                f.write("{}\n".format(key))
                #f.write("{},{},{},{}\n".format(i,j,len(key),str(key).count("=")))
                print("({})% / [{}]%".format(((i/(x0*1.0))*100.0), ((j/(x1*1.0))*100.0)))
        f.close()
    # =====================================
    def generate_one_key(self, lenght=8):
        return b64enc("".join([chr(int(random.random()*256)) for i in range(0, lenght)]).encode()).decode()[0:lenght]
    # =====================================
    def minethat(self, keystormed):
        mined = hashlib.sha512((keystormed).encode()).hexdigest()
        if mined[0:self.sizerepeat] == self.caractrepeat*self.sizerepeat:
            print("0x{}".format(mined))
            return {"mined": mined, "keystormed": keystormed}
        return None
    # =====================================
    def mineLimitedPlusRetry(self, stck, verbose=False, RETRY_WITH_INC_INT_NN_=True):
        nounce = 0
        if verbose:
            print(stck)
        if RETRY_WITH_INC_INT_NN_:
            nounce = 0
        keystormed, retry_conf = stck[0], stck[1]
        limit_retry = retry_conf["RETRY_LIMIT"]
        SIZE_SALT_RETRY_ = retry_conf["SIZE_SALT_RETRY_"]
        SALT_FOR_FIRST_TRY_ = retry_conf["SALT_FOR_FIRST_TRY_"]
        # =====================================
        STORE_OLD_KEY = keystormed
        RETRY_SALT = self.generate_one_key(SIZE_SALT_RETRY_)
        # =====================================
        for retry_n in range(0, limit_retry):
            # =====================================
            if retry_n > 0:
                keystormed = STORE_OLD_KEY
                keystormed = keystormed + RETRY_SALT
                if RETRY_WITH_INC_INT_NN_:
                    nounce += 1
                    keystormed = keystormed + str(nounce)
            elif retry_n == 0:
                if SALT_FOR_FIRST_TRY_:
                    keystormed = keystormed + RETRY_SALT
                    if RETRY_WITH_INC_INT_NN_:
                        nounce += 1
                        keystormed = keystormed + str(nounce)
            # =====================================
            mined = hashlib.sha512((keystormed).encode()).hexdigest()
            # =====================================
            if mined[0:self.sizerepeat] == self.caractrepeat*self.sizerepeat:
                print("0x{}".format(mined))
                # =====================================
                return {"mined": mined, "keystormed": keystormed}
        # =====================================
        return None
        # =====================================
    # =====================================

    def dump_n_encryptymined_by_password(self, nb_keygenerated_sub_, temporal_point, symlink_path, password, size_key=128, elongtheread=[1,2], sizerepeat=3, caractrepeat="0",
                                  nb_keygenerated_=100000, POOL_WORKERS_=1, RETRY_HASH_MODE_=True,
                                  RETRY_HASH_CONFIG={"RETRY_LIMIT": 10, "SIZE_SALT_RETRY_": 96, "SALT_FOR_FIRST_TRY_": False}):
        self.sizerepeat, self.caractrepeat = sizerepeat, caractrepeat
        self.count_hashed = 0
        key = self.read_one_key(
            symlink_path, size_key, nb_keygenerated_sub_, temporal_point, elongtheread)
        keystormed = [str(k)+str(password) for k in key]
        resultats = []
        with Pool(POOL_WORKERS_) as p:
            if RETRY_HASH_MODE_:
                stck = {"keystormed": keystormed, "RETRY_HASH_CONFIG": [
                    RETRY_HASH_CONFIG] * nb_keygenerated_}
                multistck1 = multi_stck(stck)
                resultats.append(p.map(self.mineLimitedPlusRetry,multistck1.valueToUnpacked()))
            else:
                resultats.append(p.map(self.minethat, keystormed))
        resultats = sorted(resultats)[0]
        self.count_hashed_total = len(resultats)
        resultats = [item for item in resultats if item != None]
        self.count_hashed_ok = len(resultats)
        self.count_hashed_fail = abs(
            self.count_hashed_ok - self.count_hashed_total)
        return {
            "results": resultats,
            "count_hashed_OK": "{}".format(self.count_hashed_ok),
            "count_hashed_FAIL": "{}".format(self.count_hashed_fail),
            "count_hashed_TOTAL": "{}".format(self.count_hashed_total)
        }

    def read_one_key(self, symlink, size_key, nb_keygenerated_sub_, temporal_point, elongtheread=[0,1]):
        f = open(symlink, "rb")
        endisat=f.seek(-512,2)
        A=f.read(512)
        f.seek(0,0)
        B=f.read(512)
        random.seed("{}{}{}".format(A,temporal_point,B))
        telled = f.seek(0,2)
        print("KEYSIZE({})".format(telled))
        KEY = b''
        itmsk=[]
        for j in range(0,nb_keygenerated_sub_):
            for n in range(0,size_key):
                #print("({})[{}]".format(j/nb_keygenerated_sub_,n/size_key))
                ColoredProgressBar(j + 1, nb_keygenerated_sub_, prefix='Current Key({}%) - Global Progress:'.format(int(round((n/size_key)*100.0))),
                                 suffix='Complete', length=50)
                f.seek(random.randint(512, endisat), 0)
                KEY=KEY+f.read(1+random.randint(elongtheread[0],elongtheread[1]))
            itmsk.append(KEY)
            KEY=b''
        return itmsk
    
    #symlink="/dev/sr0"
    #print(read_one_key(symlink,4096,8,"rick"))

# ==========================================================================
# Add paste library's (favorites)
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
# ==========================================================================


def ColoredProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    if filledLength >= 1: bar = colored(fill * (filledLength-1),'yellow')+colored(fill*1,'red')+ colored('-' * (length - filledLength),"green")
    if filledLength < 1: bar = colored(fill * filledLength, 'red') + colored('-' * (length - filledLength), "red")
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
# ==========================================================================
# =====================================
# Fonctions extra


def transform2HumanCharset(randomdata):
	charset = [
	    i for i in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789/*-+@()[]#€$%:;,?.!"]
	acc = []
	#char 0-255
	for c in randomdata:
		acc.append(charset[int(ord(c)) % len(charset)])
	return "".join(acc)


def reverse(item):
	return item[::-1]


def urandom_integer(min_=1000, max_=5000, loop=1000000, START_=0, STOP_=None):
    number = START_
    for i in range(0, loop):
        number += int(ord(os.urandom(1)))
        if STOP_ != None:
            if number == STOP_:
                break
    if number <= min_:
        number = abs(number % -min_)
    return number % max_

# ==========================================================================


import gzip
class Rules_Dictator(object):
    def __init__(self,secret_init):
        random.seed(secret_init)
        self.external_senses = external_senses()
        self.Version="1.0"
        self.CodeName="Rules-Dictator"
        self.IsAnBetaVersion=True
        self.describe=("PDTSLSW-RULES")
        self.Authors=["Rick Sanchez (D-634)"]
        self.Contact_Dev=["Rick Sanchez Contact e-mail: {}".format("informabox.contact@gmail.com")]
        self.TRV1 = TrueRandom_v1()
    # =====================================
    def notify_user(self, title, message):
        os.system("notify-send '{}' '{}'".format(title,message))
    # =====================================
    # MONITOR OF RESSOURCES
    # =====================================
    def display_entropy(self):
        entropy = self.external_senses = self.get_entropy()
        self.notify_user("ENTROPY INFO", "Entropy: "+str(entropy))
    def display_WARNING_entropy(self):
        entropy = self.external_senses = self.get_entropy()
        if entropy<200:
            self.notify_user("ALERT OF SECURITY!", "Entropy too low, DANGER for SSL and cryptography!")
            self.display_entropy()
    # =====================================
    #self.external_senses.get_time_from_internet()
    # =====================================
    def input_password(self):
        password = ""
        while True:
            x = getch.getch()
            if x == '\n':
                break
            sys.stdout.write("*")
            password += x
        return password
    # =====================================
    # SECRET PIN GENERATOR

    def PIN_GENERATOR(self, TADSAD_SEED):
        TADSAD_SEED_R = TADSAD_SEED["results"]
        BIGSEED=b''
        VERIFICATION_CODES=""
        #for i in TADSAD_SEED_R:
        keystormed = TADSAD_SEED_R[0]["keystormed"]  # for seed
        mined = TADSAD_SEED_R[0]["mined"]  # for verification
        BIGSEED = keystormed.encode()
        VERIFICATION_CODES=str(mined)+"\n"
        
        VERIFICATION_CODES = VERIFICATION_CODES.strip()
        random.seed(BIGSEED)
        RANDOM_DATA="".join(map(str,[random.randint(0,9) for i in range(1,6)]))
        return {"pin": RANDOM_DATA, "mined": VERIFICATION_CODES}
    # =====================================
    def PASSWORD_GENERATOR(self,TADSAD_SEED):
        TADSAD_SEED_R = TADSAD_SEED["results"]
        BIGSEED=b''
        VERIFICATION_CODES=""
        #for i in TADSAD_SEED_R:
        keystormed = TADSAD_SEED_R[0]["keystormed"]  # for seed
        mined = TADSAD_SEED_R[0]["mined"]  # for verification
        BIGSEED = keystormed.encode()
        VERIFICATION_CODES=str(mined)+"\n"
        
        VERIFICATION_CODES = VERIFICATION_CODES.strip()
        random.seed(BIGSEED)
        RANDOM_DATA="".join([chr(random.randint(0,255)) for i in range(1,20)])
        return {"password": transform2HumanCharset(RANDOM_DATA), "mined": VERIFICATION_CODES}
    # =====================================

    def KEY_SELECTOR(self, TADSAD_SEED):
        TADSAD_SEED_R = TADSAD_SEED["results"]
        BIGSEED=b''
        VERIFICATION_CODES=""
        #for i in TADSAD_SEED_R:
        keystormed = TADSAD_SEED_R[0]["keystormed"]  # for seed
        mined = TADSAD_SEED_R[0]["mined"]  # for verification
        BIGSEED = keystormed.encode()
        VERIFICATION_CODES=str(mined)+"\n"
        
        VERIFICATION_CODES = VERIFICATION_CODES.strip()
        random.seed(BIGSEED)
        if self.yesORnoASK(colored("Generate an key? ",'yellow')):
            name = str(urandom_integer(min_=10,max_=100000000000))
            with open(name+".bin","w") as f:
                [f.write(chr(random.randint(0,255))) for i in range(0,4096)]
                f.close()
            print("Key saved into: {}".format(name+".bin"))
    # =====================================
    def detected_CDROM(self):
        list_cdrom_drives=[]
        for i in range(0,99):
            pathofthat = "/dev/sr{}".format(i)
            if os.path.exists(pathofthat):
                list_cdrom_drives.append(pathofthat)
        return list_cdrom_drives
    # =====================================
    def yesORnoASK(self,ask):
        print(colored("{} (Yes/No)?".format(ask), 'red'))
        reply=input(":")
        if (reply.upper()=="Y") or (reply.upper()=="YES"): 
            return True
        elif (reply.upper()=="N") or (reply.upper()=="NO"): 
            return False
        else:
            return self.yesORnoASK(ask)
    # =====================================     
    def insert_CDROM(self,detected_CDROM):
        for srcur in detected_CDROM:
            if self.yesORnoASK("USE THE CDROM ON '{}' SYMLINK?".format(srcur)): 
                return srcur
        return False
    # =====================================
    
    # =====================================
    def select_persistance_timeset_mode(self): 
        message = """ 
        (0) Ponctuality time set mode - YYYY+MM+DD+HH 
        (1) Presence time set mode - YYYY+MM+DD
        (2) Skipped time set mode - YYYY+MM 
        (3) absence time set mode - YYYY
        [> or < after 3 for next of past year]
        """
        print(message)
        reply = input("choice: ")
        try:
            if ( int(reply) > 3 ) or ( int(reply) < 0 ):
                return self.select_persistance_timeset_mode()
        except:
            return reply
        return reply 
    # ===================================== 
    def get_datetime_withmode(self,code): 
        flag_temporal = datetime.now()
        YYYY,MM,DD,HH = flag_temporal.year,flag_temporal.month,flag_temporal.day,flag_temporal.hour
        if (code=="0"): 
            flag_temporal = datetime(YYYY,MM,DD,HH)
        elif (code == "1"):
            flag_temporal = datetime(YYYY,MM,DD)
        elif (code == "2"):
            flag_temporal = datetime(YYYY,MM,1)
        elif (code == "3"):
            flag_temporal = datetime(YYYY,1,1)
        elif (code == "3>"):
            flag_temporal = datetime(YYYY+1,1,1)
        elif (code == "3<"):
            flag_temporal = datetime(YYYY-1, 1, 1)
        return flag_temporal
    # ===================================== 
    def welcome(self):
        os.system("clear")
        print(""" 
        
        By Rick Sanchez, The programmer with an ADHD brain.
        Pour toi ma Gabi chérie [Je t'aime fort ❤❤❤❤❤❤❤^+∞]
        """)
        if self.IsAnBetaVersion==True:
            print("!!__--**~IS AN BETA VERSION~**--__!!") 
        print("# ===================================== #")
        print("PDTSLSW\n{}\nCODENAME: {}\nVersion: {}\nAuthors: {}\nDev Contact: {}\n".format(
            self.describe, self.CodeName, self.Version, "\n".join(self.Authors), "\n".join(self.Contact_Dev)))
        print("# ===================================== #")
        print("""
        WELCOME TO THE NORMAL USE CASE, END OF END, LAST STEP, AND YOU      
        CAN NOW USE THE 'NoNeedBrainForPassword'... Enjoy !    
        """) 
    # ===================================== 
    def TADSAD2SEED_fn(self, password, temporal_point, symlink_path, nb_keygenerated_sub):
        message = """
        SECURITY AND SPEED MODE:
        (0) TURTLE
        (1) RABBIT
        (2) CAT
        (3) USS_ENTERPRISE
        """
        print(message)
        reply = input("choice: ")
        if ( int(reply) > 3 ) or ( int(reply) < 0 ):
            return self.TADSAD2SEED_fn(password, temporal_point, symlink_path, nb_keygenerated_sub)
        if reply=="0":
            data_trv = self.TRV1.dump_n_encryptymined_by_password(nb_keygenerated_sub, temporal_point, symlink_path, password, size_key=24, sizerepeat=5, elongtheread=[0, 8], caractrepeat="0",
                            nb_keygenerated_=nb_keygenerated_sub, POOL_WORKERS_=12, RETRY_HASH_MODE_=True,
                            RETRY_HASH_CONFIG={"RETRY_LIMIT": 1000000, "SIZE_SALT_RETRY_": 0, "SALT_FOR_FIRST_TRY_": False})#tortue
        elif reply=="1":
            data_trv = self.TRV1.dump_n_encryptymined_by_password(int(nb_keygenerated_sub/2), temporal_point, symlink_path, password, size_key=4, sizerepeat=3, elongtheread=[0, 1024], caractrepeat="1",
                            nb_keygenerated_=nb_keygenerated_sub, POOL_WORKERS_=4, RETRY_HASH_MODE_=True,
                            RETRY_HASH_CONFIG={"RETRY_LIMIT": 1000000, "SIZE_SALT_RETRY_": 0, "SALT_FOR_FIRST_TRY_": False})  # lapin

        elif reply=="2":
            data_trv = self.TRV1.dump_n_encryptymined_by_password(int(nb_keygenerated_sub/2), temporal_point, symlink_path, password, size_key=4, sizerepeat=4, elongtheread=[0, 96], caractrepeat="2",
                            nb_keygenerated_=nb_keygenerated_sub, POOL_WORKERS_=4, RETRY_HASH_MODE_=True,
                            RETRY_HASH_CONFIG={"RETRY_LIMIT": 1000000, "SIZE_SALT_RETRY_": 0, "SALT_FOR_FIRST_TRY_": False})  # chat
        
        elif reply=="3": 
            data_trv = self.TRV1.dump_n_encryptymined_by_password(nb_keygenerated_sub, temporal_point, symlink_path, password, size_key=8, sizerepeat=5, elongtheread=[0, 16], caractrepeat="3",
                            nb_keygenerated_=nb_keygenerated_sub, POOL_WORKERS_=4, RETRY_HASH_MODE_=True,
                            RETRY_HASH_CONFIG={"RETRY_LIMIT": 1000000, "SIZE_SALT_RETRY_": 0, "SALT_FOR_FIRST_TRY_": False})  # USS_Enterprise
        
        return data_trv
    # =====================================

    def show_output(self):
        print("""
        The generation it's done !
        HASH CODE FOR VERIFICATION OF AUTHENTICITY {}
        
        Password in output: {}  
        PIN CODE: {}   
        
        Note your HASH CODE VERIFICATION and compare if you need to check at the next time.
        Don't keep note your password, you can use password saves functions under protection by master password on your navigator,
        Every time you type the MagicPassword with this RAWKEY-CDROM and timestamp seed settings in current range, you get this password !  
        If You generate another time (our of current range with the settings of timestamp) the password is fully different. 
        So you have the keys of the infinite !
        
           -Rick Sanchez D-634   
        """.format(self.out_mined, self.out_password, self.out_pin))
        while(True):
            if self.yesORnoASK("READY TO EXIT Rules-Dictator ?"):
                break
            else:
                print("OK OK I WAIT...")
    
    # =====================================
    def run(self):
        self.welcome()
        srcur = self.insert_CDROM(self.detected_CDROM())
        if srcur == False:
            exit(0) 
        OUTOFTIME_ = datetime.now()
        self.notify_user("TIME REGISTERED:","Dont forgot the {}".format(OUTOFTIME_))
        datetimeOfTimeTravel = self.get_datetime_withmode(self.select_persistance_timeset_mode())
        print("Magic Password: ")
        MagicPasswordInput = self.input_password()
        print("RETYPE THE, Magic Password: ")
        MagicPasswordInput2 = self.input_password()
        if MagicPasswordInput!=MagicPasswordInput2: 
            print("ERROR NOT SAME PASSWORDS !")
            exit(-1)
        TADSAD_SEED = self.TADSAD2SEED_fn(MagicPasswordInput,hashlib.sha512(
            str(datetimeOfTimeTravel).encode()).hexdigest(), srcur, 256)
        #print(TADSAD_SEED)
        #GENETERATE PIN ,PASSWORD COMPREHENSIVE BY HUMAN WITH THE SEED'S 
        PASSWDOUT = self.PASSWORD_GENERATOR(TADSAD_SEED)
        self.out_password = PASSWDOUT["password"]
        self.out_mined = PASSWDOUT["mined"]
        self.out_pin = self.PIN_GENERATOR(TADSAD_SEED)["pin"]
        #Selector of sector key in a matricial representation of the stream
        self.KEY_SELECTOR(TADSAD_SEED)
        print("Remember: {}".format(str(datetimeOfTimeTravel)))
        self.show_output()
    # =====================================    
    """
    def run(self,srcur, notify_me=False):
        OUTOFTIME_ = datetime.now()
        if notify_me: self.notify_user("TIME REGISTERED:","Dont forgot the {}".format(OUTOFTIME_))
        datetimeOfTimeTravel = self.get_datetime_withmode(self.select_persistance_timeset_mode())
        print("Magic Password: ")
        MagicPasswordInput = self.input_password()
        print("RETYPE THE, Magic Password: ")
        MagicPasswordInput2 = self.input_password()
        if MagicPasswordInput!=MagicPasswordInput2: 
            print("ERROR NOT SAME PASSWORDS !")
            exit(-1)
        TADSAD_SEED = self.TADSAD2SEED_fn(MagicPasswordInput,hashlib.sha512(
            str(datetimeOfTimeTravel).encode()).hexdigest(), srcur, 256)
        #print(TADSAD_SEED)
        #GENETERATE PIN ,PASSWORD COMPREHENSIVE BY HUMAN WITH THE SEED'S 
        PASSWDOUT = self.PASSWORD_GENERATOR(TADSAD_SEED)
        self.out_password = PASSWDOUT["password"]
        self.out_mined = PASSWDOUT["mined"]
        self.out_pin = self.PIN_GENERATOR(TADSAD_SEED)["pin"]
        #Selector of sector key in a matricial representation of the stream
        self.KEY_SELECTOR(TADSAD_SEED)
        print("Remember: {}".format(str(datetimeOfTimeTravel)))
        self.show_output()
    """

RD = Rules_Dictator(634)
RD.run()
