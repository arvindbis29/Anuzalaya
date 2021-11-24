from tkinter import*
from tkinter import ttk 
import random
import time
import datetime
import tkinter.messagebox
from tkinter.messagebox import showinfo
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.nameoftablet=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateofBirth=StringVar()
        self.PatientAddress=StringVar()
        self.Booldp=StringVar()


                
         
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Online Hospital Management System",fg="red",bg="white",font=("time new roman",50,"bold"))
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
       #===============lable for tablet==================
        lblNameTablet=Label(Dataframeleft,text="Name of Tablet",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNameTablet=ttk.Combobox(Dataframeleft,textvariable=self.nameoftablet,state="readonly", font=("arial",12,"bold"),
                                                                                    width=33)
        comNameTablet["values"]=("Nice","corona Vacacine","Acetaninophen","Adderall","Amlodipine","Ativan","fluticasone","insulin glargine",
        "lisdexamfetamine","pregabalin","tiotropium","sitagliptin","levothyroxine","rosuvastatin","albuterol","Nexium","Naproxen","Clonazepam","Pantoprazole","Prednisone") 
        comNameTablet.grid(row=0,column=1) 
                                                                     
        #============lable for refence no.:-=================
        lblref=Label(Dataframeleft,font=("arial",12,"bold"),text="Refence No:-",padx=2)
        lblref.grid(row=1,column=0,sticky=W) 
        txtref=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1) 
        #==================lable for Dose============
        lblDose=Label(Dataframeleft,font=("arial",12,"bold"),text="Dose:-",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W) 
        txtDose=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1) 
#================lable for no of tablets ===============
        lblNooftablets=Label(Dataframeleft,font=("arial",12,"bold"),text="No of Tablets:-",padx=2,pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W) 
        txtNooftablets=Entry(Dataframeleft,textvariable=self.NumberofTablets,font=("arial",12,"bold"),width=35)
        txtNooftablets.grid(row=3,column=1) 
        #======= lable for No of lots========================#
        lblLot=Label(Dataframeleft,font=("arial",12,"bold"),text="Lot:-",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W) 
        txtLot=Entry(Dataframeleft,textvariable=self.Lot,font=("arial",12,"bold"),width=35)
        txtLot.grid(row=4,column=1) 
