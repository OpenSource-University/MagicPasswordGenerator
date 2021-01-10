from JumpDB import jumpdatabase as jdb 
from base64 import b64encode as b64enc
class dbmanager(object):
    def __init__(self):
        self.db=jdb.jumpdb()
    def load_db(self,filepath):
        self.db.load(filepath)
    def save_db(self,filepath):
        self.db.save(filepath)
    def insertFile(self,namefile,datefirst,
                        typefile,author,datafile):
        data_dict={
            "namefile":namefile,
            "datefirst":datefirst,
            "typefile":typefile,
            "autor":author,
            "b64data": b64enc(datafile).decode()
        }
        ID = self.db.insert(data_dict)
    def removeFile(self,id_):
        self.db.delete(id_)


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