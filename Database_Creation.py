# To be Executed only Once.......
# If Executed more than once....Can result in Data Loss
import sqlite3
import readCSV
db = sqlite3.connect('Patient_Db.db')
ptnt={'Name':[],'Disease':[],'Waiting':[],'Bed':[],'Appointment':[],'Doctor_Assigned':[]}
readCSV.insrt(ptnt,'Patient_Db.db')
db = sqlite3.connect('Doctor_Db.db')
readCSV.insrt(readCSV.readCSV('Hospital_Doctor_Db.csv'),'Doctor_Db.db')
db.close()
