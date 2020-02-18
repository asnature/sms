from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Check")
root.geometry("1530x830+0+0")
root.configure(bg="lime")
root.propagate(0)

l1 = Label(root, text="Welcome To the School Management System Online Portal",bg="yellow",font="comicsans 15 italic",fg="red").pack(fill = X)
global temp_value3


#-----------------frame for the status bar and website info----------------

statusbar = StringVar()
statusbar.set("This portal is designed using python only")
sbar = Label(root, textvariable=statusbar, relief=SUNKEN, bg="purple",fg="white").pack(side=BOTTOM,fill=X)





# ---------------Background frame------------------
# ---------------Registration Frame-----------------------
Left_frame = Frame(root, bd=5, relief=GROOVE, bg="green")
Left_frame.place(x=35, y=205, width=700, height=600)

# ----------------Check detail frame______________________
Right_frame = Frame(root, bd=5, relief=SUNKEN, bg="green")
Right_frame.place(x=810, y=205, width=700, height=607)

# -------------left Frame for title in registration frame---------------
Left_Registration_frame_title = Frame(root, bd=1, relief=RIDGE, bg="red")
Left_Registration_frame_title.place(x=85, y=155, width=600, height=50)

# -------------right Frame for title in check detais frame---------------
Right_Registration_frame_title = Frame(root, bd=1, relief=RIDGE, bg="red")
Right_Registration_frame_title.place(x=870, y=145, width=600, height=57)

##----------Frame for the dialog box-----------

Left_Diag_frame = Frame(Left_frame,bd=3,relief=RIDGE,bg="yellow")
Left_Diag_frame.place(x=50,y=380, width=600, height=57)
##--------------Frame---------------------------------
Right_Diag_frame = Frame(Right_frame,bd=3,relief=RIDGE,bg="yellow")
Right_Diag_frame.place(x=50,y=380, width=600, height=57)


title1 = Label(Left_Registration_frame_title, text="TEACHER REGISTRATION", bg="red", fg="white",font="comicsans 30 bold", padx=50).grid(row=0, column=0)

title2 = Label(Right_Registration_frame_title, text="STUDENT REGISTRATION", bg="red", fg="white",font="comicsans 30 bold", padx=50).grid(row=0, column=0)

#------------------MAIN PROGRAMME--------------------------------

n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()
n5=StringVar()
n6=StringVar()
n11=StringVar()
n12=StringVar()
n13=StringVar()

def Teacher_button():
    t1=n1.get()
    t2=n2.get()
    t3=n3.get()
    t4=n4.get()
    t5=n5.get()
    t6=n6.get()
    t11=n11.get()
    t12=n12.get()
    t13=n13.get()

    temp_value2=open("admission_number.txt","r")
    temp_value4=temp_value2.read(1)
    temp_value2.close()
    temp_value2=open("admission_number.txt","w")
    temp_value4=int(temp_value4)
    temp_value3=temp_value4
    temp_value4=temp_value4+1
    temp_value4=str(temp_value4)
    temp_value2.write(temp_value4)
    temp_value2.close()



    temp_value1=str(temp_value3)
    full_file_name=temp_value1+".txt"
    student_record=open(full_file_name,"x")
    student_record.close()
    student_record=open(full_file_name,"a")
    student_record.write("First Name: "+t1)
    student_record.write("\nLast Name: "+t2)
    student_record.write("\nMobile Name: "+t3)
    student_record.write("\n /EmailId: "+t4)
    student_record.write("\nDateofBirth: "+t5)
    student_record.write("\nSpecialisation: "+t6)
    student_record.write("\nGender: "+t11)
    student_record.write("\nAddress: "+t12)
    student_record.write("\nQualification: "+t13)
    student_record.close()
    print("Admission Number is",(temp_value3))
    admission_number = Label(Left_Diag_frame, text="Unique Id Generated Is :"+str(temp_value3),fg='red',bg="yellow",font="comicsans 20 bold").grid(padx =25,pady=5)


