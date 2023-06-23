import sys
from prettytable import PrettyTable
import mysql.connector as con
mydb=con.connect(host='localhost',user='root',password='1234',database='KVSadm')
mycursor=mydb.cursor()

def Update_Details():
    try:
        print('''\t\t\t\t\t !!! WELCOME TO UPDATE SECTION !!! \n
        \t\tFOR UPDATING ANY DETAILS WE NEED TO VERIFY YOUR FORM NUMBER AND NAME\n''')
        fn=int(input("\t\t\tEnter Form No. :"))
        n=input("\t\t\tEnter Name :")
        mycursor.execute("select * from Admission where (FormNo=%s and Name=%s)",(fn,n))
        l=list(mycursor.fetchone())
        if fn in l and n in l:
            print("\n\t\t\t\t !!!CONGRATS RECORD FOUND!!! \n")
        while True:
            print('''\t\t\t1:FOR UPDATE NAME
                        2:FOR UPDATE FATHER NAME
                        3:FOR UPDATE MOTHER NAME
                        4:FOR UPDATE CAST CATEGORY
                        5:FOR UPDATE CONTACT NUMBER
                        6:FOR UPDATE EMAIL
                        7:FOR UPDATE SERVICE CATEGORY
                        8:FOR UPDATE AGE
                        9:FOR UPDATE GENDER
                        10:exit''')
            ch4=int(input("\n\t\t\tEnter your Choice :"))
            if ch4==1:
                a=input("\n\t\t\tEnter Name to Update :")
                mycursor.execute("update Admission set Name=%s where FormNo=%s",(a,fn))
                mydb.commit() 
                print("\n\t\t\tCONGRATS RECORD UPDATED")
                print("\t\t\tYour updated record")
                mycursor.execute("select Name,Fname,Mname,ContactNo,FormNo from Admission where FormNo=%s",(fn,))
                t = PrettyTable(['Name','F_name','M_name','Contact_No.','Form_No'])
                for x in mycursor:
                    t.add_row(list(x))
                print(t)

            elif ch4==2:
                a=input("\n\t\t\tEnter Father's Name to update :")
                mycursor.execute("update Admission set Fname=%s where FormNo=%s",(a,fn))
                mydb.commit()
                print("\n\t\t\tCONGRATS RECORD UPDATED")
                mycursor.execute("select Name,Fname,Mname,ContactNo,FormNo from Admission where FormNo=%s",(fn,))
                t = PrettyTable(['Name','F_name','M_name','Contact_No.','Form_No'])
                for x in mycursor:
                    t.add_row(list(x))
                print(t)

            elif ch4==3:
                a=input("\n\t\t\tEnter Mother's Name to Update :")
                mycursor.execute("update Admission set Mname=%s where FormNo=%s",(a,fn))
                mydb.commit()
                print("\n\t\t\tCONGRATS RECORD UPDATED")
                mycursor.execute("select Name,Fname,Mname,ContactNo,FormNo from Admission where FormNo=%s",(fn,))
                t = PrettyTable(['Name','F_name','M_name','Contact_No.','Form_No'])
                for x in mycursor:
                    t.add_row(list(x))
                print(t)
                
            elif ch4==4:
                a=int(input("\n\t\t\tEnter Cast Category to update :"))
                mycursor.execute("update Admission set CastCategory=%s where FormNo=%s",(a,fn))
                mydb.commit()
                print("\n\t\t\tCONGRATS RECORD UPDATED")
                mycursor.execute("select Name,Fname,Mname,ContactNo,FormNo,CastCategory from Admission where FormNo=%s",(fn,))
                t = PrettyTable(['Name','F_name','M_name','Contact_No.','Form_No','Cast_CAT'])
                for x in mycursor:
                    t.add_row(list(x))
                print(t)
                
            elif ch4==5:
                while True:
                    try:
                        a=input("\n\t\t\tEnter Contact No. to Update :")
                        if len(a)==10:
                            mycursor.execute("update Admission set ContactNo=%s where FormNo=%s",(a,fn))
                            mydb.commit()
                            print("\n\t\t\tCONGRATS RECORD UPDATED")
                            mycursor.execute("select Name,Fname,Mname,ContactNo,FormNo from Admission where FormNo=%s",(fn,))
                            t = PrettyTable(['Name','F_name','M_name','Contact_No.','Form_No'])
                            for x in mycursor:
                                t.add_row(list(x))
                            print(t)
                            break
                        else:
                            sys.stderr.write("\n\t\t\tSorry! invalid contact number\n\n")
                    except:
                        break
            elif ch4==6:
                while True:
                    try:
                        a=input("\n\t\t\tEnter New Email to Update :")
                        if a[-10:]=='@gmail.com':
                            mycursor.execute("update Admission set Email=%s where FormNo=%s",(a,fn))
                            mydb.commit()
                            print("\n\t\t\tCONGRATS RECORD UPDATED")
                            mycursor.execute("select Name,Fname,Mname,ContactNo,FormNo,Email from Admission where FormNo=%s",(fn,))
                            t = PrettyTable(['Name','F_name','M_name','Contact_No.','Form_No','Email'])
                            for x in mycursor:
                                t.add_row(list(x))
                            print(t)
                            break
                        else:
                            sys.stderr.write("\n\t\t\tSorry! invalid Email Id\n\n")
                    except:
                        break
            elif ch4==7:
                a=int(input("\n\t\t\tEnter Service Category to Update :"))
                mycursor.execute("update Admission set ServiceCategory=%s where FormNo=%s",(a,fn))
                mydb.commit()
                print("\n\t\t\tCONGRATS RECORD UPDATED")
                mycursor.execute("select Name,Fname,Mname,ContactNo,FormNo,ServiceCategory from Admission where FormNo=%s",(fn,))
                t = PrettyTable(['Name','F_name','M_name','Contact_No.','Form_No','Service_CAT'])
                for x in mycursor:
                    t.add_row(list(x))
                print(t)
                
            elif ch4==8:
                a=int(input("\n\t\t\tEnter Age to Update :"))
                mycursor.execute("update Admission set Age=%s where FormNo=%s",(a,fn))
                mydb.commit()
                print("\n\t\t\tCONGRATS RECORD UPDATED")
                mycursor.execute("select Name,Fname,Mname,ContactNo,FormNo,Age from Admission where FormNo=%s",(fn,))
                t = PrettyTable(['Name','F_name','M_name','Contact_No.','Form_No','Age'])
                for x in mycursor:
                    t.add_row(list(x))
                print(t)
                
            elif ch4==9:
                a=input("\n\t\t\tEnter Gender to Update :")
                mycursor.execute("update Admission set Gender=%s where FormNo=%s",(a,fn))
                mydb.commit()
                print("\n\t\t\tCONGRATS RECORD UPDATED")
                mycursor.execute("select Name,Fname,Mname,ContactNo,FormNo,Gender from Admission where FormNo=%s",(fn,))
                t = PrettyTable(['Name','F_name','M_name','Contact_No.','Form_No','Gender'])
                for x in mycursor:
                    t.add_row(list(x))
                print(t)
            else:
                break                
    except:
        sys.stderr.write("\n\t\t\tSorry! No such record found\n\n")










                        
