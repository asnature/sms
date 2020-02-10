from tkinter import *
root = Tk()
root.geometry("1530x830+0+0")
root.configure(bg="blue")
root.title("-------School Management System--------")

#---------------------Title for the main portal------------------


title = Label(root, text="School Management System",font="comicsans 20 bold",bg="#00ff00",fg="blue",relief=SUNKEN,bd=10).pack(side=TOP,fill=X)

f1 = Frame(root, bg="yellow",bd=10,relief=GROOVE)
f1.pack(fill=X)

l1 = Label(f1, text="Welcome To the School Management System Online Portal",bg="yellow",font="comicsans 15 italic",fg="red").pack()

#---------------Introduction text---------------------

text_label = Label(root, text="This portal contains the record for the  student and teachers boths.\n This portal also updates the information of the student and the teacher as per requirement.\n Furthure the feature of the website will be updated as soon as possible.",bg="blue",font="comicsans 15 italic", fg="pink", pady=50).pack()

#-----------------frame for the status bar and website info----------------

statusbar = StringVar()
statusbar.set("This portal is designed using python only")
sbar = Label(root, textvariable=statusbar, relief=SUNKEN, bg="purple",fg="white").pack(side=BOTTOM,fill=X)


# ---------------------This is the button for the student portal------------

def student():
    print("this is the student record")
b1 = Button(root, fg="red", text="Student Portal",bg="green",padx=100,pady=20,command=student).pack(side=LEFT,padx=400,pady=200)



# --------------------This is the button for the Teachers portal---------------



