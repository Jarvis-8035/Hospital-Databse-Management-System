import sqlite3

def insrt(dic,pat):
    key_list=list(dic.keys())
    value=list(dic.values())
    db = sqlite3.connect(pat)
#    db.execute('DROP TABLE IF EXISTS mytable')
#    db.execute('CREATE TABLE mytable({} TEXT)'.format(key_list[0]))
#    db.commit()
#    for i in range(1,len(key_list)):
#        db.execute('ALTER TABLE mytable ADD {} TEXT'.format(key_list[i]))
#        db.commit()
    for j in range(len(value[0])):
        db.execute('INSERT INTO mytable ({}) VALUES ("{}")'.format(key_list[0],value[0][j]))
        db.commit()
        for i in range(1,len(key_list)):
            db.execute('UPDATE mytable SET {}="{}" WHERE {}="{}"'.format(key_list[i],value[i][j],key_list[0],value[0][j]))
            db.commit()
    db.close()

#insrt(readCSV("File1.csv"))

#db = sqlite3.connect('F:\\mydb1.db')
#k = db.execute('SELECT * FROM mytable')
#db.commit()
#for i in k:
#    print(i)
