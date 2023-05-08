from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont

def mainwindow():
    root = Tk()
    w = 1080
    h = 800
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
    global fullfram,userinfo,pwdinfo
    userinfo = StringVar()
    pwdinfo = StringVar()       

    fullfram = Frame(root,bg='#ff6b1e')
    fullfram.rowconfigure((0,1,2,3),weight=1)
    fullfram.columnconfigure((0,1,2,3),weight=1)
    
    rigt_frame = Frame(fullfram,bg='#ff6b1e')
    rigt_frame.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
    rigt_frame.columnconfigure((0,1,2,3,4,5),weight=1)


    Label(rigt_frame,image=pic).grid(row=0,column=0,rowspan=10,columnspan=7,sticky=NSEW)
    Label(rigt_frame,text='Login',font='Helvetica 38 bold',fg='#ffffff',bg='#ff6b1e').grid(row=2,column=5,sticky=NW)
    Label(rigt_frame,text='Username',font='Helvetica 14 bold',fg='#ffffff',bg='#ff6b1e').grid(row=2,column=5,sticky=SW)
    userentry = Entry(rigt_frame,bg='#E4FBFF',fg='#000000',width=20,textvariable=userinfo)
    userentry.grid(row=3,column=5,columnspan=2,sticky=NW)
    Label(rigt_frame,text='Password',font='Helvetica 14 bold',fg='#ffffff',bg='#ff6b1e').grid(row=3,column=5,sticky=SW)
    pwdentry = Entry(rigt_frame,bg='#E4FBFF',fg='#000000',width=20,textvariable=pwdinfo)
    pwdentry.grid(row=4,column=5,columnspan=2,sticky=NW)

    Button(rigt_frame,text='Login ',width=17, relief=FLAT,bg='#ffa82b',fg='#000000',borderwidth=5,bd=3).grid(row=5,column=5,columnspan=2,sticky=NW)


    Label(rigt_frame,text="Don't have an account? ",font='Helvetica 14 bold',fg='#ffffff',bg='#ff6b1e',activebackground='#ff6b1e').grid(row=6,column=5,sticky=SW,padx=20)
    Button(rigt_frame,text='Register Now',bg='#ff6b1e',relief="flat",fg='#ffa82b',font='Helvetica 14 bold underline').grid(row=7,column=5,columnspan=4,sticky=NW,padx=60)

    rigt_frame.grid(row=0,column=0,columnspan=4,rowspan=4,sticky=NSEW)
    fullfram.grid(row=0,column=0,columnspan=4,rowspan=4,sticky=NSEW)



root = mainwindow()

pic = PhotoImage(file='image\\Untitled-1.png').subsample(1,1)
but_1 = PhotoImage(file='image\\buttom.png').subsample(1,1)


loginlayout()
root.mainloop()                                                                                                                                                                                                                                