from tkinter import *
from tkinter import ttk, messagebox,filedialog
from PIL import Image,ImageTk
import customtkinter as ct
import mysql.connector
import re
class register_Page():
    def __init__(self,root):
         self.root= root
         self.root.geometry("750x600+350+150")
         self.root.title("Registration Page")
         self.root.iconbitmap("./attendese\pictures\icon.ico")
#=================variables===============
         self.var_fname=StringVar(value="Full Name")
         self.var_contact=StringVar(value="Contact Number")
         self.var_mail=StringVar(value="Email")
         self.var_question=StringVar()
         self.var_answer=StringVar(value="Security Answer")
         self.var_password=StringVar(value="Password")
         self.var_check=StringVar()
         
         #========background image======================
         self.wbg=ImageTk.PhotoImage(file="./attendese\pictures\greg.png")
         wbg_lbl=Label(self.root,image=self.wbg)
         wbg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

         #============Entry fields=========
         self.name = ct.CTkEntry(wbg_lbl,width=300,height=50,border_width=2,font=("times new roman",20),fg_color="#1d1325",bg_color="#1d1325",textvariable=self.var_fname)
         self.name.place(x=50,y=100)
        #========password================
         self.contactNumber = ct.CTkEntry(wbg_lbl,textvariable=self.var_contact,width=300,height=50,font=("times new roman",20),fg_color="#1d1325",bg_color="#1d1325")
         self.contactNumber.place(x=400,y=100)

         self.emailid = ct.CTkEntry(wbg_lbl,textvariable=self.var_mail, width=300,height=50,border_width=2,font=("times new roman",20),fg_color="#1d1325",bg_color="#1d1325")
         self.emailid.place(x=50,y=175)
        #========password================
         self.login_password = ct.CTkEntry(wbg_lbl,textvariable=self.var_password ,width=300,height=50,border_width=2,font=("times new roman",20),bg_color="#1d1325",fg_color="#1d1325")
         self.login_password.place(x=400,y=175)

        #  self.question = ct.CTkEntry(wbg_lbl, ",width=300,height=35,font=("times new roman",20))
         self.question=ct.CTkComboBox(wbg_lbl,variable=self.var_question,state="readonly",values=["Select Security Question","Your Birth Place","Your latest school","Favourite Pet"],width=300,height=50,bg_color="#1d1325",fg_color="#1d1325",font=("times new roman",20),button_hover_color="#140532",dropdown_font=("times new roman",20))
         self.question.set("Select Security Question")
         self.question.place(x=50,y=250)
        #========password================
         self.answer = ct.CTkEntry(wbg_lbl,textvariable=self.var_answer,bg_color="#1d1325",fg_color="#1d1325", width=300,height=50,font=("times new roman",20))
         self.answer.place(x=400,y=250)
         #======================check box==================
         self.chkbox=ct.CTkCheckBox(wbg_lbl,variable=self.var_check,text="I Agree the Terms and Conditions",hover_color="#210953",width=650,height=50,fg_color="#1d1325",bg_color="#1d1325",border_width=2,corner_radius=5,onvalue=1,offvalue=0)
         self.chkbox.place(x=50,y=325)
        #=======================login button===============
         login_btn=ct.CTkButton(wbg_lbl,text="Login Now",command=root.destroy,width=300,height=50,cursor="hand2",fg_color="#34675f",hover_color="#1f2435",bg_color="#1d1325")
         login_btn.place(x=400,y=400)
        #==============Reginter button================
         reg_btn=ct.CTkButton(wbg_lbl,text="Register Now",command=self.register_Data,width=300,height=50,cursor="hand2",fg_color="#34675f",hover_color="#1f2435",bg_color="#1d1325")
         reg_btn.place(x=50,y=400)
#=========function declaration=============
    def register_Data(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if self.var_fname.get()=="Full Name" or self.var_mail.get()=="Email" or self.var_password.get()=="Password" or self.var_question.get()=="Select Security Question" or self.var_contact.get()=="Contact Number" or self.var_answer.get()=="Security Answer":
            messagebox.showwarning("Required","All fields are Required",parent=self.root)
        elif len(self.var_contact.get())!=10:
          messagebox.showwarning("Phone number Error","Please add 10 digit phone number",parent=self.root)
        elif not(re.fullmatch(regex, self.var_mail.get())):
          messagebox.showwarning("Email Error","Please add Valid email Address",parent=self.root)
        elif self.var_check.get()!="1":
          messagebox.showwarning("Check Box error","Please Accept Terms and Conditions",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from registerdb where Email=%s",(self.var_mail.get(),))   
                row=my_cursor.fetchone()  
                if row !=None:
                  messagebox.showerror("User Exists","USer Already Exist,Please try another email",parent=self.root)
                else:
                  my_cursor.execute("insert into registerdb values(%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_contact.get(),
                    self.var_mail.get(),
                    self.var_question.get(),
                    self.var_answer.get(),
                    self.var_password.get()
                ))
                  conn.commit()
                  conn.close()
                  messagebox.showinfo("sucess","Student Details has been added Sucessfully!")
            except Exception as es:
               messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            
if __name__=="__main__":
    root=Tk()
    obj=register_Page(root)
    root.mainloop()