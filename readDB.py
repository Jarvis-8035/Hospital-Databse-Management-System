import sqlite3
import readCSV
def re(path):
    db=sqlite3.connect(path)
    k=db.execute('SELECT * FROM mytable')
    di = readCSV.readCSV('Hospital_Doctor_Db.csv')
    for i in range(len(list(di.keys()))):
        di[list(di.keys())[i]]=[]
    while k!=None:
        w=k.fetchone()
        if w==None:
            break
        for i in range(len(list(w))):
            di[list(di.keys())[i]].append(list(w)[i])
    db.close()
    return di

def re_p(path):
    db=sqlite3.connect(path)
    k=db.execute('SELECT * FROM mytable')
    di={'Name':[],'Disease':[],'Waiting':[],'Bed':[],'Appointment':[],'Doctor_Assigned':[]}
    while k!=None:
        w=k.fetchone()
        if w==None:
            break
        for i in range(len(list(w))):
            di[list(di.keys())[i]].append(list(w)[i])
    db.close()
    return di
