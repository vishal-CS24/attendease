from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import train
import face_recognisation
from attendance import Attendance_mgmnt

class Attendease():
    def __init__(self,root):
         self.root= root
         self.root.geometry("1535x835+0+0")
         self.root.title("ATTENDEASE")
         self.root.iconbitmap("./attendese\pictures\icon.ico")
#-----------------------Top bar--------------------------------------------------------------
     #    #  #first image


     #    #  #2nd image
     #     img1=Image.open(r"attendese\pictures\h4.jpeg")
     #     img1=img1.resize((500,130),Image.ANTIALIAS)
     #     self.photoimg1=ImageTk.PhotoImage(img1)
     #     f_lbl1=Label(self.root,image=self.photoimg1)
     #     f_lbl1.place(x=550,y=0,width=500,height=130)

     #     #3rd image
     #     img2=Image.open(r"attendese\pictures\h4.jpeg")
     #     img2=img2.resize((550,130),Image.ANTIALIAS)
     #     self.photoimg2=ImageTk.PhotoImage(img2)
     #     f_lbl2=Label(self.root,image=self.photoimg2)
     #     f_lbl2.place(x=1050,y=0,width=550,height=130)
        # ----------------------------------------#background image---------------------------------------------------------------
     #     bgimg=Image.open(r"attendese\pictures\loginback1.jpg")
     #     bgimg=bgimg.resize((1530,790),Image.ANTIALIAS)
     #     self.bgphotoimg=ImageTk.PhotoImage(bgimg)
     #     bglbl=Label(self.root,image=self.bgphotoimg)
     #     bglbl.place(x=0,y=0,width=1530,height=790)

         self.bg=ImageTk.PhotoImage(file="./attendese\pictures\loginback1.jpg")
         bglbl=Label(self.root,image=self.bg)
         bglbl.place(x=0,y=0,relwidth=1,relheight=1)

         img=Image.open(r"attendese\pictures\homepage.png")
         img=img.resize((570,380),Image.ANTIALIAS)
         self.photoimg=ImageTk.PhotoImage(img)
         f_lbl=Label(bglbl,image=self.photoimg)
         f_lbl.place(x=480,y=235,width=570 ,height=370)

         #------------------------------------------Title--------------------------------------------------------------------
     #     title=Label(bglbl,text="ATTENDEASE",font=("Rockwell Condensed",25,"bold"),bg="#2a6f87",fg="#052556")
     #     title.place(x=0,y=0,width=1530,height=45)
     #     title1=Label(bglbl,text="(A Machine learning based Attendance System)",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
     #     title1.place(x=0,y=40,width=1530,height=45)
         #--------------------Student Button--------------------------
         stdbutton=Image.open(r"attendese\pictures\st.jpg")
         stdbutton=stdbutton.resize((220,220),Image.ANTIALIAS)
         self.stdphotoimg=ImageTk.PhotoImage(stdbutton)
         sb=Button(bglbl,image=self.stdphotoimg,command=self.student_details,cursor="hand2")
         sb.place(x=195,y=10,width=220,height=220)
        #  sbl=Button(bglbl,text="Student Details",command=self.student_details,cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
        #  sbl.place(x=195,y=195,width=220,height=40)
                #------------------------Training Data----------------------------
         trbutton=Image.open(r"attendese\pictures\training.jpeg")
         trbutton=trbutton.resize((220,220),Image.ANTIALIAS)
         self.trphotoimg=ImageTk.PhotoImage(trbutton)
         sb2=Button(bglbl,command=self.classifier_train,image=self.trphotoimg,cursor="hand2")
         sb2.place(x=425,y=10,width=220,height=220)
        #  sbl2=Button(bglbl,command=self.classifier_train,text="Train Data",cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
        #  sbl2.place(x=425,y=195,width=220,height=40)
         #----------------FACE DETECTION-------------------------------------
         fdbutton=Image.open(r"attendese\pictures\h14.jpeg")
         fdbutton=fdbutton.resize((220,220),Image.ANTIALIAS)
         self.fdphotoimg=ImageTk.PhotoImage(fdbutton)
         sb1=Button(bglbl,command=self.recognize_face,image=self.fdphotoimg,cursor="hand2")
         sb1.place(x=655,y=10,width=220,height=220)
        #  sbl1=Button(bglbl,text="Face Detector",cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
        #  sbl1.place(x=655,y=195,width=220,height=40)
     
    #--------------------------Attendance---------------------------
         adbutton=Image.open(r"attendese\pictures\attendance.jpeg")
         adbutton=adbutton.resize((220,220),Image.ANTIALIAS)
         self.adphotoimg=ImageTk.PhotoImage(adbutton)

         sb3=Button(bglbl,command=self.attendance,image=self.adphotoimg,cursor="hand2")
         sb3.place(x=885,y=10,width=220,height=220)
        #  sbl3=Button(bglbl,command=self.attendance,text="Attendance Details",cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
        #  sbl3.place(x=885,y=195,width=220,height=40)

    #-----------------Photos------------------------
         phbutton=Image.open(r"attendese\pictures\photos.jpg")
         phbutton=phbutton.resize((220,220),Image.ANTIALIAS)
         self.phphotoimg=ImageTk.PhotoImage(phbutton)

         sb4=Button(bglbl,command=self.open_images,image=self.phphotoimg,cursor="hand2")
         sb4.place(x=1115,y=10,width=220,height=220)
        #  sbl4=Button(bglbl,command=self.open_images,text="Photos",cursor="hand2",font=("Arial", 15,"bold"),bg="#2a6f87",fg="#052556")
        #  sbl4.place(x=1115,y=195,width=220,height=40)

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
