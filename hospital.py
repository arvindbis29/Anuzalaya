from tkinter import*
from tkinter import ttk 
import random
import time
import tk
import datetime
import tkinter.messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
         
         
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="online Hospitel Management System",fg="red",bg="white",font=("time new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        ###########for DATA FRame##################

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        


        Dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                    font=("arial",12,"bold"),text="Patient Information")

        Dataframeleft.place(x=0,y=5,width=980,height=350)
        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                    font=("arial",12,"bold"),text="Prescription")

        DataframeRight.place(x=990,y=5,width=460,height=350)

        ###############Button Frame ##############
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        ###############Details Frame ##############
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
      #============================DataframeLeft=========================
        lblNameTablet=Label(Dataframeleft,text="Name of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNameTablet=ttk.Combobox(Dataframeleft,font=("times new roman",12,"bold"),
                                                                                    width=33)
        comNameTablet["values"]=("Nice","corona Vacacine","Acetaninophen","Adderall","Amlodipine","Ativan","fluticasone","insulin glargine",
        "lisdexamfetamine","pregabalin","tiotropium","sitagliptin","levothyroxine","rosuvastatin","albuterol","Nexium","Naproxen","Clonazepam","Pantoprazole","Prednisone") 
        comNameTablet.grid(row=0,column=1) 
        lblref=Label(Dataframeleft)                                                              
        


root=Tk()
ob=Hospital(root)
root.mainloop()