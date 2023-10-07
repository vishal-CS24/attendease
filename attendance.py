from tkinter import *
from tkinter import ttk, messagebox,filedialog
from tkcalendar import Calendar, DateEntry
from PIL import Image,ImageTk
import mysql.connector
import cv2
import os
import csv

mydata=[]
class Attendance_mgmnt():
    def __init__(self,root):
         self.root= root
         self.root.geometry("1530x830+0+0")
         self.root.title("Attendance Management System")
         self.root.iconbitmap("./attendese\pictures\icon.ico")

         #-===text variables========
         self.var_status=StringVar()
         self.var_rollno=StringVar()
         self.var_time=StringVar()
         self.var_date=StringVar()
         self.var_name=StringVar()

          #  #first image
         img=Image.open(r"attendese\pictures\sd2.jpeg")
         img=img.resize((800,150),Image.ANTIALIAS)
         self.photoimg=ImageTk.PhotoImage(img)
         f_lbl=Label(self.root,image=self.photoimg)
         f_lbl.place(x=0,y=0,width=800,height=150)

        #  #2nd image
         img1=Image.open(r"attendese\pictures\sd2.jpeg")
         img1=img1.resize((800,150),Image.ANTIALIAS)
         self.photoimg1=ImageTk.PhotoImage(img1)
         f_lbl1=Label(self.root,image=self.photoimg1)
         f_lbl1.place(x=800,y=0,width=800,height=150)
#=================title===================================
         title=Label(self.root,text="Attendance Management System",font=("Rockwell Condensed",25,"bold"),bg="#ace5ee",fg="red")
         title.place(x=0,y=150,width=1530,height=80)
         #-------------------Frame----------------------
         main_frame=Frame(self.root,bd=10,bg="white")
         main_frame.place(x=0,y=220,width=1730,height=630)
         #-----------------left frame----------------------
         left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,font=("times new roman",15,"bold"),text="Student Attendance Details",bg="white")
         left_frame.place(x=10,y=5,width=720,height=600)

          #-------------image on top-----------
         img4=Image.open(r"attendese\pictures\stu.jpeg")
         img4=img4.resize((700,130),Image.ANTIALIAS)
         self.photoimg4=ImageTk.PhotoImage(img4)
         f_lbl4=Label(left_frame,image=self.photoimg4)
         f_lbl4.place(x=10,y=5,width=700,height=130)

         #---------------Attendance Information-----------------------
         a_frame=LabelFrame(left_frame,bd=5,relief=RIDGE,font=("times new roman",15,"bold"),text="Attendance Information",bg="white")
         a_frame.place(x=10,y=140,width=690,height=400)

#=========================================labels and entries======================================

#=====roll no==========
         strno_lbl=Label(a_frame,text="Roll Number :",font=("times new roman",12,"bold"),bg="white")
         strno_lbl.grid(row=0,column=0,padx=10,pady=10)
         stdrno_ip=ttk.Entry(a_frame,textvariable=self.var_rollno,width=15,font=("times new roman",15))
         stdrno_ip.grid(row=0,column=1,padx=10,sticky=W)
