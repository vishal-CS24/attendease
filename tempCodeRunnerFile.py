from tkinter import *
from tkinter import ttk, messagebox,filedialog
from PIL import Image,ImageTk
import customtkinter as ct

class login_Page():
    def __init__(self,root):
         self.root= root
         self.root.geometry("1535x835+0+0")
         self.root.title("Login Page")
         self.root.iconbitmap("./attendese\pictures\icon.ico")
#========background image======================
         self.wbg=ImageTk.PhotoImage(file="./attendese\pictures\loginback1.jpg")
         wbg_lbl=Label(self.root,image=self.wbg)
         wbg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

         #=======frame for login ============
         frame=ct.CTkFrame(self.root,width=565,height=380)
         frame.place(x=485,y=230)

         lbgimg=Image.open("./attendese\pictures\ATTENDEASE.png")
         lbgimg=lbgimg.resize((565,380),Image.ANTIALIAS)
         self.bglimg1=ImageTk.PhotoImage(lbgimg)
         lbg_lbl=Label(frame,image=self.bglimg1)
         lbg_lbl.place(x=0,y=0,width=565,height=380)

#=============login logo====================
        #  l_img=Image.open("./attendese\pictures\login.png")
        #  l_img=l_img.resize((100,100),Image.ANTIALIAS)
        #  self.bglimg=ImageTk.PhotoImage(l_img)
        #  l_lbl=Label(frame,image=self.bglimg,bg="#000000")
        #  l_lbl.place(x=230,y=10,width=100,height=100)
#============frame for buttons and entry widgets=====================
         ip_frame=ct.CTkFrame(frame,width=515,height=241,corner_radius=10,fg_color="#000000",border_width=2)
         ip_frame.place(x=25,y=120)

   
        #==========email==================
         self.username = ct.CTkEntry(ip_frame,fg_color="#2b1b33", placeholder_text="Enter your username",width=495,height=45,border_width=2,font=("times new roman",25))
         self.username.place(x=10,y=10)