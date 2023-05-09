import sqlite3
from tkinter import *
from tkinter import messagebox

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





def home1():
    splash_page = Frame(root,bg='#ffffff')
    splash_page.grid(row=0,column=0,sticky=NSEW)
    Label(splash_page,relief=FLAT,image=home_v1,width=375,height=812).grid(row=0,column=0,sticky=NSEW)
    scoll = Scrollbar(splash_page, orient= 'vertical')
    scoll.place(relx= 1 , rely= 0,relheight=1,anchor=NE)



root = mainwindow()
home1()
logo = PhotoImage(file='image_2\logo jukjik 02.png').subsample(3,3)
bg_firt = PhotoImage(file='image_2\Bg_firt.png').subsample(1,1)
bg_signup = PhotoImage(file='image_2\\bg_signup.png').subsample(1,1)
page2 = PhotoImage(file='image_2\page_2.png').subsample(1,1)
page3 = PhotoImage(file='image_2\page_3.png').subsample(1,1)
buttom_image = PhotoImage(file='image_2\\buttom.png')
buttom_login = PhotoImage(file='image_2\\buttom_login.png')
buttom_register = PhotoImage(file='image_2\\register_buttom.png')
buttom_back = PhotoImage(file='image_2\\buttom_back.png')
login_pag = PhotoImage(file='image_2\loing.png')
home_v1 = PhotoImage(file='image_2\Home_1.png')
root.mainloop()