from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from PIL import Image,ImageTk
import mysql.connector
import cv2
import re
class Student():
    def __init__(self,root):
         self.root= root
         self.root.geometry("1535x835+0+0")
         self.root.title("Student Management System")
         self.root.iconbitmap("./attendese\pictures\icon.ico")
#=============variables============
         self.var_dep=StringVar()
         self.var_course=StringVar()
         self.var_year=StringVar()
         self.var_sem=StringVar()
         self.var_id=StringVar()
         self.var_name=StringVar()
         self.var_roll=StringVar()
         self.var_div=StringVar()
         self.var_gender=StringVar()
         self.var_dob=StringVar()
         self.var_email=StringVar()
         self.var_phone=StringVar()
         self.var_address=StringVar()
         self.var_teacher=StringVar()
         self.var_search_type=StringVar() 
         self.var_roll_search=StringVar()
         #-----------------------Top bar-------------------------------------------------------------

        #  #first image
         img=Image.open(r"attendese\pictures\sd1.jpeg")
         img=img.resize((550,130),Image.ANTIALIAS)
         self.photoimg=ImageTk.PhotoImage(img)
         f_lbl=Label(self.root,image=self.photoimg)
         f_lbl.place(x=0,y=0,width=550,height=130)

        #  #2nd image
         img1=Image.open(r"attendese\pictures\sd2.jpeg")
         img1=img1.resize((500,130),Image.ANTIALIAS)
         self.photoimg1=ImageTk.PhotoImage(img1)
         f_lbl1=Label(self.root,image=self.photoimg1)
         f_lbl1.place(x=550,y=0,width=500,height=130)

         #3rd image
         img2=Image.open(r"attendese\pictures\sd3.jpeg")
         img2=img2.resize((550,130),Image.ANTIALIAS)
         self.photoimg2=ImageTk.PhotoImage(img2)
         f_lbl2=Label(self.root,image=self.photoimg2)
         f_lbl2.place(x=1050,y=0,width=550,height=130)
                #------------------------------------------Title--------------------------------------------------------------------
         title=Label(self.root,text="Student Management System",font=("Rockwell Condensed",25,"bold"),bg="#ace5ee",fg="red")
         title.place(x=0,y=130,width=1530,height=60)
         #-------------------Frame----------------------
         main_frame=Frame(self.root,bd=10,bg="white")
         main_frame.place(x=0,y=190,width=1730,height=790)
        #-----------------left frame----------------------
         left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,font=("times new roman",15,"bold"),text="Student Details",bg="white")
         left_frame.place(x=10,y=10,width=720,height=620)

         #-------------image on top-----------
         img4=Image.open(r"attendese\pictures\stu.jpeg")
         img4=img4.resize((700,130),Image.ANTIALIAS)
         self.photoimg4=ImageTk.PhotoImage(img4)
         f_lbl4=Label(left_frame,image=self.photoimg4)
         f_lbl4.place(x=10,y=5,width=700,height=130)

