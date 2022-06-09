from tkinter import *
from tkinter import ttk
from  tkinter import messagebox
import sqlite3

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Inventory Management System | Created by Manish")
        self.root.geometry("1350x700+0+0")
        root.configure(bg='#FFFFFF')      
      
        title = Label(self.root , text="Students Management System" ,bd=10 , relief=GROOVE, font=("times",50,"bold"), bg="#6200ee", fg="white")
        title.pack(side=TOP, fill = X)
#=======================================================All variable ==========================================================#

        self.Roll_no_var = StringVar()  
        self.Name_var = StringVar()       
        self.Email_var = StringVar() 
        self.gender_var = StringVar() 
        self.contract_var = StringVar() 
        self.dob_var = StringVar()    
        self.txt_address = StringVar()
        
        self.search_by = StringVar() 
        self.search_txt = StringVar()
       
        
    #==============================Manage Frame===========================================#   
        Manage_Frame = Frame(self.root, bd=4 , relief=GROOVE,bg="white")
        Manage_Frame.place(x=20 , y=120 , width=450, height=690)
        m_title = Label(Manage_Frame , text = "Manage students",fg='black', font=("times",30,"bold"))
        m_title.grid(row=0 , columnspan=2 , pady=20)
        
        lbl_rool = Label(Manage_Frame , text="Roll no."  , font=("times",20 , "bold"), fg="black" , bg="white")
        lbl_rool.grid(row=1 , column=0 , pady=10 , padx=20, sticky='w')
        txt_rool = Entry(Manage_Frame,textvariable=self.Roll_no_var,width=25,  font=("times",16 ), bg="white", fg="black" ,bd=5 , relief=GROOVE)
        txt_rool.grid(row=1 , column=1 , pady=10 , padx=0, sticky='w')
        
        lbl_Name = Label(Manage_Frame , text="Name"  , font=("times",20 , "bold"), fg="black" ,bg="white")
        lbl_Name.grid(row=2 , column=0 , pady=10 , padx=20, sticky='w')
        txt_Name = Entry(Manage_Frame,textvariable=self.Name_var ,width=25, font=("times",16 ), bg="white", fg="black" ,bd=5 , relief=GROOVE)
        txt_Name.grid(row=2, column=1 , pady=10 , padx=0, sticky='w')
        
        
        lbl_Email = Label(Manage_Frame , text="Email"  , font=("times",20 , "bold"), fg="black" ,bg="white")
        lbl_Email.grid(row=3 , column=0 , pady=10 , padx=20, sticky='w')
        txt_Email = Entry(Manage_Frame,textvariable=self.Email_var,width=25,font=("times",16 ), bg="white", fg="black" ,bd=5 , relief=GROOVE)
        txt_Email.grid(row=3 , column=1 , pady=10 , padx=0, sticky='w')
        
        
        lbl_Gender = Label(Manage_Frame , text="Gender"  , font=("times",20 , "bold"), fg="black",bg="white")
        lbl_Gender.grid(row=4 , column=0 , pady=10 , padx=20, sticky='w')

        combo_gender = ttk.Combobox(Manage_Frame ,textvariable=self.gender_var,width=24, font=("times",17), state="readonly")
        combo_gender['values'] =("Male", "Female" , "Other")
        combo_gender.grid(row=4 , column=1 , pady=10,)



        lbl_contract = Label(Manage_Frame , text="contact"  , font=("times",20 , "bold"), fg="black",bg="white")
        lbl_contract.grid(row=5 , column=0 , pady=10 , padx=20, sticky='w')
        txt_contract = Entry(Manage_Frame,textvariable=self.contract_var,  font=("times",16 ),width=25, bg="white", fg="black" ,bd=5 , relief=GROOVE)
        txt_contract.grid(row=5 , column=1 , pady=10 , padx=0, sticky='w')
        
        
        lbl_DOB = Label(Manage_Frame , text="D.O.B"  , font=("times",20 , "bold"), fg="black",bg="white")
        lbl_DOB.grid(row=6 , column=0 , pady=10 , padx=20, sticky='w')
        txt_DOB = Entry(Manage_Frame, textvariable=self.dob_var, font=("times",16 ),width=25, bg="white", fg="black" ,bd=5 , relief=GROOVE)
        txt_DOB.grid(row=6 , column=1 , pady=10 , padx=0, sticky='w')
        
        
        lbl_address = Label(Manage_Frame , text="address"  , font=("times",20 , "bold"), fg="black",bg="white")
        lbl_address.grid(row=7 , column=0 , pady=10 , padx=20, sticky='w')
        
        
        txt_address = Entry(Manage_Frame ,textvariable=self.txt_address, width=35 ,  bd=4,relief=GROOVE)
        txt_address.grid(row=7 , column=1 , pady=10 , padx=0, sticky='w')
        
        
        tm_Frame = Frame(self.root, bd=4 , relief=GROOVE)
        tm_Frame.place(x=20 , y=723 , width=450, height=70)
        
        m_title = Label(tm_Frame , text = "-----------Tearms and Condition applied------------",fg='black', font=("times",16,"bold"))
        m_title.grid(row=0 , columnspan=2 , pady=20)
        
        