Firstname = Label(Left_frame, text="First Name  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=0, column=0, pady=5, sticky="w")
txtfirstname = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n1).grid(row=0,column=1, padx=20,sticky="w")

Lastname = Label(Left_frame, text="Last Name  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=1, column=0, sticky="w")
txtlastname = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n2).grid(row=1,column=1, padx=20,pady=5,sticky="w")

Mobileno = Label(Left_frame, text="Mbile No.  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=2, column=0, sticky="w")
txtmobile = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n3).grid(row=2, column=1, padx=20,pady=5,sticky="w")

Email = Label(Left_frame, text="Email Id.  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=3,column=0, sticky="w")
txtemail = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n4).grid(row=3, column=1, padx=20,pady=5,sticky="w")

Dateofbirth = Label(Left_frame, text="D. O. B.  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=4, column=0, sticky="w")
txtdateofbirth = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n5).grid(row=4, column=1,padx=20,pady=5,sticky="w")

Specialisation = Label(Left_frame, text="Specialisation  :", bg="green", fg="white",font="comicsans 15 bold").grid(row=5, column=0, sticky="w")
txtspecialisation = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n6).grid(row=5, column=1,padx=20, pady=5,sticky="w")

Gender = Label(Left_frame, text="Gender  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=6, column=0, sticky="w")
Dropdown_gender = ttk.Combobox(Left_frame, font="comicsans 14 bold", state="readonly",textvariable=n11)
Dropdown_gender['values'] = ("male", "female", "other")
Dropdown_gender.grid(row=6, column=1, pady=5)

adress = Label(Left_frame, text="Address  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=1,column=2, sticky="w")
txtadress = Entry(Left_frame,textvariable=n12,relief=SUNKEN,bd=5).grid(row=2, column=2, sticky="w")

qualification = Label(Left_frame, text="Qualifications:", bg="green", fg="white",font="comicsans 17 bold bold").grid(row=4, column=2, sticky="w")
txtqualification1 = Entry(Left_frame,textvariable=n13,relief=SUNKEN,bd=5).grid(row=5, column=2, sticky="w")




n7= StringVar()
admission = Label(root, text="uniqueID  :", bg="green", fg="white",
font="comicsans 17 bold").place(x=10,y=100)
txtadmissiion = Entry(root, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n7).place(x=150,y=100)



global t8




b11=Button(Left_frame,text="Click",bg='blue',command=Teacher_button,padx = 100,pady=20)
b11.place(x=150,y=450)

###############################################################








def button1():
        root1=Tk()
        root1.geometry('1200x800')
        frame12=Frame(root1,height=800,width=1200,bg='green').pack()
        t7 = n7.get()
        t8=t7+".txt"
        #t9=t8+".txt"
        t10 = open(t8,'r')
        t20 = t10.read()
        #t20.close()
        label1 = Label(root1,text=t20).place(x=800,y=50)
        root1.mainloop()
b12=Button(root,text="Click",bg='blue',command=button1,padx = 30,pady=5)
b12.place(x=400,y=100)

########TIME TABLE ################################

def take_value1():
    root1 = Tk()
    root1.geometry("1280x720")
    root1.title("Time Table")

    def take_value():
        t1_timetable = n2_timetable.get()
        t2_timetable = n3_timetable.get()
        t3_timetable = n4_timetable.get()
        t4_timetable = n5_timetable.get()
        t5_timetable = n6_timetable.get()
        t6_timetable = n7_timetable.get()
        t7_timetable = n8_timetable.get()
        t8_timetable = n9_timetable.get()
        t9_timetable = n10_timetable.get()

        t11_timetable = "Class " + t9_timetable + ".txt"
        t10_timetable = open(t11_timetable, 'x')
        t10_timetable.write("Period 1 " + t1_timetable)
        t10_timetable.write("\nPeriod 2 " + t2_timetable)
        t10_timetable.write("\nPeriod 3 " + t3_timetable)
        t10_timetable.write("\nPeriod 4 " + t4_timetable)
        t10_timetable.write("\nPeriod 5 " + t5_timetable)
        t10_timetable.write("\nPeriod 6 " + t6_timetable)
        t10_timetable.write("\nPeriod 7 " + t7_timetable)
        t10_timetable.write("\nPeriod 8 " + t8_timetable)
        t10_timetable.close()

        l2_timetable = Label(root1,text=t1_timetable + t2_timetable + t3_timetable + t4_timetable + t5_timetable + t6_timetable + t7_timetable + t8_timetable).place(x=600, y=60)

    ##################################################################
    n2_timetable = StringVar()
    n3_timetable = StringVar()
    n4_timetable = StringVar()
    n5_timetable = StringVar()
    n6_timetable = StringVar()
    n7_timetable = StringVar()
    n8_timetable = StringVar()
    n9_timetable = StringVar()
    n10_timetable = StringVar()

    ##########################################################################
    f1_timetable = Frame(root1, height=720, width=1280, bg="red").pack()

    l1_timetable = Label(root1, text="Enter Class", font=(20)).place(x=150, y=30)
    e1_timetable = Entry(root1, width=25, bd=5, textvariable=n10_timetable).place(x=300, y=30)
    b1_timetable = Button(root1, width=15, height=3, text="Submit", bg='green', command=take_value).place(x=450, y=600)

    l2_timetable = Label(root1, text="Period 1", font=(20)).place(x=150, y=90)
    s2_timetable = Spinbox(root1, values=(
    "English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), font=('Arial,12'),
                           textvariable=n2_timetable).place(x=300, y=90)

    l3_timetable = Label(root1, text="Period 2", font=(20)).place(x=150, y=150)
    s3_timetable = Spinbox(root1, values=(
    "English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), font=('Arial,12'),
                           textvariable=n3_timetable).place(x=300, y=150)

    l4_timetable = Label(root1, text="Period 3", font=(20)).place(x=150, y=210)
    s4_timetable = Spinbox(root1, values=(
    "English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), font=('Arial,12'),
                           textvariable=n4_timetable).place(x=300, y=210)

    l5_timetable = Label(root1, text="Period 4", font=(20)).place(x=150, y=270)
    s5_timetable = Spinbox(root1, values=(
    "English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), font=('Arial,12'),
                           textvariable=n5_timetable).place(x=300, y=270)

    l6_timetable = Label(root1, text="Period 5", font=(20)).place(x=150, y=330)
    s6_timetable = Spinbox(root1, values=(
    "English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), font=('Arial,12'),
                           textvariable=n6_timetable).place(x=300, y=330)

    l7_timetable = Label(root1, text="Period 6", font=(20)).place(x=150, y=390)
    s7_timetable = Spinbox(root1, values=(
    "English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), font=('Arial,12'),
                           textvariable=n7_timetable).place(x=300, y=390)

    l8_timetable = Label(root1, text="Period 7", font=(20)).place(x=150, y=450)
    s8_timetable = Spinbox(root1, values=(
    "English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), font=('Arial,12'),
                           textvariable=n8_timetable).place(x=300, y=450)

    l9_timetable = Label(root1, text="Period 8", font=(20)).place(x=150, y=510)
    s9_timetable = Spinbox(root1, values=(
    "English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), font=('Arial,12'),
                           textvariable=n9_timetable).place(x=300, y=510)

    root1.mainloop()





b13=Button(root,text="Manage Time Table",bg='blue',padx = 100,pady=20,command=take_value1)
b13.place(x=600,y=60)










#################################
############################
###########################################################
#######################################################################3
##################################################################################3
#####################################################################################3



#------------------MAIN PROGRAMME--------------------------------

a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()
a5=StringVar()
a6=StringVar()
a11=StringVar()
a12=StringVar()
a13=StringVar()

def Student_button():
    b1=a1.get()
    b2=a2.get()
    b3=a3.get()
    b4=a4.get()
    b5=a5.get()
    b6=a6.get()
    b11=a11.get()
    b12=a12.get()
    b13=a13.get()


    temp_value2=open("regg_number.txt","r")
    temp_value4=temp_value2.read(1)
    temp_value2.close()
    temp_value2=open("regg_number.txt","w")
    temp_value4=int(temp_value4)
    temp_value3=temp_value4
    temp_value4=temp_value4+1
    temp_value4=str(temp_value4)
    temp_value2.write(temp_value4)
    temp_value2.close()



    temp_value1=str(temp_value3)
    full_file_name=temp_value1+".txt"
    student_record=open(full_file_name,"x")
    student_record.close()
    student_record=open(full_file_name,"a")
    student_record.write("First Name: "+b1)
    student_record.write("\nSecond Name: "+b2)
    student_record.write("\nSecond Name: "+b3)
    student_record.write("\nSecond Name: "+b4)
    student_record.write("\nSecond Name: "+b5)
    student_record.write("\nSecond Name: "+b6)
    student_record.write("\nSecond Name: "+b11)
    student_record.write("\nSecond Name: "+b12)
    student_record.write("\nSecond Name: "+b13)
    student_record.close()
    print("Admission Number is",(temp_value3))
    admission_number = Label(Right_Diag_frame, text="Unique Id Generated Is :"+str(temp_value3),fg='red',bg="yellow",font="comicsans 20 bold").grid(padx =25,pady=5)



Firstname = Label(Right_frame, text="First Name  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=0, column=0, pady=5, sticky="w")
txtfirstname = Entry(Right_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=a1).grid(row=0,column=1, padx=20,sticky="w")

Lastname = Label(Right_frame, text="Last Name  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=1, column=0, sticky="w")
txtlastname = Entry(Right_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=a2).grid(row=1,column=1, padx=20,pady=5,sticky="w")

Mobileno = Label(Right_frame, text="Mbile No.  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=2, column=0, sticky="w")
txtmobile = Entry(Right_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=a3).grid(row=2, column=1, padx=20,pady=5,sticky="w")

Email = Label(Right_frame, text="Email Id.  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=3,column=0, sticky="w")
txtemail = Entry(Right_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=a4).grid(row=3, column=1, padx=20,pady=5,sticky="w")

Dateofbirth = Label(Right_frame, text="D. O. B.  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=4, column=0, sticky="w")
txtdateofbirth = Entry(Right_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=a5).grid(row=4, column=1,padx=20,pady=5,sticky="w")

Specialisation = Label(Right_frame, text="Specialisation  :", bg="green", fg="white",font="comicsans 15 bold").grid(row=5, column=0, sticky="w")
txtspecialisation = Entry(Right_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=a6).grid(row=5, column=1,padx=20, pady=5,sticky="w")

Gender = Label(Right_frame, text="Gender  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=6, column=0, sticky="w")
Dropdown_gender = ttk.Combobox(Right_frame, font="comicsans 14 bold", state="readonly")
Dropdown_gender['values'] = ("male", "female", "other")
Dropdown_gender.grid(row=6, column=1, pady=5)

Gender = Label(Right_frame, text="Gender  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=6, column=0, sticky="w")
Dropdown_gender = ttk.Combobox(Right_frame, font="comicsans 14 bold", state="readonly",textvariable=a11)
Dropdown_gender['values'] = ("male", "female", "other")
Dropdown_gender.grid(row=6, column=1, pady=5)

adress = Label(Right_frame, text="Address  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=1,column=2, sticky="w")
txtadress = Entry(Right_frame,textvariable=a12,relief=SUNKEN,bd=5).grid(row=2, column=2, sticky="w")

qualification = Label(Right_frame, text="Qualifications:", bg="green", fg="white",font="comicsans 17 bold bold").grid(row=4, column=2, sticky="w")
txtqualification1 = Entry(Right_frame,textvariable=a13,relief=SUNKEN,bd=5).grid(row=5, column=2, sticky="w")


b12=Button(Right_frame,text="Click",bg='blue',command=Student_button,padx = 100,pady=20)
b12.place(x=150,y=450)


root.mainloop()

