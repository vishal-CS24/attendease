
         lbgimg=Image.open("./attendese\pictures\ATTENDEASE.png")
         lbgimg=lbgimg.resize((565,380),Image.ANTIALIAS)
         self.bglimg1=ImageTk.PhotoImage(lbgimg)
         lbg_lbl=Label(frame,image=self.bglimg1)
         lbg_lbl.place(x=0,y=0,width=565,height=380)