'''This module is for Registration for Admission'''

import datetime
import csv
import sys
import random as r
import mysql.connector as con
mydb=con.connect(host='localhost',user='root',password='1234',database='KVSadm')
mycursor=mydb.cursor()
def Add_Details():
    date=datetime.date.today()
    if str(date)>'2021-01-01':
        sys.stderr.write("\t\t\tSorry! Form is out of Date , You can't apply")
    else:   
        name=input("\n\t\t\tEnter name student :" )
        Fname=input("\t\t\tEnter father's name student :" )
        Mname=input("\t\t\tEnter mother's name student :" )
        while True:
            l=['general','obc','sc','st','other']
            try:
                cast=input("\t\t\tEnter your cast catagory- general/obc/sc/st/other :")
                if cast in l:
                    break
                else:
                    sys.stderr.write("\n\t\t\tSorry! invalid cast catagory\n\n")
            except:
                break
        while True:
            l=['m','f']
            try:
                Gender=input("\t\t\tEnter your Gender- m(male)/f(female) :")
                if gender in l:
                    break
                else:
                    sys.stderr.write("\n\t\t\tSorry! You have entered something Irrelevent\n\n")
            except:
                break
        while True:
            l=[5,6,7]
            try:
                Age=int(input("\t\t\tEnter your Age :"))
                if Age in l:
                    break
                else:
                    sys.stderr.write("\n\t\t\tSorry! Your Can't Register because of Age Restrictions\n\n")
            except:
                break
        while True:
            try:
                ph=input("\t\t\tEnter Contact number :" )
                if len(ph)==10:
                    break
                else:
                    sys.stderr.write("\n\t\t\tSorry! invalid contact number\n\n")
            except:
                break
        otp=r.randint(1000,9999)
        print('\n\t\t\tThis is one time OTP :',otp)
        check=int(input("\t\t\tEnter the OTP displaying on your Screen :"))
        if check==otp:
            print("\n\t\t\tverifieng your OTP...........")
            print("\t\t\tDone! your OTP is correct")
        else:
            sys.stderr.write("\n\t\t\tSorry! invalid OTP\n\n")
            passs()
        while True:
            try:
                email=input("\n\t\t\tEnter your Email Id :" )
                if email[-10:]=='@gmail.com':
                    break
                else:
                    sys.stderr.write("\n\t\t\tSorry! invalid Email Id\n\n")
            except:
                break
        while True:
            l=[0,1,2,3,4,5]
            try:
                catagory=int(input('''\n\t\t\tEnter service catagory
                                    0 - Right to Education (RTE)
                                    1 - Catagory 1
                                    2 - Catagory 2
                                    3 - Catagory 3
                                    4 - Catagory 4
                                    5 - Catagory 5
                                    :'''))
                if catagory in l:
                    break
                else:
                    sys.stderr.write("\n\t\t\tSorry! invalid Service Catagory\n\n")
            except:
                break
        mycursor.execute("select max(FormNo) from Admission")
        row=mycursor.fetchone()
        if row==(None,):
            FormNo=1
        else:
            f=list(row)
            FormNo=max(f)+1
        mycursor.execute("insert into Admission values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,Fname,Mname,cast,ph,email,date,FormNo,catagory,Age,Gender))
        mydb.commit()
        file=open('C:/Users/hp/Desktop/F vs D.csv','a',newline='')
        w=csv.writer(file)
        w.writerow([FormNo,date])
        print('\n\t\t\tCongrats!Your form is submitted.')
        print('\t\t\tYour form no is : ',FormNo)

def passs():
    ch=input("\t\t\tResend the OTP press 'y' to continue and any other key to break :")
    if ch=="y":
        otp=r.randint(1000,9999)
        print('\n\t\t\tThis is one time OTP :',otp)
        check=int(input("\t\t\tEnter the OTP displaying on your device :"))
        if check==otp:
            print("\n\t\t\tverifieng your OTP")
            print("\t\t\tDone! your OTP is correct")
        else:
            sys.stderr.write("\n\t\t\tSorry! invalid OTP\n\n")
            passs()
    else:
        sys.stderr.write("\n\t\t\tFine! you have choosen to discontinue the process .\n\n")
