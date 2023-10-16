from tkinter import *
from tkinter import ttk, messagebox,filedialog
from PIL import Image,ImageTk
import customtkinter as ct
from register import register_Page
from main import Attendease
import mysql.connector

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
         ip_frame=ct.CTkFrame(frame,width=515,height=241,corner_radius=10,fg_color="#000000",border_width=2)
         ip_frame.place(x=25,y=120)
         
        #==========email==================
         self.username = ct.CTkEntry(ip_frame,textvariable=self.var_username,fg_color="#2b1b33", placeholder_text="Enter your username",width=495,height=45,border_width=2,font=("times new roman",25))
         self.username.place(x=10,y=10)
        #========password================
         self.password = ct.CTkEntry(ip_frame,show="*",textvariable=self.var_password ,fg_color="#2e1929",placeholder_text="Enter your Password",width=495,height=45,font=("times new roman",25))
         self.password.place(x=10,y=65)
        #===========login button============
         login_btn=ct.CTkButton(ip_frame,command=self.login,text="Login",width=495,height=35,cursor="hand2",fg_color="#34675f",hover_color="#1f2435")
         login_btn.place(x=10,y=115)
        #==============Reginter button================
         reg_btn=ct.CTkButton(ip_frame,command=self.registration,text="Register Now",width=495,height=35,cursor="hand2",fg_color="#34675f",hover_color="#1f2435")
         reg_btn.place(x=10,y=155)
        #===============forget button=================
         fgt_btn=ct.CTkButton(ip_frame,text="Forget Password?",width=495,height=35,cursor="hand2",fg_color="#34675f",hover_color="#1f2435")
         fgt_btn.place(x=10,y=195)

    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        elif self.username.get()=="vishal" and self.password.get()=="123":
            messagebox.showinfo("Sucess","Welcome to Attendease",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from registerdb where Email=%s and Password=%s",(self.var_username.get(),self.var_password.get()))
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
            else:
                print(row)
                self.new_window=Toplevel(self.root)
                self.app=Attendease(self.new_window)
            conn.commit()
            conn.close()

    def registration(self):
            self.new_window=Toplevel(self.root)
            self.app=register_Page(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=login_Page(root)
    root.mainloop()