from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from PIL import Image,ImageTk
import cv2
import os
import mysql.connector
import numpy as np

def train_classifier():
    data_dir=(r"C:\Users\Acer\Desktop\major project\attendese\Data")
    path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
    faces=[]
    ids=[]
    for image in path:
        img=Image.open(image).convert("L")#convert ot gray scale
        imageNp=np.array(img,"uint8")
        # print(os.path.split(image.split(".")[1]))
        # print(image.split(".")[1])
        id1=int(image.split(".")[1])
        # print(id1)
        faces.append(imageNp)
        ids.append(id1)
        cv2.imshow("Training",imageNp)
        cv2.waitKey(1)==13
    ids=np.array(ids)
    #==========Traing and Save=====
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("classifier.xml")
    cv2.destroyAllWindows()
    messagebox.showinfo("Result","Training of dataset completed")







