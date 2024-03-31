from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from PIL import Image,ImageTk
import cv2
import os
import mysql.connector
import numpy as np
from time import strftime
from datetime import datetime
import csv


def mark_attendance(id1, n):
    now = datetime.now()
    date = now.strftime("%d_%m_%Y")

    # Predefined column names
    columns = ['Rollno', 'Name', 'Time', 'Date', 'Status']

    # Check if the file already exists, if not, write the header
    file_path = f"Attendance_files/{date}.csv"
    is_file_empty = not os.path.isfile(
        file_path) or os.stat(file_path).st_size == 0

    with open(file_path, "a+", newline="\n") as f:
        writer = csv.DictWriter(f, fieldnames=columns)

        # Write header if the file is empty
        if is_file_empty:
            writer.writeheader()

        # Check if the ID is already in the attendance file
        f.seek(0)
        myDataList = f.readlines()
        id_list = [line.split(",")[0] for line in myDataList]

        if str(id1) not in id_list:
            time = now.strftime("%H:%M:%S")
            date = now.strftime("%d-%m-%Y")

            # Write attendance entry
            writer.writerow({'Rollno': id1, 'Name': n,
                            'Time': time, 'Date': date, 'Status': 'present'})


def faceRecognisation():
    def draw_boundary(img,classifier,scaleFactor,minNeighbors,colour,text,clf):
        gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
        coord=[]
        for (x,y,w,h) in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id1,predic=clf.predict(gray_image[y:y+h,x:x+w])
            confidence=int((100*(1-predic/300)))
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendease_db")
            my_cursor=conn.cursor()
            my_cursor.execute("select Student_Name from student where Roll_no="+str(id1))
            n=my_cursor.fetchone()
            n="+".join(n)
            if confidence>77:
                cv2.putText(img,f"Roll:{id1}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                cv2.putText(img,f"Name:{n}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                mark_attendance(id1,n)
            else:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(img,f"Unknown face",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
            coord=[x,y,w,h]
        return coord
    def recognize(img,classifier,faceCascade):
        coords=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
        return img
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")
    video_cap=cv2.VideoCapture(0)
    while(True):
        ret,img=video_cap.read()
        img=recognize(img,clf,faceCascade)
        cv2.imshow("Welcome to Face Recognisation",img)
        if cv2.waitKey(1)==13:
            break
    video_cap.release()
    cv2.destroyAllWindows()