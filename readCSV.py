def readCSV(path):
    f=open(path,'r+')
    di=f.read()
    f.close()
    w=di.split("\n")
    key_list=w[0].split(",")
    value_list=[s.split(',') for s in w[1:]]
    di={}
    for i in range(len(key_list)):
        di[key_list[i]]=[]
        for j in range(len(value_list)-1):
                di[key_list[i]].append(value_list[j][i])
    return di

import sqlite3

def insrt(dic,pat):
    key_list=list(dic.keys())
    value=list(dic.values())
    db = sqlite3.connect(pat)
    db.execute('DROP TABLE IF EXISTS mytable')
    db.execute('CREATE TABLE mytable({} TEXT)'.format(key_list[0]))
    db.commit()
    for i in range(1,len(key_list)):
        db.execute('ALTER TABLE mytable ADD {} TEXT'.format(key_list[i]))
        db.commit()
    for j in range(len(value[0])):
        db.execute('INSERT INTO mytable ({}) VALUES ("{}")'.format(key_list[0],value[0][j]))
        db.commit()
        for i in range(1,len(key_list)):
            db.execute('UPDATE mytable SET {}="{}" WHERE {}="{}"'.format(key_list[i],value[i][j],key_list[0],value[0][j]))
            db.commit()
    db.close()
