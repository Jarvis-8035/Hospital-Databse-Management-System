import sqlite3
import readCSV
import readCSV_pat
import readDB
class Hospital():
    patient_no=0
    Name=""
    disease_list=["Flu","Allergy","Infection","Skin Problem","Fracture","Physiotherapy"]
    def __init__(self,name):
        self.Name=name
        self.patient_no=Hospital.patient_no
    def problem(self,disease):
        if disease in Hospital.disease_list:
            hel=[]
            app_doc=[]
            docs=readDB.re('Doctor_Db.db')
#            readCSV.insrt(docs,"Doctor_Db.db")
            print("Just wait for a sec while we check our Availability of the Doctor....")
            for j in range(len(docs[list(docs.keys())[0]])):
                for i in range(1,len(list(docs.keys()))-1):
                    if docs[list(docs.keys())[i]][j]==disease and docs['Free'][j]=='Yes':
                        hel.append(docs[list(docs.keys())[0]][j])
                    elif docs[list(docs.keys())[i]][j]==disease:
                        app_doc.append(docs[list(docs.keys())[0]][j])
            ptnt={'Name':[],'Disease':[],'Waiting':[],'Bed':[],'Appointment':[],'Doctor_Assigned':[]}
            if len(hel)==0:
                print("""Sorry , we don't have any doctor free right Now. You can take a future Appointment for the following doctors : """)
                print(" , ".join(app_doc))
                x=int(input())
                ptnt['Appointment']=["Yes"]
                ptnt['Doctor_Assigned']=[app_doc[x-1]]
            else:
                print("You can consult to the following docters :")
                print(" , ".join(hel))
                x=int(input())
                ptnt['Appointment']=["No"]
                ptnt['Doctor_Assigned']=[hel[x-1]]
                f=0
                le=len(docs['DcotorName'])
                for i in range(le):
                    if docs['DoctorName'][i]==hel[x-1]:
                        f=i
                        break
                docs['Free'][f]="No"
                readCSV.insrt(docs,'Doctor_Db.db')
#            Patient Record Update
            ptnt['Name'].append(self.Name)
            ptnt['Disease'].append(disease)
            db = sqlite3.connect('Patient_Db.db')
            u = db.execute('SELECT * FROM mytable ORDER BY bed DESC LIMIT 1')
            k=u.fetchone()
            if k==None:
                self.patient_no=1
            else:
                self.patient_no=int(list(k)[3])+1
            db.close()
            if len(hel)==0:
                ptnt['Waiting'].append('Yes')
                print("Doctor is currently unavailable but we have selected a future appointment for you")
            else:
                ptnt['Waiting'].append('No')
                ptnt['Bed'].append(str(self.patient_no))
            readCSV_pat.insrt(ptnt,'Patient_Db.db')
            d=readDB.re_p('Patient_Db.db')
        else:
            print("We can recommend you another Hospital which will treat you in a Better way")

a=Hospital("StarLord")
a.problem("Allergy")
a=Hospital("Drax")
a.problem("Fracture")
a=Hospital("Rocket")
a.problem("Flu")
a=Hospital("Gamora")
a.problem("Infection")
a=Hospital("Groot")
a.problem("Physiotherapy")

e=readDB.re_p('Patient_Db.db')
print(e)
e=readDB.re('Doctor_Db.db')
print(e)

