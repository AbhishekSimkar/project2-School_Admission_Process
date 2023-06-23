import sys
import mysql.connector as con
mydb=con.connect(host='localhost',user='root',password='1234',database='KVSadm')
mycursor=mydb.cursor()

def Delete_Details():
    try:
        while True:            
            print('''\n \t\t\t\t !!!!WELCOME TO DELETE SECTION !!!! \n 
                     \t 1: Delete your records using Form NO. And Name.
                     \t 2: Delete your records using Form NO. And Phone NO.
                     \t 3: Delete your records using Name And Phone NO.
                     \t 4: exit ''')
            ch=int(input("\t\t\t\t\t Please Enter your choice :"))
            if ch==1:
                fn=int(input("\n\t\t\t\tEnter your Form NO. :"))
                n=input("\t\t\t\tEnter your Name :")
                mycursor.execute("select * from Admission where (FormNo=%s and Name=%s)",(fn,n))
                l=list(mycursor.fetchone())
                flag=0
                if fn in l and n in l:
                    print("\n\t\t\t\t\t Congrats your Record founded here")
                    flag=1
                    mycursor.execute("delete from Admission where (FormNo=%s and Name=%s)",(fn,n))
                    mydb.commit()
                    print("\n\t\t\t\tDELETING......")
                    print("\t\t\t\t\t Congrats your Record DELETED. ")                       
                if flag==0:
                    sys.stderr.write("\n\t\t\t\tSorry no such record founds !\n\n")
            elif ch==2:
                fn=int(input("\n\t\t\t\tEnter your Form No. :"))
                p=input("\t\t\t\tEnter your Phone No. :")
                mycursor.execute("select* from Admission where (FormNo=%s and ContactNo=%s)",(fn,p))
                l=list(mycursor.fetchone())
                flag=0
                if fn in l and p in l:
                    print("\t\t\t\t\t Congrats your Record founded here")
                    flag=1
                    mycursor.execute("delete from Admission where (FormNo=%s and ContactNo=%s)",(fn,p))
                    mydb.commit()
                    print("\n\t\t\t\tDELETING......")
                    print("\t\t\t\t\t Congrats your Record DELETED. ")                        
                if flag==0:
                    sys.stderr.write("\n\t\t\t\tSorry no such record founds !\n\n")
            elif ch==3:
                n=input("\n\t\t\t\tEnter your Name:")
                p=input("\t\t\t\tEnter Phone No.:")
                mycursor.execute("select* from Admission where (Name=%s and ContactNo=%s)",(n,p))
                l=list(mycursor.fetchone())
                flag=0
                if n in l and p in l:
                    print("\t\t\t\t\t Congrats your Record founded here")
                    flag=1
                    mycursor.execute("delete from Admission where (Name=%s and ContactNo=%s)",(n,p))
                    mydb.commit()
                    print("\n\t\t\t\tDELETING......")
                    print("\t\t\t\t\t Congrats your Record DELETED. ")       
                if flag==0:
                    sys.stderr.write("\n\t\t\t\tSorry no such record founds !\n\n")
            else:
                break
    except:
        sys.stderr.write("\n\t\t\t\tSorry no such record founds !\n\n")
        
def Delete_Details1():
    try:
        ch1=int(input('''\t\t\t\t !!!!WELCOME TO DELETE SECTION !!!!
                         1:Delete all records. \n
                         2:Delete particular records.\n
                          Your's Choice :-'''))
        if ch1==1:
            cnfm=input('''\t\t\t\tAre you sure, Do you want to delete all the records \n
                            press y to continue :-''')
            if cnfm=='y':
                mycursor.execute("delete  from Admission ")
                mydb.commit()
                print("\n\t\t\t\tDELETING......")
                print("\n\t\t\t\tYour all Records has been Deleted\n")
            else:
                print("\n\t\t\t\tThanks! Records are not deleted")
        elif ch1==2:
            Delete_Details()
        else:
            sys.stderr.write('\n\t\t\t\tSorry! Invalid Option \n\n')
                            
    except:
        sys.stderr.write("\n\t\t\t\tSorry no such record founds !\n\n")
                    
