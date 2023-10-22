from tkinter import *
from tkinter import ttk, messagebox,filedialog
from PIL import Image,ImageTk
import customtkinter as ct
from register import register_Page
from main import Attendease
import mysql.connector

class forgot_passwd():
    def __init__(self,root):
         self.root= root
         self.root.geometry("400x300+1000+300")
         self.root.title("Forgot Password")
         self.root.iconbitmap("./attendese\pictures\icon.ico")

         self.var_question=StringVar()
         self.var_answer=StringVar(value="Security Answer")
         self.var_mail=StringVar(value="Email")

          #  self.question = ct.CTkEntry(wbg_lbl, ",width=300,height=35,font=("times new roman",20))
         self.question=ct.CTkComboBox(self.root,variable=self.var_question,state="readonly",values=["Select Security Question","Your Birth Place","Your latest school","Favourite Pet"],width=300,height=50,bg_color="#1d1325",fg_color="#1d1325",font=("times new roman",20),button_hover_color="#140532",dropdown_font=("times new roman",20))
         self.question.set("Select Security Question")
         self.question.place(x=10,y=20)
        #========password================
         self.answer = ct.CTkEntry(self.root,textvariable=self.var_answer,bg_color="#1d1325",fg_color="#1d1325", width=300,height=50,font=("times new roman",20))
         self.answer.place(x=10,y=80)

         self.emailid = ct.CTkEntry(self.root,textvariable=self.var_mail, width=300,height=50,border_width=2,font=("times new roman",20),fg_color="#1d1325",bg_color="#1d1325")
         self.emailid.place(x=10,y=140)

         self.fetch_button=ct.CTkButton(self.root,text="Get password",command=self.fetch_Password,width=300,height=50,cursor="hand2",fg_color="#34675f",hover_color="#1f2435",bg_color="#1d1325")
         self.fetch_button.place(x=10,y=200)

    def fetch_Password(self):
        if self.var_mail.get()=="Email" or self.var_question.get()=="Select Security Question" or self.var_answer.get()=="Security Answer":
            messagebox.showwarning("Required","All fields are Required",parent=self.root)
        else:

            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
                my_cursor=conn.cursor()
                my_cursor.execute("select Password from registerdb where Security_Question=%s and Answer=%s and Email=%s" ,(self.var_question.get(),self.var_answer.get(),self.var_mail.get()))   
                data=my_cursor.fetchall()
                print(data[0][0])
                conn.commit()
                conn.close()
                messagebox.showinfo("Forgot Password",f"Your password is {data[0][0]}",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=forgot_passwd(root)
    root.mainloop()         