#----------------------Current Course Information-----------------------
         cc_frame=LabelFrame(left_frame,bd=5,relief=RIDGE,font=("times new roman",15,"bold"),text="Current Course Information",bg="white")
         cc_frame.place(x=10,y=140,width=690,height=130)
         
         #department
         dep_lbl=Label(cc_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
         dep_lbl.grid(row=0,column=0,padx=10)
         dep_cb=ttk.Combobox(cc_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",background="white")
         dep_cb["values"]=("Select Department","CSE","ECE","ME","CE")
         dep_cb.current(0)
         dep_cb.grid(row=0,column=1,padx=5,pady=10,sticky=W)

         #course
         course_lbl=Label(cc_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
         course_lbl.grid(row=0,column=2,padx=10)
         course_cb=ttk.Combobox(cc_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",background="white")
         course_cb["values"]=("Select Course","Btech","Diploma")
         course_cb.current(0)
         course_cb.grid(row=0,column=3,padx=5,pady=10,sticky=W)

                 #year
         dep_lbl=Label(cc_frame,text="Session",font=("times new roman",12,"bold"),bg="white")
         dep_lbl.grid(row=1,column=0,padx=10)
         dep_cb=ttk.Combobox(cc_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",background="white")
         dep_cb["values"]=("Select session","2020-2021","2021-2022","2022-2023","2023-2024")
         dep_cb.current(0)
         dep_cb.grid(row=1,column=1,padx=5,pady=10,sticky=W)

         #semester
         course_lbl=Label(cc_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
         course_lbl.grid(row=1,column=2,padx=10)
         course_cb=ttk.Combobox(cc_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",background="white")
         course_cb["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
         course_cb.current(0)
         course_cb.grid(row=1,column=3,padx=5,pady=10,sticky=W)
#----------------------Student information-----------------------
         cs_frame=LabelFrame(left_frame,bd=5,relief=RIDGE,font=("times new roman",15,"bold"),text="Class Student Information",bg="white")
         cs_frame.place(x=10,y=280,width=690,height=295)
            #Studetn ID no
         stID_lbl=Label(cs_frame,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
         stID_lbl.grid(row=0,column=0,padx=10)
         stdID_ip=ttk.Entry(cs_frame,textvariable=self.var_id,width=15,font=("times new roman",15))
         stdID_ip.grid(row=0,column=1,padx=10,sticky=W)

              #Studetn name no
         stname_lbl=Label(cs_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
         stname_lbl.grid(row=0,column=2,padx=10)
         stdname_ip=ttk.Entry(cs_frame,textvariable=self.var_name,width=15,font=("times new roman",15))
         stdname_ip.grid(row=0,column=3,padx=10,sticky=W)

              #class Division
         stdiv_lbl=Label(cs_frame,text="Lab Group :",font=("times new roman",12,"bold"),bg="white")
         stdiv_lbl.grid(row=1,column=0,padx=10,pady=10)
         stddiv_ip=ttk.Entry(cs_frame,textvariable=self.var_div,width=15,font=("times new roman",15))
         stddiv_ip.grid(row=1,column=1,padx=10,sticky=W)


           #ROll NO
         strno_lbl=Label(cs_frame,text="Roll Number :",font=("times new roman",12,"bold"),bg="white")
         strno_lbl.grid(row=1,column=2,padx=10,pady=10)
         stdrno_ip=ttk.Entry(cs_frame,textvariable=self.var_roll,width=15,font=("times new roman",15))
         stdrno_ip.grid(row=1,column=3,padx=10,sticky=W)

              #Gender
         stg_lbl=Label(cs_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
         stg_lbl.grid(row=2,column=0,padx=10)
         stg_ip=ttk.Combobox(cs_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="readonly",background="white",width=19)
         stg_ip["values"]=("Gender","Male","Female","Others")
         stg_ip.current(0)
         stg_ip.grid(row=2,column=1,padx=10,sticky=W)

            #DOB
         stdob_lbl=Label(cs_frame,text="DOB :",font=("times new roman",12,"bold"),bg="white")
         stdob_lbl.grid(row=2,column=2,padx=10)
         cal=DateEntry(cs_frame,textvariable=self.var_dob,width=22,bd=5, foreground="white")
         cal.grid(row=2,column=3,padx=10,sticky=W)

              #Email
         stmail_lbl=Label(cs_frame,text="Email :",font=("times new roman",12,"bold"),bg="white")
         stmail_lbl.grid(row=3,column=0,padx=10,pady=10)
         stdmail_ip=ttk.Entry(cs_frame,textvariable=self.var_email,width=15,font=("times new roman",15))
         stdmail_ip.grid(row=3,column=1,padx=10,sticky=W)
        
           #Phone no
         stpno_lbl=Label(cs_frame,text="Contact Number :",font=("times new roman",12,"bold"),bg="white")
         stpno_lbl.grid(row=3,column=2,padx=10)
         stpno_ip=ttk.Entry(cs_frame,textvariable=self.var_phone,width=15,font=("times new roman",15))
         stpno_ip.grid(row=3,column=3,padx=10,sticky=W)

              #Address
         stadd_lbl=Label(cs_frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
         stadd_lbl.grid(row=4,column=0,padx=10)
         stdadd_ip=ttk.Entry(cs_frame,textvariable=self.var_address,width=15,font=("times new roman",15))
         stdadd_ip.grid(row=4,column=1,padx=10,sticky=W)

                  #Teacher Name
         sttr_lbl=Label(cs_frame,text="Teacher Name :",font=("times new roman",12,"bold"),bg="white")
         sttr_lbl.grid(row=4,column=2,padx=10)
         sttr_ip=ttk.Entry(cs_frame,textvariable=self.var_teacher,width=15,font=("times new roman",15))
         sttr_ip.grid(row=4,column=3,padx=10,sticky=W)

         #-----button frame-----
         btn_frame=Frame(cs_frame,bd=2,relief=RIDGE)
         btn_frame.place(x=0,y=175,width=680,height=38)

         save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="#ace5ee",fg="black")
         save_btn.grid(row=0,column=0)
         update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="#ace5ee",fg="black")
         update_btn.grid(row=0,column=1)

         delete_btn=Button(btn_frame,text="Delete",command=self.deleteData,width=16,font=("times new roman",13,"bold"),bg="#ace5ee",fg="black")
         delete_btn.grid(row=0,column=2)

         reset_btn=Button(btn_frame,command=self.resetData,text="Reset",width=16,font=("times new roman",13,"bold"),bg="#ace5ee",fg="black")
         reset_btn.grid(row=0,column=3)

         btn_frame1=Frame(cs_frame,bd=2,relief=RIDGE)
         btn_frame1.place(x=140,y=220,width=400,height=38)

         take_photo=Button(btn_frame1,text="Take Photo Sample",width=19,command=self.generateDataset,font=("times new roman",13,"bold"),bg="#ace5ee",fg="black")
         take_photo.grid(row=0,column=0)

         update_photo=Button(btn_frame1,text="Update Photo Sample",command=self.generateDataset,width=19,font=("times new roman",13,"bold"),bg="#ace5ee",fg="black")
         update_photo.grid(row=0,column=1)


        #-----------------------------right frame------------------------------
         right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,font=("times new roman",15,"bold"),text="Student Details Preview",bg="white")
         right_frame.place(x=760,y=10,width=750,height=620)

         img5=Image.open(r"attendese\pictures\stu.jpeg")
         img5=img5.resize((740,130),Image.ANTIALIAS)
         self.photoimg5=ImageTk.PhotoImage(img5)
         f_lbl5=Label(right_frame,image=self.photoimg5)
         f_lbl5.place(x=0,y=10,width=740,height=130)

         #========================search system=======================
         search_frame=LabelFrame(right_frame,bd=5,relief=RIDGE,font=("times new roman",15,"bold"),text="Search System",bg="white")
         search_frame.place(x=10,y=130,width=720,height=80)
         search_lbl=Label(search_frame,text="Search By : ",font=("times new roman",13,"bold"),bg="lightpink")
         search_lbl.grid(row=0,column=0,padx=10,pady=2,sticky=W)

         search_cb=ttk.Combobox(search_frame,textvariable=self.var_search_type,font=("times new roman",12,"bold"),state="readonly",background="white",width=13)
         search_cb["values"]=("Select","Roll no","Lab Group")
         search_cb.current(0)
         search_cb.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         search_ip=ttk.Entry(search_frame,textvariable=self.var_roll_search,width=15,font=("times new roman",13,"bold"))
         search_ip.grid(row=0,column=2,padx=10,sticky=W)

         search_btn=Button(search_frame,command=self.search,text="Search",bd=2,width=12,font=("times new roman",12,"bold"),bg="#ace5ee",fg="black")
         search_btn.grid(row=0,column=3,sticky=W,padx=5)
         showall_btn=Button(search_frame,command=self.fetch_data,text="Show All",bd=2,width=12,font=("times new roman",12,"bold"),bg="#ace5ee",fg="black")
         showall_btn.grid(row=0,column=4,padx=5,sticky=W)

#=========================table frame=====================
         tab_frame=Frame(right_frame,bd=5,relief=RIDGE,bg="white")
         tab_frame.place(x=10,y=220,width=720,height=360)

         scrolx=ttk.Scrollbar(tab_frame,orient=HORIZONTAL)
         scroly=ttk.Scrollbar(tab_frame,orient=VERTICAL)
         
         self.student_table=ttk.Treeview(tab_frame,columns=("Department","Course","Session","Semester","Student_ID","Student_Name","Lab_Group","Roll_no","Gender","DOB","Email","Phone_no","Address","Teacher"),xscrollcommand=scrolx.set,yscrollcommand=scroly.set)
         scrolx.pack(side=BOTTOM,fill=X)
         scroly.pack(side=RIGHT,fill=Y)
         scrolx.config(command=self.student_table.xview)
         scroly.config(command=self.student_table.yview)

         self.student_table.heading("Department",text="Department")
         self.student_table.heading("Course",text="Course")
         self.student_table.heading("Session",text="Session")
         self.student_table.heading("Semester",text="Semester")
         self.student_table.heading("Student_ID",text="Student_ID")
         self.student_table.heading("Student_Name",text="Student_Name")
         self.student_table.heading("Lab_Group",text="Lab_Group")
         self.student_table.heading("Roll_no",text="Roll no")
         self.student_table.heading("Gender",text="Gender")
         self.student_table.heading("DOB",text="DOB")
         self.student_table.heading("Email",text="Email")
         self.student_table.heading("Phone_no",text="Phone_no")
         self.student_table.heading("Address",text="Address")
         self.student_table.heading("Teacher",text="Teacher_name")
         self.student_table["show"]="headings"

         self.student_table.column("Department",width=100)
         self.student_table.column("Course",width=100)
         self.student_table.column("Session",width=100)
         self.student_table.column("Semester",width=100)
         self.student_table.column("Student_ID",width=100)
         self.student_table.column("Student_Name",width=100)
         self.student_table.column("Lab_Group",width=100)
         self.student_table.column("Roll_no",width=100)
         self.student_table.column("Gender",width=100)
         self.student_table.column("DOB",width=100)
         self.student_table.column("Email",width=100)
         self.student_table.column("Phone_no",width=100)
         self.student_table.column("Address",width=100)
         self.student_table.column("Teacher",width=100)

         self.student_table.pack(fill=BOTH,expand=1)
         self.student_table.bind("<ButtonRelease>",self.get_cursor)
         self.fetch_data()

     #==============function declaration=========
    def add_data(self):
     regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
     if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_address.get()=="" or self.var_course.get()=="Select Course" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="Gender" or self.var_sem.get()=="Select Semester" or self.var_year.get()=="Select session" or self.var_teacher.get()=="" or self.var_div.get()=="" or self.var_id.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
     elif len(self.var_phone.get())!=10:
          messagebox.showwarning("Phone number Error","Please add 10 digit phone number",parent=self.root)
     elif not(re.fullmatch(regex, self.var_email.get())):
          messagebox.showwarning("Email Error","Please add Valid email Address",parent=self.root)
     else:
          try:
               conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
               my_cursor=conn.cursor()
                         
               my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get()
               ))
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("sucess","Student Details has been added Sucessfully!",parent=self.root)
          except Exception as es:
               messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
   #===================fetch data===========       
    def fetch_data(self):

     conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
     my_cursor=conn.cursor()
     my_cursor.execute("select * from student")
     data=my_cursor.fetchall()
     if len(data)!=0:
          self.student_table.delete(*self.student_table.get_children())
          for i in data:
               self.student_table.insert("",END,values=i)
          conn.commit()
     conn.close()

 #===============get cursor===================
    def get_cursor(self,event=""):
     cursor_focus=self.student_table.focus()
     content=self.student_table.item(cursor_focus)
     data=content["values"]
     self.var_dep.set(data[0]),
     self.var_course.set(data[1]),
     self.var_year.set(data[2]),
     self.var_sem.set(data[3]),
     self.var_id.set(data[4]),
     self.var_name.set(data[5]),
     self.var_div.set(data[6]),
     self.var_roll.set(data[7]),
     self.var_gender.set(data[8]),
     self.var_dob.set(data[9]),
     self.var_email.set(data[10]),
     self.var_phone.set(data[11]),
     self.var_address.set(data[12]),
     self.var_teacher.set(data[13])

#==============update function============
    def update_data(self):
     if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_address.get()=="" or self.var_course.get()=="Select Course" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="Gender" or self.var_sem.get()=="Select Semester" or self.var_year.get()=="Select session" or self.var_teacher.get()=="" or self.var_div.get()=="" or self.var_id.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
     elif len(self.var_phone.get())!=10:
          messagebox.showwarning("Phone number Error","Please add 10 digit phone number",parent=self.root)
     elif not(re.fullmatch(regex, self.var_email.get())):
          messagebox.showwarning("Email Error","Please add Valid email Address",parent=self.root)
     else:
          try:
               Update=messagebox.askyesno("Update","Do you want to update Student Details",parent=self.root)
               if Update>0:

                    conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student SET Department=%s,Course=%s,Session=%s,Semester=%s,Student_Name=%s,Lab_Group=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone_no=%s,Address=%s,Teacher_name=%s where Student_ID=%s",(

                         self.var_dep.get(),
                         self.var_course.get(),
                         self.var_year.get(),
                         self.var_sem.get(),
                         self.var_name.get(),
                         self.var_div.get(),
                         self.var_roll.get(),
                         self.var_gender.get(),
                         self.var_dob.get(),
                         self.var_email.get(),
                         self.var_phone.get(),
                         self.var_address.get(),
                         self.var_teacher.get(),
                         self.var_id.get()  
                    ))
               else:
                    if not Update :
                         return
               messagebox.showinfo("Sucess","Student Details are Updated sucessfully",parent=self.root)
               conn.commit()
               self.fetch_data()
               conn.close()
          except Exception as es:
               messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

#=========================== Delete Button Function===========================
    def deleteData(self):
     if self.var_id.get()=="":
          messagebox.showerror("Error","Student Id must b required",parent=self.root)
     else:
          try:
               delete=messagebox.askyesno("Delete Page","Do you want to delete the Student Data?",parent=self.root)
               if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
               else:
                    if not delete:
                         return
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Deleted","Data Deleted Sucessfully!",parent=self.root)
          except Exception as es:
               messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)  

#=================Reset data Button Function====================================================  
    def resetData(self):
     self.var_dep.set("Select Department"),
     self.var_course.set("Select Course"),
     self.var_year.set("Select session"),
     self.var_sem.set("Select Semester"),
     self.var_id.set(""),
     self.var_name.set(""),
     self.var_div.set(""),
     self.var_roll.set(""),
     self.var_gender.set("Gender"),
     self.var_dob.set(""),
     self.var_email.set(""),
     self.var_phone.set(""),
     self.var_address.set(""),
     self.var_teacher.set("")   



#==============Dataset generation======================
    def generateDataset(self):
     if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_address.get()=="" or self.var_course.get()=="Select Course" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="Gender" or self.var_sem.get()=="Select Semester" or self.var_year.get()=="Select session" or self.var_teacher.get()=="" or self.var_div.get()=="" or self.var_id.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
     else:
          try:

               conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
               my_cursor=conn.cursor()
               my_cursor.execute("select * from student")
               myResult=my_cursor.fetchall()
               id=self.var_roll.get()
               # for x in myResult:
               #      id+=1
               my_cursor.execute("update student SET Department=%s,Course=%s,Session=%s,Semester=%s,Student_Name=%s,Lab_Group=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Phone_no=%s,Address=%s,Teacher_name=%s where Student_ID=%s",(

                         self.var_dep.get(),
                         self.var_course.get(),
                         self.var_year.get(),
                         self.var_sem.get(),
                         self.var_name.get(),
                         self.var_div.get(),
                         self.var_roll.get(),
                         self.var_gender.get(),
                         self.var_dob.get(),
                         self.var_email.get(),
                         self.var_phone.get(),
                         self.var_address.get(),
                         self.var_teacher.get(),
                         self.var_id.get()
                    ))
               conn.commit()
               self.fetch_data()
               self.resetData()
               conn.close()

#============face recognisation=====================
               faceClassifier=cv2.CascadeClassifier("attendese\haarcascade_frontalface_default.xml")
               def faceCroped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=faceClassifier.detectMultiScale(gray,1.3,5)
                    #scaling factor 1.3
                    #min Neighbour 5
                    for(x,y,w,h) in faces:
                         faceCrop=img[y:y+h,x:x+w]
                         return faceCrop
               cap=cv2.VideoCapture(0)
               img_id=0
               while True:
                    ret,frame1=cap.read()
                    if faceCroped(frame1) is not None:
                         img_id+=1
                    c=faceCroped(frame1)
                    face=cv2.resize(c,(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_path="attendese\Data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_path,face)
                    # cv2.putText(face,cv2.FONT_HERSHEY_COMPLEX,1,(255, 255, 255), 1,cv2.LINE_AA)
                    cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                         break

               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("Results","Generating Dataset of Student Completed")
          except Exception as es:
               messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

     #============================serach============================
    def search(self):
     def fetch_search(sby,inpt):
          conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
          my_cursor=conn.cursor()
          if sby=="r":
               my_cursor.execute("select * from student where Roll_no=%s",(inpt,))
          else:
               my_cursor.execute("select * from student where Lab_Group=%s",(inpt,))

          data=my_cursor.fetchall()
          if len(data)!=0:
               self.student_table.delete(*self.student_table.get_children())
               for i in data:
                    self.student_table.insert("",END,values=i)
               conn.commit()
          conn.close()

     if self.var_search_type.get()=="Roll no":
          inpt=self.var_roll_search.get()
          if inpt=="":
               messagebox.showwarning("Roll Number","Please, enter a Roll Number",parent=self.root)
          else:
               fetch_search("r",inpt)
     elif self.var_search_type.get()=="Lab Group":
          inpt=self.var_roll_search.get()
          if inpt=="":
               messagebox.showwarning("Lab Group","Please, enter Lab Group(1 or 2)",parent=self.root)
          else:
               fetch_search("l",inpt)
          
     else:
          messagebox.showwarning("Search Warning","Please Select search type",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()