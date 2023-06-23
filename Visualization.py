import csv
import matplotlib.pyplot as plt
import mysql.connector as con
mydb=con.connect(host='localhost',user='root',password='1234',database='KVSadm')
mycursor=mydb.cursor()

def date_plot():
    file=open("C:/Users/hp/Desktop/F vs D.csv",'r')
    read=list(csv.reader(file))
    l=[]
    for i in read[1:]:
        l.append(i[-1])
    d={}
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    count=list(d.keys())
    date=list(d.values())
    plt.bar(count,date,color=['k','r','b','m'])
    plt.xlabel('Date')
    plt.ylabel('Count of Form Submitted')
    plt.title('Date v/s Count of Form')
    plt.xticks(date,rotation=90)
    plt.show()

def s_category_plot():
    l=[]
    for i in range(0,6):
        mycursor.execute("select count(ServiceCategory) from Admission where ServiceCategory=%s",(i,))
        RTE=mycursor.fetchone()
        for i in RTE:
            l.append(i)
    ax=plt.axes()
    l1=['RTE','CAT1','CAT2','CAT3','CAT4','CAT5']
    plt.bar(l1,l,color=["k",'b','g','m','r','y'])
    plt.xlabel(' NO. of form submitted')
    plt.ylabel(' service category ')
    plt.title('Student details Vs service category')
    ax.set_facecolor('grey')
    plt.show()

def Age_plot():
    g=[5,6,7]
    A=[]
    for i in g:
        mycursor.execute("select count(Age) from Admission where Age=%s",(i,))
        l=mycursor.fetchone()
        for i in l:
            A.append(i)
    Age=["Age5","Age6","Age7"]
    plt.bar(Age,A,color=['m','g','k'])
    plt.title("AGE GRAPH")
    plt.show()

def Gender_plot():
    mycursor.execute("select count(Gender) from Admission where Gender='m'")
    l=mycursor.fetchone()
    gender=[]
    for i in l:
        gender.append(i)
        
    mycursor.execute("select count(Gender) from Admission where Gender='f'")
    l=mycursor.fetchone()
    for i in l:
        gender.append(i)
    
    gen=["Male","Female"]
    plt.bar(gen,gender,color=["g","m"])
    plt.title("MALE VS FEMALE GRAPH")
    plt.show()

def c_category_plot():
    Cast=[]
    g=['general','obc','sc','st','other']
    for i in g:
        mycursor.execute("select count(Castcategory) from Admission where Castcategory=%s",(i,))
        C=mycursor.fetchone()
        for i in C:
            Cast.append(i)
    ax=plt.axes()
    l1=['GEN','OBC','SC','ST','OTHER']
    plt.bar(l1,Cast,color=["k",'b','g','m','r'])
    plt.xlabel(' NO.of form submitted')
    plt.ylabel(' Castcategory ')
    plt.title('Student details Vs Castcategory')
    ax.set_facecolor('blue')
    plt.show()