#=======================================button frame=============================================================#        
        btn_frame = Frame(Manage_Frame, bd=4 , relief=GROOVE)
        btn_frame.place(x=10 , y=530 , width=420)
        
        Add_btn = Button(btn_frame , font=("times" ,12, "normal"),text = "Add" , width =8 ,bg="#03dac4" ,bd=2, relief=RIDGE, fg="black",command= self.add_Student).grid(row=0, column=0 , padx=9, pady=10)
        Update_btn = Button(btn_frame ,font=("times" ,12, "normal"), text = "Update",bg="#03dac4" , bd=2, relief=RIDGE,fg="black", command=self.update_data,width =8).grid(row=0, column=1 , padx=9 , pady=10)
        Delete_btn = Button(btn_frame ,font=("times" ,12, "normal"), text = "Delete" ,bg="#03dac4" ,bd=2, relief=RIDGE, fg="black",command=self.Delete_data, width =8).grid(row=0, column=2 , padx=9, pady=10)
        Clear_btn = Button(btn_frame ,font=("times" ,12, "normal"), text = "Clear" ,bg="#03dac4" , bd=2, relief=RIDGE,fg="black",command=self.clear, width =8).grid(row=0, column=3 , padx=9 , pady=10)
    #==============================detail frame===========================================#   
        Detail_Frame = Frame(self.root, bd=4 , relief=GROOVE)
        Detail_Frame.place(x=500 , y=120 , width=1010, height=690)
        
        lbl_search = Label(Detail_Frame , text="Search By"  , font=("roman",20 , "bold"), fg="black")
        lbl_search.grid(row=0 , column=0 , pady=10 , padx=20, sticky='w')
        
    
        combo_search = ttk.Combobox(Detail_Frame ,textvariable=self.search_by,width=10, font=("roman",15), state="readonly")
        combo_search['values'] =("Roll_no", "Name", "Email" , "dob","gender" )
        combo_search.grid(row=0 , column=1 , pady=10)
        
        txt_Search = Entry(Detail_Frame,textvariable=self.search_txt,  font=("roman ",18 ),width=25, bg="white", fg="black" ,bd=5 , relief=GROOVE)
        txt_Search.grid(row=0 , column=2 , pady=10 , padx=10, sticky='w')
        
        Search_btn = Button(Detail_Frame,command=self.search_data , font=("roman ",10) ,bg="#03dac4" ,bd=2, relief=GROOVE, fg="black", text = "Search" , width =10 , pady=10).grid(row=0, column=3 , padx=10, pady=10)
        showal_btn = Button(Detail_Frame , command=self.fetch_data, font=("roman ",10) ,bg="#03dac4" ,bd=2, relief=GROOVE, fg="black",text = "Show All" , width =10 , pady=10).grid(row=0, column=4 , padx=10 , pady=50)
        Delete_btn = Button(Detail_Frame , command=self.Delete_data, font=("roman ",10) ,bg="#03dac4" ,bd=2, relief=GROOVE, fg="black",text = "Delete" , width =10, pady=10).grid(row=0, column=5 , padx=10 , pady=50)
        
      #==============================Table frame===========================================#   
        Table_Frame = Frame(Detail_Frame, bd=4 , relief=GROOVE)
        Table_Frame.place(x=10 , y=120 , width=970, height=540)
        
        scrool_x = Scrollbar(Table_Frame , orient=HORIZONTAL)
        scrool_y = Scrollbar(Table_Frame , orient=VERTICAL)
        self.Students_Table = ttk.Treeview(Table_Frame , columns=("roll" , "name" , "Email", "gender" ,"contract" , "dob" ,"address"), xscrollcommand=scrool_x.set , yscrollcommand=scrool_y.set)      
        scrool_x.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)
        scrool_x.config(command=self.Students_Table.xview)     
        scrool_y.config(command=self.Students_Table.yview)   
        self.Students_Table.heading("roll" , text="Roll No.")
        self.Students_Table.heading("name" , text="Name")
        self.Students_Table.heading("Email" , text="Email")
        self.Students_Table.heading("contract" , text="Contract")
        self.Students_Table.heading("dob" , text="D.O.B")
        self.Students_Table.heading("gender" , text="Gender")
        self.Students_Table.heading("address" , text="address")
        
        self.Students_Table.column("roll" , width="50")
        self.Students_Table.column("name" , width="100")
        self.Students_Table.column("Email" , width="150")
        self.Students_Table.column("contract" , width="120")
        self.Students_Table.column("dob" , width="100")
        self.Students_Table.column("gender" , width="100")
        self.Students_Table.column("address" , width="270")
        
        
        
        
        
        self.Students_Table.pack(fill=BOTH , expand=1)
        self.Students_Table.bind("<ButtonRelease-1>",self.get_cursor)
         
        self.Students_Table['show']='headings'
        self.Students_Table.pack()
        self.fetch_data()
        
        
    def add_Student(self ) :
       
           con = sqlite3.connect('stm.db')
           
           cur = con.cursor()
              
           cur.execute("INSERT INTO students (roll,name,email,gender,contact,dob,addres) VALUES (? , ? , ? , ?,?,?,?)",
                       ((self.Roll_no_var.get(), self.Name_var.get(), self.Email_var.get() , self.gender_var.get(), self.contract_var.get() , self.dob_var.get(), self.txt_address.get()  )))
      
           
                
           con.commit()
           self.fetch_data()
           self.clear()
           con.close()
           messagebox.showinfo("Success" ,"Record has been successfully added")
       
    def  fetch_data(self):
        con = sqlite3.connect('stm.db')
        cur = con.cursor()
                  
        cur.execute("select * from students ")
        rows =cur.fetchall()
        if len(rows)!=0:
            self.Students_Table.delete(*self.Students_Table.get_children())
            for row in rows:
                self.Students_Table.insert('' , END , values=row)

            con.commit()
            con.close()
        
    def clear(self):
                self.Roll_no_var.set(''), 
                self.Name_var.set('') ,     
                self.Email_var.set(''),
                self.gender_var.set(''),
                self.contract_var.set(''),
                self.dob_var.set('')  , 
                self.txt_address.set('')
        
    def get_cursor(self , ev):
        cursor_row = self.Students_Table.focus()    
        content = self.Students_Table.item(cursor_row)
        row=content['values']
        self.Roll_no_var.set(row[0]), 
        self.Name_var.set(row[1]),     
        self.Email_var.set(row[2]), 
        self.gender_var.set(row[3]),
        self.contract_var.set(row[4]),
        self.dob_var.set(row[5]), 
        self.txt_address.set(row[6])
        
    def update_data(self):
        con = sqlite3.connect('stm.db')
        cur = con.cursor()
        cur.execute("update students set name=?, email=?, gender=? , contact=? , dob=? , addres= ? WHERE roll = ?",( 
        self.Name_var.get(),     
        self.Email_var.get(), 
        self.gender_var.get(),
        self.contract_var.get(),
        self.dob_var.get(), 
        self.txt_address.get(), 
        self.Roll_no_var.get()   
        ))                                                                                   

        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("Success" ,"Record has been successfully updated")    
    def  Delete_data(self):
        con = sqlite3.connect('stm.db')
        cur = con.cursor()
              
        query= ("DELETE FROM students WHERE  roll= ?" )
        
        cur.execute(query, (self.Roll_no_var.get(),))
   
      
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        
           
    def  search_data(self):
        con = sqlite3.connect('stm.db')
        cur = con.cursor()
                
        cur.execute("select * from students where " + str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows =cur.fetchall()
        if len(rows)!=0:
            self.Students_Table.delete(*self.Students_Table.get_children())
            for row in rows:
                self.Students_Table.insert('' , END , values=row)

            con.commit()
            con.close()  
            
    
root = Tk()
ob =Student(root)
root.mainloop()