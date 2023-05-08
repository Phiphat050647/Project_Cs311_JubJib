import sqlite3
from tkinter import *
from tkinter import messagebox

def creatconnection():
    global conn,cursor
    conn = sqlite3.connect('JukJik_database.db')
    cursor = conn.cursor()

def mainwindow():
    root = Tk()
    w = 375
    h = 812
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#1D708B')
    root.title("Login Application: ")
    root.option_add('*font',"Helvetica 18 bold")
    root.rowconfigure((0),weight=1)
    root.columnconfigure((0),weight=1)
    canvas = Canvas(root,width=375,height=812)
    canvas.place(x=0,y=0)
    
    return root

def firt_pace() :
    global splash_page
    splash_page = Frame(root,bg='#ffffff')
    splash_page.grid(row=0,column=0,sticky=NSEW)
    Button(splash_page,relief=FLAT,image=bg_firt,command=pag_login).grid(row=0,column=0,sticky=NSEW)

def buttom_all():
    print('Hello')
    global buttom_click_login,buttom_click_pag2,buttom_click_register,buttom_signup

    def buttom_click_login(x,y):
        global Label_buttom

        Label_buttom = Label(splash_page,relief=FLAT,image=buttom_login,width=327,height=62,bg='#ffffff',border=0)
        Label_buttom.place(x=x,y=y)
        def on_enter(e):
            Label_buttom.config(cursor='hand2')
            buttom_login.configure(file='image_2\\buttom_act_login.png')
        def on_leave(e):
            buttom_login.configure(file='image_2\\buttom_login.png')
        Label_buttom.bind("<Enter>",on_enter)
        Label_buttom.bind("<Leave>",on_leave)
        Label_buttom.bind("<Button-1>", loginclick)

    def buttom_click_register(x,y):
        global Label_buttom

        Label_buttom = Label(splash_page,relief=FLAT,image=buttom_register,width=327,height=62,bg='#ffffff',border=0)
        Label_buttom.place(x=x,y=y)
        def on_enter(e):
            Label_buttom.config(cursor='hand2')
            buttom_register.configure(file='image_2\\register_buttom_act.png')
        def on_leave(e):
            buttom_register.configure(file='image_2\\register_buttom.png')
        Label_buttom.bind("<Enter>",on_enter)
        Label_buttom.bind("<Leave>",on_leave)
        Label_buttom.bind("<Button-1>", register)
    
    def buttom_click_pag2(x,y):
        global Label_buttom
        Label_buttom = Label(splash_page,relief=FLAT,image=buttom_image,width=327,height=62,bg='#ffffff',border=0)
        Label_buttom.place(x=x,y=y)
        def on_enter(e):
            Label_buttom.config(cursor='hand2')
            buttom_image.configure(file='image_2\\buttom_act.png')
        def on_leave(e):
            buttom_image.configure(file='image_2\\buttom.png')
        Label_buttom.bind("<Enter>",on_enter)
        Label_buttom.bind("<Leave>",on_leave)
        Label_buttom.bind("<Button-1>", pag3)

    def buttom_signup(x,y):
        global Label_buttom

        Label_buttom = Label(splash_page,relief=FLAT,image=buttom_register,width=327,height=62,bg='#ffffff',border=0)
        Label_buttom.place(x=x,y=y)
        def on_enter(e):
            Label_buttom.config(cursor='hand2')
            buttom_register.configure(file='image_2\\register_buttom_act.png')
        def on_leave(e):
            buttom_register.configure(file='image_2\\register_buttom.png')
        Label_buttom.bind("<Enter>",on_enter)
        Label_buttom.bind("<Leave>",on_leave)
        Label_buttom.bind("<Button-1>", registration_data)


def register(event):
    Label(splash_page,relief=FLAT,image=bg_signup).place(x=-1,y=-1)
    global name,gmail,password,password_cf
    def name_on_enter(e):
        name.delete(0,'end')
    def name_on_leave(e):
        if name.get()=="":
            name.insert(0,'john wick')
    
    def gmail_on_enter(e):
        gmail.delete(0,'end')
    def gmail_on_leave(e):
        if gmail.get()=="":
            gmail.insert(0,'example@gmail.com')

    def pass_on_enter(e):
        password.delete(0,'end')
    def pass_on_leave(e):
        if password.get()=="":
            password.insert(0,' **********')
    
    def pass_cf_on_enter(e):
        password_cf.delete(0,'end')
    def pass_cf_on_leave(e):
        if password_cf.get()=="":
            password_cf.insert(0,' **********')

    name = Entry(splash_page,width=23,fg='#646464',border=0,bg='#f0f5fa')
    name.place(x=32,y=279)
    name.insert(0, 'john wick')
    name.bind("<FocusIn>",name_on_enter)
    name.bind("<FocusOut>",name_on_leave)
    
    gmail = Entry(splash_page,width=23,fg='#646464',border=0,bg='#f0f5fa')
    gmail.place(x=32,y=390)
    gmail.insert(0, 'example@gmail.com')
    gmail.bind("<FocusIn>",gmail_on_enter)
    gmail.bind("<FocusOut>",gmail_on_leave)

    password = Entry(splash_page,width=23,fg='#646464',border=0,bg='#f0f5fa')
    password.place(x=32,y=500)
    password.insert(0, ' **********')
    password.bind("<FocusIn>",pass_on_enter)
    password.bind("<FocusOut>",pass_on_leave)

    password_cf = Entry(splash_page,width=23,fg='#646464',border=0,bg='#f0f5fa')
    password_cf.place(x=32,y=610)
    password_cf.insert(0, ' **********')
    password_cf.bind("<FocusIn>",pass_cf_on_enter)
    password_cf.bind("<FocusOut>",pass_cf_on_leave)
    buttom_signup(24,710)

