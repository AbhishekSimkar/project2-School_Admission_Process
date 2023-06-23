import random as r
import datetime
from prettytable import PrettyTable
import mysql.connector as con
mydb=con.connect(host='localhost',user='root',password='1234',database='KVSadm')
mycursor=mydb.cursor()

def lottery():
    student=30
    mycursor.execute('delete from lottery')
    for i in range(0,6):
        if i==0:
            mycursor.execute('select FormNo from Admission where ServiceCategory=0')
            RTE=list(mycursor.fetchall())
            l=[]
            for i in RTE:
                for k in i:
                    l.append(k)
            a=0
            for i in l:
                a+=1
            if a<=4 and a>0:
                for k in l:
                    mycursor.execute("select Name,Fname,Mname,CastCategory,ContactNo,Email,ServiceCategory,Age,Gender \
                                      from Admission where FormNo=%s",(k,))
                    RTE=mycursor.fetchall()
                    i=[]
                    for g in RTE:
                        for k in g:
                            i.append(k)
                    mycursor.execute("select max(AdmNo) from lottery")
                    row=mycursor.fetchone()
                    if row==(None,):
                        AdmNo=1
                    else:
                        f=list(row)
                        AdmNo=max(f)+1
                    mycursor.execute("insert into lottery values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(i[0],i[1],i[2],i[3],i[4],i[5],datetime.date.today(),AdmNo,i[6],i[7],i[8]))
                    mydb.commit()
            elif a==0:
                pass
            else:
                l1=[]
                def Edu():
                    x=r.sample(l,4)
                    if x not in l1:
                        l1.extend(x)
                    else:
                        Edu()
                Edu()
                for k in l1:
                    mycursor.execute("select Name,Fname,Mname,Castcategory,ContactNo,Email,Servicecategory,Age,Gender \
                                    from Admission where FormNo=%s",(k,))
                    RTE=mycursor.fetchone()
                    i=[]
                    for g in RTE:
                        for k in g:
                            i.append(k)
                    mycursor.execute("select max(AdmNo) from lottery")
                    row=mycursor.fetchone()
                    if row==(None,):
                        AdmNo=1
                    else:
                        f=list(row)
                        AdmNo=max(f)+1
                    mycursor.execute("insert into lottery values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(i[0],i[1],i[2],i[3],i[4],i[5],datetime.date.today(),AdmNo,i[6],i[7],i[8]))
                    mydb.commit()
            if a<=4:
                student-=a
            else:
                student-=4
        else:
            mycursor.execute('select FormNo from Admission where ServiceCategory=%s',(i,))
            CAT=list(mycursor.fetchall())
            l2=[]
            for i in CAT:
                for k in i:
                    l2.append(k)
            b=0
            for i in l2:
                b+=1
            if b<=student:
                for k in l2:
                    mycursor.execute("select Name,Fname,Mname,Castcategory,ContactNo,Email,ServiceCategory,Age,Gender \
                                      from Admission where FormNo=%s",(k,))
                    RTE=mycursor.fetchall()
                    i=[]
                    for g in RTE:
                        for k in g:
                            i.append(k)
                    mycursor.execute("select max(AdmNo) from lottery")
                    row=mycursor.fetchone()
                    if row==(None,):
                        AdmNo=1
                    else:
                        f=list(row)
                        AdmNo=max(f)+1
                    mycursor.execute("insert into lottery values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(i[0],i[1],i[2],i[3],i[4],i[5],datetime.date.today(),AdmNo,i[6],i[7],i[8]))
                    mydb.commit()
            elif b==0:
                pass
            else:
                l1=[]
                def Edu():
                    x=r.sample(l2,student)
                    if x not in l1:
                        l1.extend(x)
                    else:
                        Edu()
                Edu()
                for k in l1:
                    mycursor.execute("select Name,Fname,Mname,Castcategory,ContactNo,Email,ServiceCategory,Age,Gender \
                                    from Admission where FormNo=%s",(k,))
                    RTE=mycursor.fetchone()
                    i=[]
                    for g in RTE:
                        for k in g:
                            i.append(k)
                    mycursor.execute("select max(AdmNo) from lottery")
                    row=mycursor.fetchone()
                    if row==(None,):
                        AdmNo=1
                    else:
                        f=list(row)
                        AdmNo=max(f)+1
                    mycursor.execute("insert into lottery values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(i[0],i[1],i[2],i[3],i[4],i[5],datetime.date.today(),AdmNo,i[6],i[7],i[8]))
                    mydb.commit()
                    student-=b


    print( "\t\t\t\t!!!!Lottery Successful Done!!!!! " )
    mycursor.execute("select AdmNo,Name,Fname,ContactNo from lottery")
    t = PrettyTable(['Adm_No.','Name', 'F_Name','Contact_No.'])
    for x in mycursor:
        t.add_row(list(x))
    print(t)
