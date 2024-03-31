from tkinter import *
from tkinter import ttk, messagebox
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
         self.root.iconbitmap("pictures\icon.ico")
#-----------------------Top bar--------------------------------------------------------------
         self.bg = ImageTk.PhotoImage(file="pictures\loginback1.jpg")
         bglbl=Label(self.root,image=self.bg)
         bglbl.place(x=0,y=0,relwidth=1,relheight=1)

         img = Image.open(r"pictures\homepage.png")
         img=img.resize((570,380),Image.ANTIALIAS)
         self.photoimg=ImageTk.PhotoImage(img)
         f_lbl=Label(bglbl,image=self.photoimg)
         f_lbl.place(x=480,y=235,width=570 ,height=370)

         #--------------------Student Button--------------------------
         stdbutton = Image.open(r"pictures\studetails.png")
         stdbutton=stdbutton.resize((130,130),Image.ANTIALIAS)
         self.stdphotoimg=ImageTk.PhotoImage(stdbutton)
         sb=ct.CTkButton(bglbl,text="",image=self.stdphotoimg,command=self.student_details,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f",anchor="center")
         sb.place(x=80,y=70)
                #------------------------Training Data----------------------------
         trbutton = Image.open(r"pictures\traindata.png")
         trbutton=trbutton.resize((130,130),Image.ANTIALIAS)
         self.trphotoimg=ImageTk.PhotoImage(trbutton) 
         sb2=ct.CTkButton(bglbl,command=self.classifier_train,text="",image=self.trphotoimg,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f")
         sb2.place(x=80,y=240)
    
         #----------------FACE DETECTION-------------------------------------
         fdbutton = Image.open(r"pictures\face detect.png")
         fdbutton=fdbutton.resize((130,130),Image.ANTIALIAS)
         self.fdphotoimg=ImageTk.PhotoImage(fdbutton)
         sb1=ct.CTkButton(bglbl,text="",command=self.recognize_face,image=self.fdphotoimg,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f")
         sb1.place(x=80,y=410)
    #--------------------------Attendance---------------------------
         adbutton = Image.open(r"pictures\attenddetails.png")
         adbutton=adbutton.resize((130,130),Image.ANTIALIAS)
         self.adphotoimg=ImageTk.PhotoImage(adbutton)

         sb3=ct.CTkButton(bglbl,text="",command=self.attendance,image=self.adphotoimg,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f")
         sb3.place(x=1290,y=70)
 
    #-----------------Photos------------------------
         phbutton = Image.open(r"pictures\photosget.png")
         phbutton=phbutton.resize((130,130),Image.ANTIALIAS)
         self.phphotoimg=ImageTk.PhotoImage(phbutton)

         sb4=ct.CTkButton(bglbl,text="",command=self.open_images,image=self.phphotoimg,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f")
         sb4.place(x=1290,y=240)
    
    #----------------Help--------------------
         hbutton = Image.open(r"pictures\support.png")
         hbutton=hbutton.resize((130,130),Image.ANTIALIAS)
         self.hphotoimg=ImageTk.PhotoImage(hbutton)

         sb5=ct.CTkButton(bglbl,text="",command=self.support_win,image=self.hphotoimg,cursor="hand2",corner_radius=20,bg_color="black",fg_color="#ec850a",hover_color="#d96b0f")
         sb5.place(x=1290,y=400)

    #---------------------------Exit------------------------------
         ebutton = Image.open(r"pictures\log-out1.png")
         ebutton=ebutton.resize((100,100),Image.ANTIALIAS)
         self.ehphotoimg=ImageTk.PhotoImage(ebutton)
         sb5=Button(bglbl,command=root.destroy,image=self.ehphotoimg,cursor="hand2",background="black")
         sb5.place(x=1340,y=680,width=100,height=100)
         
    #====================photo Access===========
    def open_images(self):
        os.startfile(r"Data")
    #===============================function for student button================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    #=========function for classifier=========
    def classifier_train(self):
      train.train_classifier()
      messagebox.showinfo(
          "Result", "Training of dataset completed", parent=self.root)
    #===========function for recognize face==================
    def recognize_face(self):
      face_recognisation.faceRecognisation()
    #=========function for attendance mark=====================
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_mgmnt(self.new_window)

    def support_win(self):
         self.support_window=Toplevel(self.root)
         self.support_window.geometry("1535x835+0+0")
         self.support_window.title("How can I help you?")
         self.support_window.iconbitmap("pictures\icon.ico")
         self.support_window.minsize(1535,835)
         self.root.state('zoomed')
         supp_img = Image.open(r"pictures\support_contactuspage.png")
         supp_img=supp_img.resize((1535,835),Image.ANTIALIAS)
         self.sup_photoimg=ImageTk.PhotoImage(supp_img)
         supp_lbl=Label(self.support_window,image=self.sup_photoimg)
         supp_lbl.place(x=0,y=0,width=1535,height=835)
if __name__=="__main__":
    root=Tk()
    obj=Attendease(root)
    root.mainloop()
