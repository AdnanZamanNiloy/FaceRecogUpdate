from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
# #import mysql.connector
import cv2



class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        # first image
        img = Image.open(r"F:\Desktop\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_18-31-16.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)
        
        # second image
        img1 = Image.open(r"F:\Desktop\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_18-31-23.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)
        
        # bg image
        img3 = Image.open(r"F:\Desktop\Face Recognation Project\Face_Recog_Images\synthetic-data-scaled.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 27, "bold"), bg="blue", fg="white")
        title_lbl.place(x=-3, y=0, width=1530, height=35)
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=12, y=45, width=1500, height=600)
        
        #Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=580)
        
        img_left = Image.open(r"F:\Desktop\Face Recognation Project\Face_Recog_Images\photo_2024-12-12_18-31-29.jpg")
        img_left = img_left.resize((655, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=1, y=0, width=655, height=130)
        
        #left inside frame
        left_inside_frame = Frame(Left_frame, bd=2, bg="white", relief=RIDGE)
        left_inside_frame.place(x=4, y=135, width=648, height=418)
        
        #labelend entry
        #attendance id
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        attendanceId_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        #Name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        name_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        #Department
        department_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        department_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
        #Reg No
        regNo_label = Label(left_inside_frame, text="Reg No:", font=("times new roman", 12, "bold"), bg="white")
        regNo_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        regNo_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))

        regNo_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        #Date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        date_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        date_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        #Time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        time_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        #Attendance Status
        attendanceStatus_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendanceStatus_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        self.atten_status = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), state="readonly", width=18)
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        #buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE ,bg="white")
        btn_frame.place(x=0, y=380, width=644, height=30)
        
        save_btn = Button(btn_frame, text="Import csv", font=("times new roman", 10, "bold"), bg="blue", fg="white", width=22)
        save_btn.grid(row=0, column=0)
        
        update_btn = Button(btn_frame, text="Export.csv", font=("times new roman", 10, "bold"), bg="blue", fg="white", width=22)
        update_btn.grid(row=0, column=1)
        
        delete_btn = Button(btn_frame, text="Delete", font=("times new roman", 10, "bold"), bg="blue", fg="white", width=22)
        delete_btn.grid(row=0, column=2)
        
        reset_btn = Button(btn_frame, text="Reset", font=("times new roman", 10, "bold"), bg="blue", fg="white", width=22)
        reset_btn.grid(row=0, column=3)
        
        #Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=805, height=580)
        
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=790, height=540)
        
        #==========scroll bar table============
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "name", "Date","department", "regNo", "time", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("regNo", text="Reg No")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("attendance", text="Attendance Status")
        
        self.AttendanceReportTable["show"] = "headings"
        
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("Date", width=100)
        self.AttendanceReportTable.column("department", width=100)

        self.AttendanceReportTable.column("regNo", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
