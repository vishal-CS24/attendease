from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import train
import face_recognisation
from attendance import Attendance_mgmnt
import customtkinter as ct

class Attendease():
    def __init__(self,root):
         self.root= root
         self.root.geometry("1535x835+0+0")
         self.root.title("ATTENDEASE")
         self.root.state('zoomed')
         self.root.iconbitmap("./attendese\pictures\icon.ico")
#-----------------------Top bar--------------------------------------------------------------
         self.bg=ImageTk.PhotoImage(file="./attendese\pictures\loginback1.jpg")
         bglbl=Label(self.root,image=self.bg)
         bglbl.place(x=0,y=0,relwidth=1,relheight=1)

         img=Image.open(r"attendese\pictures\homepage.png")
         img=img.resize((570,380),Image.ANTIALIAS)
         self.photoimg=ImageTk.PhotoImage(img)
         f_lbl=Label(bglbl,image=self.photoimg)
         f_lbl.place(x=480,y=235,width=570 ,height=370)

         #--------------------Student Button--------------------------
         stdbutton=Image.open(r"attendese\pictures\studetails.png")
         stdbutton=stdbutton.resize((150,150),Image.ANTIALIAS)
         self.stdphotoimg=ImageTk.PhotoImage(stdbutton)
         sb=ct.CTkButton(bglbl,text="",image=self.stdphotoimg,command=self.student_details,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f")
         sb.place(x=200,y=10)
        #  sbl=Button(bglbl,text="Student Details",command=self.student_details,cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
        #  sbl.place(x=195,y=195,width=220,height=40)
                #------------------------Training Data----------------------------
         trbutton=Image.open(r"attendese\pictures\traindata.png")
         trbutton=trbutton.resize((150,150),Image.ANTIALIAS)
         self.trphotoimg=ImageTk.PhotoImage(trbutton) 
         sb2=ct.CTkButton(bglbl,command=self.classifier_train,text="",image=self.trphotoimg,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f")
         sb2.place(x=415,y=10)
        #  sbl2=Button(bglbl,command=self.classifier_train,text="Train Data",cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
        #  sbl2.place(x=425,y=195)
         #----------------FACE DETECTION-------------------------------------
         fdbutton=Image.open(r"attendese\pictures\face detect.png")
         fdbutton=fdbutton.resize((150,150),Image.ANTIALIAS)
         self.fdphotoimg=ImageTk.PhotoImage(fdbutton)
         sb1=ct.CTkButton(bglbl,text="",command=self.recognize_face,image=self.fdphotoimg,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f")
         sb1.place(x=635,y=10)
        #  sbl1=Button(bglbl,text="Face Detector",cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
        #  sbl1.place(x=655,y=195,width=150,height=40)
     
    #--------------------------Attendance---------------------------
         adbutton=Image.open(r"attendese\pictures\details.png")
         adbutton=adbutton.resize((150,150),Image.ANTIALIAS)
         self.adphotoimg=ImageTk.PhotoImage(adbutton)

         sb3=ct.CTkButton(bglbl,text="",command=self.attendance,image=self.adphotoimg,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f")
         sb3.place(x=855,y=10)
        #  sbl3=Button(bglbl,command=self.attendance,text="Attendance Details",cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
        #  sbl3.place(x=885,y=195,width=150,height=40)

    #-----------------Photos------------------------
         phbutton=Image.open(r"attendese\pictures\photosget.png")
         phbutton=phbutton.resize((150,150),Image.ANTIALIAS)
         self.phphotoimg=ImageTk.PhotoImage(phbutton)

         sb4=ct.CTkButton(bglbl,text="",command=self.open_images,image=self.phphotoimg,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f")
         sb4.place(x=1075,y=10)
        #  sbl4=Button(bglbl,command=self.open_images,text="Photos",cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
        #  sbl4.place(x=1115,y=195,width=150,height=40)

    #----------------Help--------------------
         hbutton=Image.open(r"attendese\pictures\support.png")
         hbutton=hbutton.resize((220,120),Image.ANTIALIAS)
         self.hphotoimg=ImageTk.PhotoImage(hbutton)

         sb5=Button(bglbl,image=self.hphotoimg,cursor="hand2",bd=10,background="#5bb6c3")
         sb5.place(x=535,y=680,width=220,height=120)
     #     sbl5=Button(bglbl,text="Support",cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
     #     sbl5.place(x=535,y=510,width=220,height=40)

    #---------------------------Exit------------------------------
         ebutton=Image.open(r"attendese\pictures\exit.png")
         ebutton=ebutton.resize((220,120),Image.ANTIALIAS)
         self.ehphotoimg=ImageTk.PhotoImage(ebutton)
         sb5=Button(bglbl,command=root.destroy,image=self.ehphotoimg,cursor="hand2",background="#5bb6c3")
         sb5.place(x=765,y=680,width=220,height=120)
     #     sbl5=Button(bglbl,command=root.destroy,text="Exit",cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
     #     sbl5.place(x=765,y=510,width=220,height=40)
    #====================photo Access===========
    def open_images(self):
        os.startfile(r"C:\Users\Acer\Desktop\major project\attendese\Data")
    #===============================function for student button================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    #=========function for classifier=========
    def classifier_train(self):
      train.train_classifier()
    #===========function for recognize face==================
    def recognize_face(self):
      face_recognisation.faceRecognisation()
    #=========function for attendance mark=====================
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_mgmnt(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Attendease(root)
    root.mainloop()
