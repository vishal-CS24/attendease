from tkinter import *
from tkinter import ttk, messagebox,filedialog
from PIL import Image,ImageTk
import customtkinter as ct

class login_Page():
    def __init__(self,root):
         self.root= root
         self.root.geometry("1535x835+0+0")
         self.root.title("Login Page")
         self.root.iconbitmap("pictures\icon.ico")
#========background image======================
        #  self.wbg=ImageTk.PhotoImage(file="./attendese\pictures\h8.jpg")
        #  self.wbg=self.wbg.resize((1535,835),Image.ANTIALIAS)
        #  wbg_lbl=Label(self.root,image=self.wbg)
        #  wbg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

         img = Image.open("pictures\h8.jpg")
         img=img.resize((1535,835),Image.ANTIALIAS)
         self.bgimg=ImageTk.PhotoImage(img)
         f_lbl=Label(self.root,image=self.bgimg)
         f_lbl.place(x=0,y=0,width=1530,height=835)

         #=======frame for login ============
         button = ct.CTkButton(self.root, fg_color="yellow",bg_color="green",hover_color="white")  # single color name
         button.pack(side="top")
         button = ct.CTkButton(self.root, fg_color="#FF0000")  # single hex string
         button = ct.CTkButton(self.root, fg_color=("#DB3E39", "#821D1A"))  # tuple color

if __name__=="__main__":
    root=Tk()
    obj=login_Page(root)
    root.mainloop()