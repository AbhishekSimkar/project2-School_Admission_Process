print('''


                              K          K            V                 V               S
                              K        K               V               V             S    S
                              K      K                  V             V            S
                              K    K                     V           V            s
                              K  K                        V         V             S
                              K                            V       V                S
                              K  K                          V     V                   s s    
                              K    K                         V   V                        s  
                              K      K                        V V                          s  
                              K        K                       V                  s       s 
                              K          K                                          s  s s
        =============================================================================================\n


                           ==================================================================
                              ***************WELCOME TO KVS ADMISSION SYSTEM***************
                           ==================================================================

''')

while True:
    print('''
                                -------------------------------------------------------
                                       *******KENDRIYA VIDYALAYA SANGATHAN*******
                                -------------------------------------------------------\n\n\n''')
    print('''
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                           *******WELCOME TO MAIN MENU*******
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n''')
    
    break

'''Main Program'''

import sys
import KVSpackage.Lottery as l
import KVSpackage.Visualization as v
import KVSpackage.Delete as d
import KVSpackage.Update as u
import KVSpackage.Search as s
import KVSpackage.Sel_Stud as ss
import KVSpackage.Admission as a

while True:
    ch=int(input('''\n\n\t\t\t Enter your profile\n
                 \t\t\t 1:  Continue As Administrater\n 
                 \t\t\t 2:  Continue As Normal user \n
                 \t\t Choice :- '''))
    if ch==1:
        pswd=input('''\t\t\t
                        \t\t !!!! WELCOME TO AdMIN SECTION !!!!\n
                        Enter Your Admin Pascode  :-''')
        if pswd=='1234':
            while True:
                ch1=int(input(''' \t\t\t
                            1: Lottery Conduction \n
                            2: Deletion of records \n
                            3: Search Bar  \n
                            4: Update a record \n
                            5: Visualization Section \n
                            6: Exit

                                     Enter Choice :-'''))
                if ch1==1:
                    l.lottery()
                elif ch1==2:
                    d.Delete_Details()
                elif ch1==3:
                    s.SEARCH_Details1()
                elif ch1==4:
                    u.Update_Details()
                elif ch1==5:
                    while True:
                        print('''\n\t\t\t\t !!WELCOME TO VISUALISATION CORNER!! \n
                                    1: Date v/s No.of Form plot. \n
                                    2: Gender v/s No.of Form plot. \n
                                    3: Age v/s No.of Form plot. \n
                                    4: Castcatagory v/s No.of Form plot.\n
                                    5: service catagory v/s No.of Form plot. \n
                                    6: exit.''')
                        ch2=int(input("\t\t\t\t Enter your choice :"))
                        if ch2==1:
                            v.date_plot()
                        elif ch2==2:
                            v.Gender_plot()
                        elif ch2==3:
                            v.Age_plot()
                        elif ch2==4:
                            v.c_category_plot()
                        elif ch2==5:
                            v.s_category_plot()
                        else:
                            break
                elif ch1==6:
                    break
                else:
                    sys.stderr.write('\n\t\t\tINVALID OPTIONS ,Try Again')     
        else:
            sys.stderr.write('\n\t\t\tSorry! Password is incorrect ,Try Again')
    elif ch==2:
        while True:
            print("\n\t\t\t\t\t!!!WELCOME TO USER SECTION!!! ")
            ch1=int(input('''\t\t\t
                          1:Register for Admission \n
                          2:deletion of records \n
                          3:search for a records \n
                          4:update a record \n
                          5:Visualization \n
                          6:View list of Selected_Student \n
                          7:Exit \n

                                  Enter Your Choice :- '''))
            if ch1==1:
                a.Add_Details()
            elif ch1==2:
                d.Delete_Details1()
            elif ch1==3:
                s.Search_Details()
            elif ch1==4:
                u.Update_Details()
            elif ch1==5:
                while True:
                    print('''\n\t\t\t\t !!WELCOME TO VISUALISATION CORNER!! \n
                                    1: Date v/s No.of Form plot. \n
                                    2: Gender v/s No.of Form plot. \n
                                    3: Age v/s No.of Form plot. \n
                                    4: Castcatagory v/s No.of Form plot.\n
                                    5: service catagory v/s No.of Form plot. \n
                                    6: exit.''')
                    ch2=int(input("\t\t\t\t Enter your choice :"))
                    if ch2==1:
                        v.date_plot()
                    elif ch2==2:
                        v.Gender_plot()
                    elif ch2==3:
                        v.Age_plot()
                    elif ch2==4:
                        v.c_category_plot()
                    elif ch2==5:
                        v.s_category_plot()
                    else:
                        break
            elif ch1==6:
                ss.sel_stud()
            elif ch1==7:
                break
            else:
                sys.stderr.write('\n\t\t\tINVALID OPTIONS ,Try Again')
    else:
        print("\t\t\t\t !!THANKYOU FOR VISITING OUR SITE!!")



      
