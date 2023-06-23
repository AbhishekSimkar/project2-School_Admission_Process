import sys
from prettytable import PrettyTable
import mysql.connector as con
mydb=con.connect(host='localhost',user='root',password='1234',database='KVSadm')
mycursor=mydb.cursor()

def Search_Details():
    try:
        while True:
            print(''' \n
                        1: Search Details Using Form NO. And Name. \n
                        2: Search Details Using Form No. And Phone No. \n
                        3: Search Details Using Name And Phone No. \n
                        4:Exit''')
            ch=int(input("\n\t\t\t\t Enter your choice :"))
            if ch==1:
                fn=int(input("\n\t\t\t\t Enter Form No. :"))
                n=input(" \t\t\t\t Enter Name :")
                mycursor.execute("select* from Admission where (FormNo=%s and Name=%s)",(fn,n))
                l=list(mycursor.fetchone())
                flag=0
                if fn in l and n in l:
                    print("\n\t\t\t\t\t!!Congrats your Record found!!")
                    flag=1
                    print("\n\t\t\t\t Do You Want To View your Details :")
                    print("\t\t\t\t\t Y:For View Details. ")
                    print("\t\t\t\t\t N:For EXIT")
                    ch5=input("\n\t\t\t\t Enter your choice :")
                    if ch5=="Y":
                        mycursor.execute("select Name,Fname,Mname,CastCategory,ContactNo,Email,AdmNo,ServiceCategory,Age,Gender from Admission where (FormNo=%s and Name=%s)",(fn,n))
                        t = PrettyTable(['Name','Fname','Mname','C_CAT','Cont_No.','Email','AdmNo','S_CAT','AGE','Gender'])
                        for x in mycursor:
                            t.add_row(list(x))
                        print(t)
                        
                    elif ch5=="N":
                        break
                    else:
                        sys.stderr.write('\n\t\t\tSorry! Invalid Option ,Try Again')
                        break
                if flag==0:
                    print("\t\t Sorry No Such Records Found")
                    
            elif ch==2:
                fn=int(input("\n\t\t\t\t Enter Form No."))
                p=input("\t\t\t\t Enter Phone NO.:")
                mycursor.execute("select* from Admission where (FormNo=%s and ContactNo=%s)",(fn,p))
                l=list(mycursor.fetchone())
                flag=0
                if fn in l and p in l:
                    print("\n\t\t\t\t\t !!Congrats your Record Found !!")
                    flag=1
                    print("\n\t\t\t\t Do You Want To View your Details :")
                    print("\t\t\t\t\t Y:For View Details. ")
                    print("\t\t\t\t\t N:FOR EXIT")
                    ch5=input("\n\t\t\t\t Enter your choice :-")
                    if ch5=="Y":
                        mycursor.execute("select Name,Fname,Mname,CastCategory,ContactNo,Email,AdmNo,ServiceCategory,Age,Gender from Admission where (FormNo=%s and ContactNo=%s)",(fn,p))
                        t = PrettyTable(['Name','Fname','Mname','C_CAT','Cont_No.','Email','AdmNo','S_CAT','AGE','Gender'])
                        for x in mycursor:
                            t.add_row(list(x))
                        print(t)
                        
                    elif ch5=="N":
                        break
                    else:
                        sys.stderr.write('\n\t\t\tSorry! Invalid Option ,Try Again')
                        break

            elif ch==3:
                n=input("\n\t\t\t\t Enter Name :-")
                p=input("\t\t\t\t Enter Phone No. :-")
                mycursor.execute("select* from Admission where (Name=%s and ContactNo=%s)",(n,p))
                l=list(mycursor.fetchone())
                flag=0
                if n in l and p in l:
                    print("\n\t\t\t\t\t !!Congrats your Record Found !!")
                    flag=1
                    print("\n\t\t\t\t Do You Want To View your Details :")
                    print("\t\t\t\t\t Y:For View Details. ")
                    print("\t\t\t\t\t N:FOR EXIT")
                    ch5=input("\n\t\t\t\t Enter your Choice:")
                    if ch5=="Y":
                        mycursor.execute("select Name,Fname,Mname,CastCategory,ContactNo,Email,AdmNo,ServiceCategory,Age,Gender from Admission where (Name=%s and ContactNo=%s)",(n,p))
                        t = PrettyTable(['Name','Fname','Mname','C_CAT','Cont_No.','Email','AdmNo','S_CAT','AGE','Gender'])
                        for x in mycursor:
                            t.add_row(list(x))
                        print(t)
                        
                    elif ch5=="N":
                        break
                    else:
                        sys.stderr.write('\n\t\t\tSorry! Invalid Option ,Try Again')
                        break                    
            elif ch==4:
                break
            else:
                sys.stderr.write('\n\t\t\tSorry! Invalid Option ,Try Again')
    except:
        sys.stderr.write("\n\t\t\t\t Sorry! no such record found\n\n")

def SEARCH_Details1():
    try:
        while True:
            ch1=int(input('''\n \t\t\t\t\t !!!WELCOME TO SEARCH BAR !!! \n
                             1: Show All Records \n
                             2: Search Particular Records \n
                             3: Exit \n
                             Your Choice please :-'''))
            if ch1==1:
                mycursor.execute("select* from Admission ")
                d=list(mycursor.fetchall())
                if len(d)==0:
                    print("\n\t\t\t\tNo one is applied for Admission yet!!!\n")
                else:
                    mycursor.execute("select Name,Fname,Mname,CastCategory,ContactNo,Email,AdmNo,ServiceCategory,Age,Gender from Admission")
                    t = PrettyTable(['Name','Fname','Mname','C_CAT','Cont_No.','Email','AdmNo','S_CAT','AGE','Gender'])
                    for x in mycursor:
                        t.add_row(list(x))
                    print(t)
                    
            elif ch1==2:
                Search_Details()
            elif ch1==3:
                break
            else:
                sys.stderr.write('\n\t\t\t\tSorry! Invalid Option ,Try Again')
    except:
        sys.stderr.write("\n\t\t\t\tSorry! no such record found\n\n")



        



    

















                    