#=================lable for Issue dates===================
        lblissueDate=Label(Dataframeleft,font=("arial",12,"bold"),text="Issue Date:-",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W) 
        txtissueDate=Entry(Dataframeleft,textvariable=self.Issuedate,font=("arial",12,"bold"),width=35)
        txtissueDate.grid(row=5,column=1) 

        #=================ExpDate Lable+++++++++++++++++
        lblExpDate=Label(Dataframeleft,font=("arial",12,"bold"),text="Exp Date:-",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W) 
        txtExpDate=Entry(Dataframeleft,textvariable=self.ExpDate,font=("arial",12,"bold"),width=35)
        txtExpDate.grid(row=6,column=1) 

    #+++++++++++++++++++++++++lable for Daily Dose++++++++++++++++++++++
        lblDailyDose=Label(Dataframeleft,font=("arial",12,"bold"),text="Daily Dose:-",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W) 
        txtDailyDose=Entry(Dataframeleft,textvariable=self.DailyDose,font=("arial",12,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1) 

        #=======================Side Effect Lable+++++++++++++++++++++++++++++++++++++++++++++
        lblSideEffect=Label(Dataframeleft,font=("arial",12,"bold"),text="Side Effect:-",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W) 
        txtSideEffect=Entry(Dataframeleft,textvariable=self.sideEfect,font=("arial",12,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1) 
#========================lable for Futher Information==============
        lblFurtherinfo=Label(Dataframeleft,font=("arial",12,"bold"),text="Further Information",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W) 
        txtFurtherinfo=Entry(Dataframeleft,textvariable=self.FurtherInformation,font=("arial",12,"bold"),width=35)
        txtFurtherinfo.grid(row=0,column=3) 
#=======================lable for Blood Preessure++++++++++++++++
        lblBloodPressure=Label(Dataframeleft,font=("arial",12,"bold"),text="Blood Pressure",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W) 
        txtBloodPress=Entry(Dataframeleft,textvariable=self.Booldp,font=("arial",12,"bold"),width=35)
        txtBloodPress.grid(row=1,column=3) 


        #===============Storage Advice ++++++++++=====
        lblStorage=Label(Dataframeleft,font=("arial",12,"bold"),text="Storage Advice",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W) 
        txtStorage=Entry(Dataframeleft,textvariable=self.StorageAdvice,font=("arial",12,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        #===================Medication lable===========
        lblMedicine=Label(Dataframeleft,font=("arial",12,"bold"),text="Medication",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W) 
        txtMedicine=Entry(Dataframeleft,textvariable=self.HowToUseMedication,font=("arial",12,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)
        #==================Patient Id+++++++++++
        lblPatientId=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient ID:-",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W) 
        txtPatientId=Entry(Dataframeleft,textvariable=self.PatientId,font=("arial",12,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)
 #===============Nhs Number +++++++++++++++++
        lblNhsNumber=Label(Dataframeleft,font=("arial",12,"bold"),text="NHS Number:-",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W) 
        txtNhsNumber=Entry(Dataframeleft,textvariable=self.nhsNumber,font=("arial",12,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)
        #==============Patient Name+++++++++++++++
        lblPatientName=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient Name:-",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W) 
        txtPatientName=Entry(Dataframeleft,textvariable=self.PatientName,font=("arial",12,"bold"),width=35)
        txtPatientName.grid(row=6,column=3)

        #==================patient Date of Birth lable ================
        lblDateofBirth=Label(Dataframeleft,font=("arial",12,"bold"),text="Date of Birth",padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W) 
        txtDateofBirth=Entry(Dataframeleft,textvariable=self.DateofBirth,font=("arial",12,"bold"),width=35)
        txtDateofBirth.grid(row=7,column=3)
        #==============Patient Addresss lable ========================================
        lblPatientAddress=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient Address",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W) 
        txtPatientAddress=Entry(Dataframeleft,textvariable=self.PatientAddress,font=("arial",12,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)






#=========================DataFrameRight+++++++++++++++++++++++++++==
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


        #================================Buttons+++++++++++++++++++++++========
        btnPrescription=Button(Buttonframe,text="Presciption",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=14,padx=2,pady=6, command = self.button_click)
        btnPrescription.grid(row=0,column=0)
       


        btnPrescriptionData=Button(Buttonframe,text="Presciption Data",bg="green",fg="white",font=("arial",12,"bold"),width=26,height=14,padx=2,pady=6,command = self.button_click)
        btnPrescriptionData.grid(row=0,column=1)


        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=26,height=14,padx=2,pady=6,command = self.button_click)
        btnUpdate.grid(row=0,column=2)


        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=26,height=14,padx=2,pady=6,command = self.button_click)
        btnDelete.grid(row=0,column=3)


        btnClear=Button(Buttonframe,text="clear",bg="green",fg="white",font=("arial",12,"bold"),width=26,height=14,padx=2,pady=6,command = self.button_click)
        btnClear.grid(row=0,column=4)



        btnExit=Button(Buttonframe,text="Exit",bg="black",fg="white",font=("arial",12,"bold"),width=26,height=14,padx=2,pady=6,command = self.button_click)
        btnExit.grid(row=0,column=5)
#===========================Table++++++++++++++++++++++++
##############################Scrolbar++++++++++++++++++++
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablet","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","dob","pname","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("nameoftablet",text="Name of Tablet")
        self.hospital_table.heading("ref",text="Reference No:-")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("Address",text="Address")
        self.hospital_table.heading("dob",text="DOB")

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("Address",width=100)
        self.hospital_table.column("dob",width=100)





############################function Declration#####################################


    def iPrescriptionData(self):
        if self.nameoftablet.get()=="" or self.ref.get()=="":
              messagebox.showerror("Error","All field are reuired")
        else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ar#12345",database="Mydata")
                my_cursor=conn.cursor()
                my_cursor.excute("insert into hospital")





    def button_click(self):
        print("button was clicked")

        



root=Tk()
ob=Hospital(root)
root.mainloop()
