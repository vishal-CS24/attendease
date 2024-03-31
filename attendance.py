from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import csv
import pandas as pd
import customtkinter as ct
from concat import mark_attendance_in_excel
mydata = []


class Attendance_mgmnt():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1535x835+0+0")
        self.root.title("Attendance Management System")
        self.root.iconbitmap("pictures\icon.ico")
        self.root.state('zoomed')

        # -===text variables========
        self.var_name = StringVar()
        self.var_rollno = StringVar()
        self.var_Tla = StringVar()
        self.var_Tld = StringVar()
        self.var_Pecnt = StringVar()

        #  #first image
        img = Image.open(r"pictures\sd2.jpeg")
        img = img.resize((800, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=150)

       #  #2nd image
        img1 = Image.open(r"pictures\sd2.jpeg")
        img1 = img1.resize((800, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=800, y=0, width=800, height=150)
# =================title===================================
        title = Label(self.root, text="Attendance Management System", font=(
            "Rockwell Condensed", 25, "bold"), bg="#ace5ee", fg="#ec4924")
        title.place(x=0, y=150, width=1530, height=80)

        # def homeButton(self):
        #     pass

        # homebutton = Image.open(r"pictures\home-page.png")
        # homebutton = homebutton.resize((50, 50), Image.ANTIALIAS)
        # self.stdphotoimg = ImageTk.PhotoImage(homebutton)
        # hb = ct.CTkButton(title, text="", image=self.stdphotoimg, cursor="hand2", corner_radius=20,
        #                   bg_color="#ace5ee", fg_color="#ace5ee", hover_color="#ace5ee", anchor="center", width=60, height=60)
        # hb.place(x=0, y=0)
        # -------------------Frame----------------------
        main_frame = Frame(self.root, bd=10, bg="white")
        main_frame.place(x=0, y=220, width=1730, height=630)
        # -----------------left frame----------------------
        left_frame = LabelFrame(main_frame, bd=5, relief=RIDGE, font=(
            "times new roman", 15, "bold"), text="Student Attendance Details", bg="white")
        left_frame.place(x=10, y=5, width=720, height=600)

        # -------------image on top-----------
        img4 = Image.open(r"pictures\stu.jpeg")
        img4 = img4.resize((700, 130), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        f_lbl4 = Label(left_frame, image=self.photoimg4)
        f_lbl4.place(x=10, y=5, width=700, height=130)

        # ---------------Attendance Information-----------------------
        a_frame = LabelFrame(left_frame, bd=5, relief=RIDGE, font=(
            "times new roman", 15, "bold"), text="Attendance Information", bg="white")
        a_frame.place(x=10, y=140, width=690, height=400)

# =========================================labels and entries======================================
# =====roll no==========
        strno_lbl = Label(a_frame, text="Roll Number :", font=(
            "times new roman", 12, "bold"), bg="white")
        strno_lbl.grid(row=0, column=0, padx=10, pady=10)
        stdrno_ip = ttk.Entry(
            a_frame, textvariable=self.var_rollno, width=15, font=("times new roman", 15))
        stdrno_ip.grid(row=0, column=1, padx=10, sticky=W)
# =============NAME===============
        stname_lbl = Label(a_frame, text="Student Name :", font=(
            "times new roman", 12, "bold"), bg="white")
        stname_lbl.grid(row=0, column=2, padx=10)
        stdname_ip = ttk.Entry(
            a_frame, textvariable=self.var_name, width=15, font=("times new roman", 15))
        stdname_ip.grid(row=0, column=3, padx=10, sticky=W)
# ============lecture attended===============
        la_lbl = Label(a_frame, text="Lecture Attended :", font=(
            "times new roman", 12, "bold"), bg="white")
        la_lbl.grid(row=1, column=0, padx=10, pady=10)

        la_ip = ttk.Entry(a_frame, textvariable=self.var_Tla,
                          width=15, font=("times new roman", 15))
        la_ip.grid(row=1, column=1, padx=10, sticky=W)
# ============lecture delevred========
        ld_lbl = Label(a_frame, text="Lecture Delivered :", font=(
            "times new roman", 12, "bold"), bg="white")
        ld_lbl.grid(row=1, column=2, padx=10, pady=10)

        ld_ip = ttk.Entry(a_frame, textvariable=self.var_Tld,
                          width=15, font=("times new roman", 15))
        ld_ip.grid(row=1, column=3, padx=10, sticky=W)
# # -==========percentage===============
        per_lbl = Label(a_frame, text="Percentage :", font=(
            "times new roman", 12, "bold"), bg="white")
        per_lbl.grid(row=2, column=0, padx=10)
        per_ip = ttk.Entry(a_frame, textvariable=self.var_Pecnt,
                           width=15, font=("times new roman", 15))
        per_ip.grid(row=2, column=1, padx=10, sticky=W)
        
        # -----button frame-----
        btn_frame = Frame(a_frame, bd=2, relief=RIDGE, bg="white",cursor="hand2")
        btn_frame.place(x=0, y=150, width=680, height=70)
# ===============import file=========================
        import_btn = Button(btn_frame, text="Import", command=self.importCsv, width=16, font=(
            "times new roman", 13, "bold"), bg="#ace5ee", fg="black")
        import_btn.grid(row=0, column=0)
# ======================export data===============================================
        export_btn = Button(btn_frame, text="Export", command=self.exportCsv, width=16, font=(
            "times new roman", 13, "bold"), bg="#ace5ee", fg="black")
        export_btn.grid(row=0, column=1)
# ===============update data======================
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=16, font=(
            "times new roman", 13, "bold"), bg="#ace5ee", fg="black")
        update_btn.grid(row=0, column=2)
# =============export updated data=====================
        update1_btn = Button(btn_frame, text="Export Updated Data", command=self.exportupdatedCsv, width=16, font=(
            "times new roman", 13, "bold"), bg="#ace5ee", fg="black")
        update1_btn.grid(row=4, column=1)
# =============reset button ==========================
        reset_btn = Button(btn_frame, text="Reset", command=self.resetData, width=16, font=(
            "times new roman", 13, "bold"), bg="#ace5ee", fg="black")
        reset_btn.grid(row=0, column=3)
# =====================================compile vutton==========================
        compile_btn = Button(btn_frame, text="Compile Attendance", command=self.compiled, width=16, font=(
            "times new roman", 13, "bold"), bg="#ace5ee", fg="black")
        compile_btn.grid(row=4, column=2)

        # -----------------Right frame----------------------
        right_frame = LabelFrame(main_frame, bd=5, relief=RIDGE, font=(
            "times new roman", 15, "bold"), text="Student Attendance Preview", bg="white")
        right_frame.place(x=760, y=5, width=750, height=600)
        # =========================table frame=====================
        tab_frame = Frame(right_frame, bd=5, relief=RIDGE, bg="white")
        tab_frame.place(x=10, y=10, width=720, height=550)

        scrolx = ttk.Scrollbar(tab_frame, orient=HORIZONTAL)
        scroly = ttk.Scrollbar(tab_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(tab_frame, columns=(
            "Roll_no", "Student_Name", "Tla", "Tld", "prcnt"), xscrollcommand=scrolx.set, yscrollcommand=scroly.set)
        scrolx.pack(side=BOTTOM, fill=X)
        scroly.pack(side=RIGHT, fill=Y)
        scrolx.config(command=self.AttendanceReportTable.xview)
        scroly.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Roll_no", text="Roll No")
        self.AttendanceReportTable.heading("Student_Name", text="Student Name")
        self.AttendanceReportTable.heading(
            "Tla", text="Lecture Attended")
        self.AttendanceReportTable.heading(
            "Tld", text="Lecture Delivered")
        self.AttendanceReportTable.heading("prcnt", text="Percentage")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("Roll_no", width=100)
        self.AttendanceReportTable.column("Student_Name", width=100)
        self.AttendanceReportTable.column("Tla", width=100)
        self.AttendanceReportTable.column("Tld", width=100)
        self.AttendanceReportTable.column("prcnt", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def get_cursor(self, event=""):
        cursorrow = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursorrow)
        rows = content["values"]
        self.var_rollno.set(rows[0])
        self.var_name.set(rows[1])
        self.var_Tla.set(rows[2])
        self.var_Tld.set(rows[3])
        self.var_Pecnt.set(rows[4])

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open Excel",
                                         filetypes=(("Excel File", "*.xlsx"), ("ALL Files", "*.*")), parent=self.root)
        try:
            if fln:
                df = pd.read_excel(fln)
                mydata = df.values.tolist()
                self.fetchData(mydata)
        except Exception as e:
            messagebox.showerror(
                "Error", f"Error reading Excel file: {str(e)}", parent=self.root)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "Warning!", "No Data Found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Export Excel",
                                               filetypes=(("Excel File", "*.xlsx"), ("ALL File", "*.*")), parent=self.root)
            if fln:
                # Create a DataFrame from the first four columns of mydata
                selected_data = [row[:5] for row in mydata]
                df = pd.DataFrame(
                    selected_data, columns=["Roll no", "Student Name", "Lecture Attended", "Lecture Delivered", "Percentage"])
                df_export = df.iloc[:, :5]  # Selecting the first four columns
                # Export DataFrame to Excel file
                df_export.to_excel(fln, index=False)
                messagebox.showinfo("Data Export", f"Your Data is Exported to {os.path.basename(fln)} Successfully",
                                    parent=self.root)
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to: {str(es)}", parent=self.root)

    def resetData(self):
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_Tla.set("")
        self.var_Tld.set("")
        self.var_Pecnt.set("")

    def percent(self, tla, tld):
        p = tla/tld*100
        return round(p, 2)

    def update_data(self):
        try:
            roll_no = self.var_rollno.get()
            student_name = self.var_name.get()
            Tla = self.var_Tla.get()
            Tld = self.var_Tld.get()
            percentage = self.percent(int(Tla), int(Tld))

            # Update the selected row in the Treeview
            selected_row = self.AttendanceReportTable.selection()[0]
            self.AttendanceReportTable.item(selected_row, values=(
                roll_no, student_name, Tla, Tld, percentage))
            # Clear the entry boxes after updating
            self.resetData()

            messagebox.showinfo(
                "Update", "Data Updated Successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error updating data: {str(es)}", parent=self.root)

    def exportupdatedCsv(self):
        try:
            if self.AttendanceReportTable.get_children():
                all_data = []

                for row_id in self.AttendanceReportTable.get_children():
                    values = self.AttendanceReportTable.item(row_id, 'values')
                    # Select only the first four columns of each row
                    selected_data = values[:4]
                    all_data.append(selected_data)

                fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Export Excel",
                                                   filetypes=(
                                                       ("Excel File", "*.xlsx"), ("ALL File", "*.*")),
                                                   parent=self.root)

                if fln:
                    # Create a DataFrame from the selected data in the Treeview
                    df_export = pd.DataFrame(all_data,
                                             columns=["Roll no", "Student Name", "Lecture Attended", "Lecture Delivered", "Percentage"])

                    # Export DataFrame to Excel file
                    df_export.to_excel(fln, index=False)

                    messagebox.showinfo("Data Export", f"Your Data is Exported to {os.path.basename(fln)} Successfully",
                                        parent=self.root)
            else:
                messagebox.showerror(
                    "Warning!", "No Data Found to Export", parent=self.root)

        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to: {str(es)}", parent=self.root)

    def compiled(self):
        compiled_attendance_file = './Attendance_files/compiled_Attendance.xlsx'
        input_directory = './Attendance_files/'
        opf = mark_attendance_in_excel(
            compiled_attendance_file, input_directory)
        if opf:
            messagebox.showinfo("Compiled FIles",
                                f"Attendance is compiled sucessfully in {opf}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Attendance_mgmnt(root)
    root.mainloop()