def teacher():
    print("this is teacher record portal")
    #teacher_root = Tk()
    #teacher_root.geometry("500x500")
    #teacher_root.configure(bg="#7B68EE")








    #-----------------Status bar for the teachers portal--------------------------
    #statusbar1 = StringVar()
    #statusbar1.set("This is the Teacher's Record Management Portal")
    #sbar1 = Label(teacher_root, textvariable=statusbar1, relief=SUNKEN, bg="red", fg="black",bd=5).pack(    side=BOTTOM, fill=X)'''

    #-------------Title for the teacher portal---------------------
    #title = Label(teacher_root, text="Teacher's Record Management Portal", font="comicsans 15 bold", bg="#00ff00", relief=RIDGE, pady=15).pack(side=TOP, fill=X)

    #--------------Mandetory information for the information input------------------
    #title_label = Label(teacher_root, text="Welcome to the teacher information login/access portal,\n fill     all the mandetory details correctly.\n Feilds marked with (*) are mandetory to fill.", bg="#7B68EE"        ,font="comicsans 20 italic", fg="red").pack()

    #firstname = Label(teacher_root, text="firstname").grid()
    #lastname = Label(teacher_root, text="lastname").grid(row=2)

    #firstvalue = StringVar()
    #lastvalue = StringVar()
    #firstentry = Entry(teacher_root, textvariable=firstvalue).grid(row=0, column=1)
    #lastentry = Entry(teacher_root, textvariable=lastvalue).grid(row=2, column=1)




    #teacher_root.mainloop()

    from tkinter import ttk
    class student:
        def __init__(self, root):
            self.root = root
            self.root.title("teacher record")
            self.root.geometry("500x400+0+0")

            title = Label(self.root, text="Teacher record managemnt", font="comicsans 20 bold",                       bg="yellow", fg="red",pady=15, bd=5).pack(side=TOP, fill=X)

    ##**==**==**==**==**==**==**==**==**==**""FRAMES""**==**==**==**==**==**==**==**==**==**==**==**==**==

        # ---------------Background frame------------------
            Main_frame = Frame(self.root, bd=10, relief=SUNKEN, bg="#7b68ee")
            Main_frame.place(x=20, y=90, width=1500, height=730)

        # -----------------Division frame------------------
            Division_frame = Frame(self.root, bd=0, relief=RIDGE, bg="lime")
            Division_frame.place(x=770, y=210, width=10, height=600)

            # ---------------Registration Frame-----------------------
            Left_frame = Frame(self.root, bd=5, relief=GROOVE, bg="green")
            Left_frame.place(x=35, y=205, width=700, height=600)

            # ----------------Check detail frame______________________
            Right_frame = Frame(self.root, bd=5, relief=SUNKEN, bg="green")
            Right_frame.place(x=810, y=205, width=700, height=607)

        # --==--==--==--==--==--==--==--==""Frame for the Titles""--==--==--==--==--==--==--==--==--==--==--

            # -------------left Frame for title in registration frame---------------
            Left_Registration_frame_title = Frame(self.root, bd=1, relief=RIDGE, bg="red")
            Left_Registration_frame_title.place(x=85, y=211, width=600, height=50)

            # -------------right Frame for title in check detais frame---------------
            Right_Registration_frame_title = Frame(self.root, bd=1, relief=RIDGE, bg="red")
            Right_Registration_frame_title.place(x=870, y=211, width=600, height=57)

            # ---------------Detail for registration frame---------------
            Registration_frame1 = Frame(self.root, bd=0, relief=RIDGE, bg="green")
            Registration_frame1.place(x=35, y=280, width=700, height=530)

            # -----------Frame for the Button---------------------

            buttonframe = Frame(Registration_frame1, bd=0, relief=GROOVE, bg="green")
            buttonframe.place(x=0, y=420, width=700, height=85)

        # ====================Titels-------------------------------------

            title = Label(Main_frame,text="Welcome to the teacher access/login management system,\n Fill              all the mondatery details correctly.\n The field marked with (*) are mondatory.",bg="#7b68ee",            font="comicsans 20 italic", fg="red").pack()
            title1 = Label(Left_Registration_frame_title, text="REGISTRATION FORM", bg="red", fg="white",
            font="comicsans 30 bold", padx=100).grid(row=0, column=0)
            title2 = Label(Right_Registration_frame_title, text="CHECK DETAIL", bg="red", fg="white",
            font="comicsans 30 bold", padx=140).grid(row=0, column=0)

        # =======================Entry Headings===========================

            Firstname = Label(Registration_frame1, text="First Name  :", bg="green", fg="white",
            font="comicsans 17 bold").grid(row=0, column=0, pady=5, sticky="w")
            txtfirstname = Entry(Registration_frame1, font="comicsans 15 bold", bd=5, relief=GROOVE).grid(            row=0,column=1,padx=20,sticky="w")

            Lastname = Label(Registration_frame1, text="Last Name  :", bg="green", fg="white",
            font="comicsans 17 bold").grid(row=1, column=0, sticky="w")
            txtlastname = Entry(Registration_frame1, font="comicsans 15 bold", bd=5, relief=GROOVE).grid(             row=1,column=1,padx=20,pady=5,sticky="w")

            Mobileno = Label(Registration_frame1, text="Mbile No.  :", bg="green", fg="white",
            font="comicsans 17 bold").grid(row=2, column=0, sticky="w")
            txtmobile = Entry(Registration_frame1, font="comicsans 15 bold", bd=5, relief=GROOVE).grid(               row=2, column=1,padx=20, pady=5,sticky="w")

            Email = Label(Registration_frame1, text="Email Id.  :", bg="green", fg="white",
            font="comicsans 17 bold").grid(row=3, column=0, sticky="w")
            txtemail = Entry(Registration_frame1, font="comicsans 15 bold", bd=5, relief=GROOVE).grid(                row=3, column=1,padx=20, pady=5,sticky="w")

            Dateofbirth = Label(Registration_frame1, text="D. O. B.  :", bg="green", fg="white",
            font="comicsans 17 bold").grid(row=4, column=0, sticky="w")
            txtqualification = Entry(Registration_frame1, font="comicsans 15 bold", bd=5,                             relief=GROOVE).grid(row=4,column=1,padx=20,pady=5,sticky="w")

            Specialisation = Label(Registration_frame1, text="Specialisation  :", bg="green", fg="white",
            font="comicsans 15 bold").grid(row=5, column=0, sticky="w")
            txtspecialisation = Entry(Registration_frame1, font="comicsans 15 bold", bd=5,                            relief=GROOVE).grid(row=5,column=1,padx=20,pady=5,sticky="w")

            Gender = Label(Registration_frame1, text="Gender  :", bg="green", fg="white",
            font="comicsans 17 bold").grid(row=6, column=0, sticky="w")
            Dropdown_gender = ttk.Combobox(Registration_frame1, font="comicsans 14 bold", state="readonly")
            Dropdown_gender['values'] = ("male", "female", "other")
            Dropdown_gender.grid(row=6, column=1, pady=5)

            adress = Label(Registration_frame1, text="Adress  :", bg="green", fg="white",
            font="comicsans 17 bold").grid(row=1, column=2, sticky="w")
            txtadress = Text(Registration_frame1, width=19, height=4).grid(row=1, column=3, sticky="w")

            qualification = Label(Registration_frame1, text="Qualifications  :", bg="green", fg="white",
            font="comicsans 10 bold").grid(row=4, column=2, sticky="w")
            txtqualification = Text(Registration_frame1, width=19, height=4).grid(row=4, column=3,                    sticky="w")

        # +++++++++++++++++++++++Buttons for filled entry++++++++++++++++++++++

            def Submitt():
                print("all the information is submitted")

            def Clear():
                print("all the above entry is cleared")


            btn = Button(buttonframe, text="SUBMITT", width=20, height=3, bg="blue", fg="white",                      command=Submitt).grid(row=0, column=1,padx=89, pady=12)
            btn1 = Button(buttonframe, text="CLEAR", width=20, height=3, bg="blue", fg="white",                       command=Clear).grid(row=0,           column=2,padx=89, pady=12)

    root = Tk()
    ob = student(root)
    root.mainloop()


b2 = Button(root,fg="red", text="Teacher Portal",bg="green",padx=100,pady=20,command=teacher).pack(side=LEFT)





root.mainloop()