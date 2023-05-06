from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def mainwindow():
    root = Tk()
    w = 1080
    h = 1920
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#ADD8E6')
    root.title("Login Application: ")
    root.option_add('*font',"Helvetica 18 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginlayout() :
    global loginframe,userinfo,pwdinfo,userentry,pwdentry
    userinfo = StringVar()
    pwdinfo = StringVar()

    fullfram = Frame(root,bg='#28527A')
    fullfram.rowconfigure((0,1,2,3),weight=1)
    fullfram.columnconfigure((0,1,2,3),weight=1)
    loginframe = Frame(fullfram,bg='#709FB0')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1,2),weight=1)
    
    Label(loginframe,font="Garamond 26 bold",bg='#709FB0').grid(row=0,columnspan=4)
    Label(loginframe,text='Accoount Login',fg='#ffffff',bg='#709FB0').grid(row=1,columnspan=4)
    Label(loginframe,text="Username :",bg='#709FB0',fg='#ffffff').grid(row=2,column=1,sticky=E)
    Label(loginframe,text="Password :",bg='#709FB0',fg='#ffffff').grid(row=3,column=1,sticky=E)
    userentry = Entry(loginframe,bg='#E4FBFF',fg='#000000',width=20,textvariable=userinfo)
    pwdentry = Entry(loginframe,bg='#E4FBFF',fg='#000000',width=20,show='*',textvariable=pwdinfo)
    userentry.grid(row=2,column=2,sticky='w',padx=20)
    pwdentry.grid(row=3,column=2,sticky='w',padx=20)
    Button(loginframe,text="Exit",width=7,command=quit).grid(row=4,column=0,columnspan=2,pady=20,ipady=5)
    Button(loginframe,text='Login',bg="#90EE90",width=7).grid(row=4,column=2,columnspan=2,pady=20,ipady=5,sticky=E,padx=20)
    fullfram.grid(row=0,column=0,columnspan=4,rowspan=4,sticky=NSEW)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    userentry.focus_force()


root = mainwindow()

loginlayout()
root.mainloop()