def registration_data() :
    if name.get() == '':
        messagebox.showwarning('Admin:','Please enter firstname')
        name.focus_force()
    elif gmail.get() == '' :
        messagebox.showwarning('Admin:','Please enter lastname')
        gmail.focus_force()
    elif password.get() == '':
        messagebox.showwarning('Admin:','Please select year')
        password.focus_force()
    elif password_cf.get() == '':
        messagebox.showwarning('Admin:','Please select year')
        password_cf.focus_force()
    elif len(password.get()) == 10 and password.get().isdigit() :
        if password.get() == password_cf.get():
            ins_sql = "INSERT INTO students VALUES(?,?,?,?,?,?,?)"
            param = [name.get(),gmail.get(),password.get()]
            cursor.execute(ins_sql,param)
            conn.commit()
            retrivedata()
            messagebox.showinfo("Admin","Registration Successfully")


        

    

    

def pag_login():
    Label(splash_page,relief=FLAT,image=login_pag).place(x=-1,y=-1)
    global gmail,password
    def gmail_on_enter(e):
        gmail.delete(0,'end')
    def gmail_on_leave(e):
        if gmail.get()=="":
            gmail.insert(0,'example@gmail.com')
    
    def password_on_enter(e):
        password.delete(0,'end')
    def password_on_leave(e):
        if password.get()=="":
            password.insert(0,'*******')

    gmail = Entry(splash_page,width=25,fg='#646464',border=0,bg='#f0f5fa')
    gmail.place(x=30,y=287)
    gmail.insert(0, 'example@gmail.com')
    gmail.bind("<FocusIn>",gmail_on_enter)
    gmail.bind("<FocusOut>",gmail_on_leave)
    
    password = Entry(splash_page,width=25,fg='#646464',border=0,bg='#f0f5fa')
    password.place(x=30,y=400)
    password.insert(0, '*************')
    password.bind("<FocusIn>",password_on_enter)
    password.bind("<FocusOut>",password_on_leave)
    buttom_click_login(24,530)
    Label(splash_page,text='----------------- or -----------------',fg='#646464',bg='#ffffff').place(x=30,y=620)
    buttom_click_register(24,680)
    

def loginclick(event) :
    global user_result

    if gmail.get() == "" :
        messagebox.showwarning("Admin:","Please enter Username")
        gmail.focus_force()
    else :
        sql = "select * from login where user_gmail=?"
        cursor.execute(sql,[gmail.get()])
        result = cursor.fetchall()
        if result :
            if password.get() == "" :
                messagebox.showwarning("Admin:","Please enter password")
                password.focus_force()
            else :
                sql = "select * from login where user_gmail=? and password=? "
                cursor.execute(sql,[gmail.get(),password.get()])   #case1
                user_result = cursor.fetchone()
                if user_result :
                    messagebox.showinfo("Admin:","Login Successfully")
                    print(user_result)
                    gmail.delete(0,END)
                    password.delete(0,END)
                    page_2()
                else :
                    messagebox.showerror("Admin:","Username or Password is invalid.")
                    gmail.select_range(0,END)
                    password.focus_force()
        else :
            messagebox.showerror("Admin:","Username not found\nPlease register before Login")
            gmail.select_range(0,END)
            gmail.focus_force()

def page_2():
    Label(splash_page,relief=FLAT,image=page2).grid(row=0,column=0,sticky=NSEW)
    buttom_click_pag2(24,675)

def pag3(event):
        Label(splash_page,relief=FLAT,image=page3).grid(row=0,column=0,sticky=NSEW)
        


def retrivedata() :
    sql = "select * from students"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)

print('ok')
print('5555')

print('5555')
creatconnection()
root = mainwindow()

logo = PhotoImage(file='image_2\logo jukjik 02.png').subsample(3,3)
bg_firt = PhotoImage(file='image_2\Bg_firt.png').subsample(1,1)
bg_signup = PhotoImage(file='image_2\\bg_signup.png').subsample(1,1)
page2 = PhotoImage(file='image_2\page_2.png').subsample(1,1)
page3 = PhotoImage(file='image_2\page_3.png').subsample(1,1)
buttom_image = PhotoImage(file='image_2\\buttom.png')
buttom_login = PhotoImage(file='image_2\\buttom_login.png')
buttom_register = PhotoImage(file='image_2\\register_buttom.png')
login_pag = PhotoImage(file='image_2\loing.png')

firt_pace()
buttom_all()
root.mainloop()