#=============NAME===============
         stname_lbl=Label(a_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
         stname_lbl.grid(row=0,column=2,padx=10)
         stdname_ip=ttk.Entry(a_frame,textvariable=self.var_name,width=15,font=("times new roman",15))
         stdname_ip.grid(row=0,column=3,padx=10,sticky=W)
#============TIME===============
         time_lbl=Label(a_frame,text="Time :",font=("times new roman",12,"bold"),bg="white")
         time_lbl.grid(row=1,column=0,padx=10,pady=10)
         time_ip=ttk.Entry(a_frame,textvariable=self.var_time,width=15,font=("times new roman",15))
         time_ip.grid(row=1,column=1,padx=10,sticky=W)
#-==========DATE===============
         date_lbl=Label(a_frame,text="Date :",font=("times new roman",12,"bold"),bg="white")
         date_lbl.grid(row=1,column=2,padx=10)
         date_ip=ttk.Entry(a_frame,textvariable=self.var_date,width=15,font=("times new roman",15))
         date_ip.grid(row=1,column=3,padx=10,sticky=W)

#==========ATTENDANCE STATUS==========
         att_lbl=Label(a_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
         att_lbl.grid(row=2,column=0,padx=10)
         att_cb=ttk.Combobox(a_frame,textvariable=self.var_status,font=("times new roman",12,"bold"),state="readonly",background="white")
         att_cb["values"]=("Status","Present","Absent")
         att_cb.current(0)
         att_cb.grid(row=2,column=1,padx=5,pady=10,sticky=W)

          #-----button frame-----
         btn_frame=Frame(a_frame,bd=2,relief=RIDGE)
         btn_frame.place(x=0,y=175,width=680,height=38)

         import_btn=Button(btn_frame,command=self.importCsv,text="Import",width=16,font=("times new roman",13,"bold"),bg="#ace5ee",fg="black")
         import_btn.grid(row=0,column=0)

         export_btn=Button(btn_frame,command=self.exportCsv,text="Export",width=16,font=("times new roman",13,"bold"),bg="#ace5ee",fg="black")
         export_btn.grid(row=0,column=1)

         update_btn=Button(btn_frame,command=self.update_data,text="Update",width=16,font=("times new roman",13,"bold"),bg="#ace5ee",fg="black")
         update_btn.grid(row=0,column=2)

         reset_btn=Button(btn_frame,command=self.resetData,text="Reset",width=16,font=("times new roman",13,"bold"),bg="#ace5ee",fg="black")
         reset_btn.grid(row=0,column=3)

  #-----------------Right frame----------------------
         right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,font=("times new roman",15,"bold"),text="Student Attendance Preview",bg="white")
         right_frame.place(x=760,y=5,width=750,height=600)
         #=========================table frame=====================
         tab_frame=Frame(right_frame,bd=5,relief=RIDGE,bg="white")
         tab_frame.place(x=10,y=10,width=720,height=360)

         scrolx=ttk.Scrollbar(tab_frame,orient=HORIZONTAL)
         scroly=ttk.Scrollbar(tab_frame,orient=VERTICAL)
         
         self.AttendanceReportTable=ttk.Treeview(tab_frame,columns=("Roll_no","Student_Name","Time","Date","Status"),xscrollcommand=scrolx.set,yscrollcommand=scroly.set)
         scrolx.pack(side=BOTTOM,fill=X)
         scroly.pack(side=RIGHT,fill=Y)
         scrolx.config(command=self.AttendanceReportTable.xview)
         scroly.config(command=self.AttendanceReportTable.yview)

         self.AttendanceReportTable.heading("Roll_no",text="Roll_no")
         self.AttendanceReportTable.heading("Student_Name",text="Student_Name")
         self.AttendanceReportTable.heading("Time",text="Time")
         self.AttendanceReportTable.heading("Date",text="Date")
         self.AttendanceReportTable.heading("Status",text="Status")
         self.AttendanceReportTable["show"]="headings"

         self.AttendanceReportTable.column("Roll_no",width=100)
         self.AttendanceReportTable.column("Student_Name",width=100)
         self.AttendanceReportTable.column("Time",width=100)
         self.AttendanceReportTable.column("Date",width=100)
         self.AttendanceReportTable.column("Status",width=100)

         self.AttendanceReportTable.pack(fill=BOTH,expand=1)
         self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        #  self.fetchData()

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #==========import csv==============     
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            readcsv=csv.reader(myfile,delimiter=",")
            for i in readcsv:
                mydata.append(i)
            self.fetchData(mydata)
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Warning!","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Export CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exWrite=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exWrite.writerow(i)
                messagebox.showinfo("Data Export","Your Data is Exported to "+os.path.basename(fln)+" Sucessfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursorrow=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursorrow)
        rows=content["values"]
        
        self.var_rollno.set(rows[0])
        self.var_name.set(rows[1])
        self.var_time.set(rows[3])
        self.var_date.set(rows[2])
        self.var_status.set(rows[4])
    
    def update_data(self):
        pass
        # r=self.var_rollno.get()
        # n=self.var_name.get()
        # t=self.var_time.get()
        # d=self.var_date.get()
        # s=self.var_status.get()
        # a=[r,n,t,d,s]
        # focused = self.AttendanceReportTable.focus()
        # # x = input('Enter a Value you want to change')
        # self.AttendanceReportTable.item(focused, values=("", str(s)))
        
    def resetData(self):
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("Status")



if __name__=="__main__":
    root=Tk()
    obj=Attendance_mgmnt(root)
    root.mainloop()