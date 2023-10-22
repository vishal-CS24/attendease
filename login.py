from tkinter import *
from tkinter import ttk, messagebox,filedialog
from PIL import Image,ImageTk
import customtkinter as ct
from register import register_Page
from main import Attendease
import mysql.connector
from forgot import forgot_passwd

class login_Page():
    def __init__(self,root):
         self.root= root
         self.root.geometry("1535x835+0+0")
         self.root.title("Login Page")
         self.root.iconbitmap("./attendese\pictures\icon.ico")

         self.var_username = StringVar()
         self.var_password= StringVar()
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
 
#============frame for buttons and entry widgets=====================
                 #========usernamelogo========
         userlogo=Image.open("./attendese\pictures\person1.png")
         userlogo=userlogo.resize((45,45),Image.ANTIALIAS)
         self.uimg=ImageTk.PhotoImage(userlogo)
         uselogolabel=Label(frame,image=self.uimg,background="black")
         uselogolabel.place(x=70,y=130,width=45,height=45)

         passlogo=Image.open("./attendese\pictures\padlock.png")
         passlogo=passlogo.resize((45,45),Image.ANTIALIAS)
         self.pimg=ImageTk.PhotoImage(passlogo)
         passlogolabel=Label(frame,image=self.pimg,background="black")
         passlogolabel.place(x=70,y=182,width=45,height=45)
         
        #==========email==================
         self.username = ct.CTkEntry(frame,textvariable=self.var_username,fg_color="#2b1b33", placeholder_text="Enter your username",width=350,height=45,border_width=2,font=("times new roman",25))
         self.username.place(x=135,y=130)
        #========password================
         self.password = ct.CTkEntry(frame,show="*",textvariable=self.var_password ,fg_color="#2e1929",placeholder_text="Enter your Password",width=350,height=45,font=("times new roman",25))
         self.password.place(x=135,y=185)
        #===========login button============
         login_btn=ct.CTkButton(frame,command=self.login,text="Login",width=200,height=40,cursor="hand2",fg_color="#34675f",hover_color="#1f2435")
         login_btn.place(x=70,y=250)
        #==============Reginter button================
         reg_btn=ct.CTkButton(frame,command=self.registration,text="Register Now",width=200,height=40,cursor="hand2",fg_color="#34675f",hover_color="#1f2435")
         reg_btn.place(x=280,y=250)
        #===============forget button=================
         fgt_btn=ct.CTkButton(frame,text="Forget Password?",command=self.forgot_password,width=410,height=40,cursor="hand2",fg_color="#34675f",hover_color="#1f2435")
         fgt_btn.place(x=70,y=305)
         self.var_username.set("Enter Email Address")
         self.var_password.set("Pwd")

    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from registerdb where Email=%s and Password=%s",(self.var_username.get(),self.var_password.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
            else:
                self.var_username.set("Enter Email Address")
                self.var_password.set("Password")
                self.new_window=Toplevel(self.root)
                self.app=Attendease(self.new_window)
            conn.commit()
            conn.close()

    def registration(self):
            self.new_window=Toplevel(self.root)
            self.app=register_Page(self.new_window)
    def forgot_password(self):
        self.new_window=Toplevel(self.root)
        self.app=forgot_passwd(self.new_window)
if __name__=="__main__":
    root=Tk()
    obj=login_Page(root)
    root.mainloop()