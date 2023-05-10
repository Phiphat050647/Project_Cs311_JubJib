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

def buttom_revese(event):
    canvas_1.destroy()
    in_shop_page.destroy()
    in_shop.destroy()
    home1()

def in_shop_3(event):
    global canvas_1,in_shop_page,in_shop

    print('ok 2')
    canvas.destroy()
    Label_buttom.destroy()
    home_1.destroy()

    canvas_1 = Canvas(root, bg='yellow',width=375, height=1100, scrollregion=(0,0,375,1100))
    canvas_1.pack()
    in_shop_page = Frame(canvas_1,bg='#ffffff')

    canvas_1.create_window((0,0), window=in_shop_page, anchor=NW)

    in_shop = Label(in_shop_page,relief=FLAT,image=in_shop3,width=375,height=1100)
    in_shop.pack()
    
    in_shop.bind('<MouseWheel>', lambda event: canvas_1.yview_scroll(int(event.delta / 60), "units"))
    
    revese = Label(in_shop_page,relief=FLAT,image=buttom_back,width=45,height=45,bg='#ffffff',border=0)
    revese.place(x=29,y=17)
       
    def on_enter(e):
        revese.config(cursor='hand2')
    revese.bind("<Enter>",on_enter)
    revese.bind("<Button-1>", buttom_revese)


    in_shop_page.update_idletasks()
    canvas_1.config(scrollregion=canvas_1.bbox('all'))

def in_shop_2(event):
    global canvas_1,in_shop_page,in_shop
    print('ok 2')
    canvas.destroy()
    Label_buttom.destroy()
    home_1.destroy()
    canvas_1 = Canvas(root, bg='yellow',width=375, height=1500, scrollregion=(0,0,375,1500))
    canvas_1.pack()
    in_shop_page = Frame(canvas_1,bg='#ffffff')

    canvas_1.create_window((0,0), window=in_shop_page, anchor=NW)

    in_shop = Label(in_shop_page,relief=FLAT,image=in_shop2,width=375,height=1500)
    in_shop.pack()
    
    in_shop.bind('<MouseWheel>', lambda event: canvas_1.yview_scroll(int(event.delta / 60), "units"))

    revese = Label(in_shop_page,relief=FLAT,image=buttom_back,width=45,height=45,bg='#ffffff',border=0)
    revese.place(x=29,y=17)
       
    def on_enter(e):
        revese.config(cursor='hand2')
    revese.bind("<Enter>",on_enter)
    revese.bind("<Button-1>", buttom_revese)

    in_shop_page.update_idletasks()
    canvas_1.config(scrollregion=canvas_1.bbox('all'))

def in_shop_1(event):
    global canvas_1,in_shop_page,in_shop

    print('ok')
    canvas.destroy()
    Label_buttom.destroy()
    home_1.destroy()

    canvas_1 = Canvas(root, bg='yellow',width=375, height=1261, scrollregion=(0,0,375,1261))
    canvas_1.pack()
    in_shop_page = Frame(canvas_1,bg='#ffffff')

    canvas_1.create_window((0,0), window=in_shop_page, anchor=NW)

    in_shop = Label(in_shop_page,relief=FLAT,image=in_shop1,width=375,height=1261)
    in_shop.pack()
    
    in_shop.bind('<MouseWheel>', lambda event: canvas_1.yview_scroll(int(event.delta / 60), "units"))

    revese = Label(in_shop_page,relief=FLAT,image=buttom_back,width=45,height=45,bg='#ffffff',border=0)
    revese.place(x=29,y=17)
    def on_enter(e):
        revese.config(cursor='hand2')
    revese.bind("<Enter>",on_enter)

    revese.bind("<Button-1>", buttom_revese)

    in_shop_page.update_idletasks()
    canvas_1.config(scrollregion=canvas_1.bbox('all'))

def home1():
    global splash_page,canvas,home_1,Label_buttom
    canvas = Canvas(root, bg='yellow',width=375, height=853 ,scrollregion=(0,0,375,853))
    canvas.pack()
    splash_page = Frame(canvas,bg='#ffffff')
    canvas.create_window((0,0), window=splash_page, anchor=NW)

    home_1 = Label(splash_page,relief=FLAT,image=home_v1,width=375,height=853)
    home_1.pack()


    Label_buttom = Label(splash_page,relief=FLAT,image=shop_1,width=328,height=225,bg='#ffffff',border=0)
    Label_buttom.place(x=29,y=109)
    def on_enter(e):
        Label_buttom.config(cursor='hand2')
    Label_buttom.bind("<Enter>",on_enter)
    Label_buttom.bind("<Button-1>", in_shop_1)


    Label_buttom_2 = Label(splash_page,relief=FLAT,image=shop_2,width=328,height=225,bg='#ffffff',border=0)
    Label_buttom_2.place(x=29,y=361)
    def on_enter(e):
        Label_buttom_2.config(cursor='hand2')
    Label_buttom_2.bind("<Enter>",on_enter)
    Label_buttom_2.bind("<Button-1>", in_shop_2)


    Label_buttom_3 = Label(splash_page,relief=FLAT,image=shop_3,width=328,height=225,bg='#ffffff',border=0)
    Label_buttom_3.place(x=29,y=593)
    def on_enter(e):
        Label_buttom_3.config(cursor='hand2')
    Label_buttom_3.bind("<Enter>",on_enter)
    Label_buttom_3.bind("<Button-1>", in_shop_3)


    home_1.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(event.delta / 60), "units"))
    Label_buttom.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(event.delta / 60), "units"))
    Label_buttom_2.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(event.delta / 60), "units"))
    Label_buttom_3.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(event.delta / 60), "units"))
    splash_page.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

root = mainwindow()
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
home_v1 = PhotoImage(file='image_2\Home V_1.png')
shop_1 = PhotoImage(file='image_2\shop_1.png')
shop_2 = PhotoImage(file='image_2\Resturant 2.png')
shop_3 = PhotoImage(file='image_2\Resturant 3.png')
in_shop1 = PhotoImage(file='image_2\in_shop_1.png')
in_shop2 = PhotoImage(file='image_2\in_shop_2.png')
in_shop3 = PhotoImage(file='image_2\in_shop_3.png')
home1()
root.mainloop()