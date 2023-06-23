import matplotlib.pyplot as plt
import mysql.connector as con
from prettytable import PrettyTable
mydb=con.connect(host='localhost',user='root',password='1234',database='KVSadm')
mycursor=mydb.cursor()

def sel_stud():
    mycursor.execute("select AdmNo,Name,Fname,ContactNo from lottery")
    t = PrettyTable(['Adm_No.','Name', 'F_Name','Contact_No.'])
    for x in mycursor:
        t.add_row(list(x))
    print(t)

    
