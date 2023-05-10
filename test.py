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

data = []

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
    #-------------------------------------------------------- สินค้า 6 สินค้า ----------------
    def ชาเขียว(event):
        check = False
        for item in data:
            if item[1] == 'ชาเขียว':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ชาเขียว' :
                        data[i][2] += 1
                        data[i][3] += 50
        if not check:
            data.append(['Cafe Amazon','ชาเขียว',1,50])
            
        print(data)
        
    def ช็อกโกแลต(event):
        check = False
        for item in data:
            if item[1] == 'ช็อกโกแลต':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ช็อกโกแลต' :
                        data[i][2] += 1
                        data[i][3] += 50
        if not check:
            data.append(['Cafe Amazon','ช็อกโกแลต',1,50])
        print(data)
    def นมสด_fresh_milk(event):
        check = False
        for item in data:
            if item[1] == 'นมสด(Fresh Milk)':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'นมสด(Fresh Milk)' :
                        data[i][2] += 1
                        data[i][3] += 50
        if not check:
            data.append(['Cafe Amazon','นมสด(Fresh Milk)',1,50])
        print(data)
    def สตรอเบอร์รี่ชีสเค้ก(event):
        check = False
        for item in data:
            if item[1] == 'สตรอเบอร์รี่ชีสเค้ก':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'สตรอเบอร์รี่ชีสเค้ก' :
                        data[i][2] += 1
                        data[i][3] += 70
        if not check:
            data.append(['Cafe Amazon','สตรอเบอร์รี่ชีสเค้ก',1,70])
        print(data)
    def คาปูชิโน่(event):
        check = False
        for item in data:
            if item[1] == 'คาปูชิโน่':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'คาปูชิโน่' :
                        data[i][2] += 1
                        data[i][3] += 60
        if not check:
            data.append(['Cafe Amazon','คาปูชิโน่',1,60])
        print(data)
    def ไลท์คอฟฟี่ฮันนี่(event):
        check = False
        for item in data:
            if item[1] == 'ไลท์คอฟฟี่ฮันนี่':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ไลท์คอฟฟี่ฮันนี่' :
                        data[i][2] += 1
                        data[i][3] += 55
        if not check:
            data.append(['Cafe Amazon','ไลท์คอฟฟี่ฮันนี่',1,55])
        print(data)

    #-------------------------------------------------------- ปุ่มสั่ง 6 สินค้า ----------------
    buttom_shop_1 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_1.place(x=136,y=598)
    def on_enter(e):
        buttom_shop_1.config(cursor='hand2')
    buttom_shop_1.bind("<Enter>",on_enter)
    buttom_shop_1.bind("<Button-1>",ชาเขียว)

    buttom_shop_2 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_2.place(x=310,y=598)
    def on_enter(e):
        buttom_shop_2.config(cursor='hand2')
    buttom_shop_2.bind("<Enter>",on_enter)
    buttom_shop_2.bind("<Button-1>",ช็อกโกแลต)

    buttom_shop_3 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_3.place(x=136,y=780)
    def on_enter(e):
        buttom_shop_3.config(cursor='hand2')
    buttom_shop_3.bind("<Enter>",on_enter)
    buttom_shop_3.bind("<Button-1>",นมสด_fresh_milk)

    buttom_shop_4 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_4.place(x=310,y=780)
    def on_enter(e):
        buttom_shop_4.config(cursor='hand2')
    buttom_shop_4.bind("<Enter>",on_enter)
    buttom_shop_4.bind("<Button-1>",สตรอเบอร์รี่ชีสเค้ก)

    buttom_shop_5 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_5.place(x=137,y=962)
    def on_enter(e):
        buttom_shop_5.config(cursor='hand2')
    buttom_shop_5.bind("<Enter>",on_enter)
    buttom_shop_5.bind("<Button-1>",คาปูชิโน่)

    buttom_shop_6 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_6.place(x=311,y=962)
    def on_enter(e):
        buttom_shop_6.config(cursor='hand2')
    buttom_shop_6.bind("<Enter>",on_enter)
    buttom_shop_6.bind("<Button-1>",ไลท์คอฟฟี่ฮันนี่)

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
     #-------------------------------------------------------- สินค้า 10 สินค้า ----------------
    def ไก่ทอด_1_ชิ้น(event):
        check = False
        for item in data:
            if item[1] == 'ไก่ทอด':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ไก่ทอด' :
                        data[i][2] += 1
                        data[i][3] += 45
        if not check:
            data.append(['KFC สาขา รังสิต','ไก่ทอด',1,45])
        print(data)
    def ข้าวไก่แซ่บโบว์ล(event):
        check = False
        for item in data:
            if item[1] == 'ข้าวไก่แซ่บโบว์ล':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ข้าวไก่แซ่บโบว์ล' :
                        data[i][2] += 1
                        data[i][3] += 69
        if not check:
            data.append(['KFC สาขา รังสิต','ข้าวไก่แซ่บโบว์ล',1,69])
        print(data)
    def ซิงเกอร์เบอร์เกอร์(event):
        check = False
        for item in data:
            if item[1] == 'ซิงเกอร์เบอร์เกอร์':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ซิงเกอร์เบอร์เกอร์' :
                        data[i][2] += 1
                        data[i][3] += 75
        if not check:
            data.append(['KFC สาขา รังสิต','ซิงเกอร์เบอร์เกอร์',1,75])
        print(data)
    def เฟรนช์ฟรายส์(event):
        check = False
        for item in data:
            if item[1] == 'เฟรนช์ฟรายส์':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'เฟรนช์ฟรายส์' :
                        data[i][2] += 1
                        data[i][3] += 75
        if not check:
            data.append(['KFC สาขา รังสิต','เฟรนช์ฟรายส์',1,75])
        print(data)
    def ชุดบักเก็ตฟอร์วันมิล(event):
        check = False
        for item in data:
            if item[1] == 'ชุดบักเก็ตฟอร์วันมิล':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ชุดบักเก็ตฟอร์วันมิล' :
                        data[i][2] += 1
                        data[i][3] += 109
        if not check:
            data.append(['KFC สาขา รังสิต','ชุดบักเก็ตฟอร์วันมิล',1,109])
        print(data)
    def แซนเดอร์_ไก่ฮิต(event):
        check = False
        for item in data:
            if item[1] == 'แซนเดอร์ ไก่ฮิต':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'แซนเดอร์ ไก่ฮิต' :
                        data[i][2] += 1
                        data[i][3] += 209
        if not check:
            data.append(['KFC สาขา รังสิต','แซนเดอร์ ไก่ฮิต',1,209])
        print(data)
    def เฮลิเดย์_บักเก็ต(event):
        check = False
        for item in data:
            if item[1] == 'เฮลิเดย์ บักเก็ต':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'เฮลิเดย์ บักเก็ต' :
                        data[i][2] += 1
                        data[i][3] += 399
        if not check:
            data.append(['KFC สาขา รังสิต','เฮลิเดย์ บักเก็ต',1,399])
        print(data)
    def อิ่มสุขใจ(event):
        check = False
        for item in data:
            if item[1] == 'Set อิ่มสุขใจ':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'Set อิ่มสุขใจ' :
                        data[i][2] += 1
                        data[i][3] += 429
        if not check:
            data.append(['KFC สาขา รังสิต','Set อิ่มสุขใจ',1,429])
        print(data)
    def แซนเดอร์ส_คอมโบ(event):
        check = False
        for item in data:
            if item[1] == 'แซนเดอร์ส คอมโบ':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'แซนเดอร์ส คอมโบ' :
                        data[i][2] += 1
                        data[i][3] += 99
        if not check:
            data.append(['KFC สาขา รังสิต','แซนเดอร์ส คอมโบ',1,99])
        print(data)
    def สแน็คสนุก(event):
        check = False
        for item in data:
            if item[1] == 'สแน็คสนุก':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'สแน็คสนุก' :
                        data[i][2] += 1
                        data[i][3] += 169
        if not check:
            data.append(['KFC สาขา รังสิต','สแน็คสนุก',1,169])
        print(data)
    #-------------------------------------------------------- ปุ่มสั่ง 10 สินค้า ----------------
    buttom_shop_1 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_1.place(x=137,y=600)
    def on_enter(e):
        buttom_shop_1.config(cursor='hand2')
    buttom_shop_1.bind("<Enter>",on_enter)
    buttom_shop_1.bind("<Button-1>",ไก่ทอด_1_ชิ้น)

    buttom_shop_2 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_2.place(x=311,y=600)
    def on_enter(e):
        buttom_shop_2.config(cursor='hand2')
    buttom_shop_2.bind("<Enter>",on_enter)
    buttom_shop_2.bind("<Button-1>",ข้าวไก่แซ่บโบว์ล)

    buttom_shop_3 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_3.place(x=137,y=782)
    def on_enter(e):
        buttom_shop_3.config(cursor='hand2')
    buttom_shop_3.bind("<Enter>",on_enter)
    buttom_shop_3.bind("<Button-1>",ซิงเกอร์เบอร์เกอร์)

    buttom_shop_4 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_4.place(x=311,y=782)
    def on_enter(e):
        buttom_shop_4.config(cursor='hand2')
    buttom_shop_4.bind("<Enter>",on_enter)
    buttom_shop_4.bind("<Button-1>",เฟรนช์ฟรายส์)

    buttom_shop_5 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_5.place(x=138,y=964)
    def on_enter(e):
        buttom_shop_5.config(cursor='hand2')
    buttom_shop_5.bind("<Enter>",on_enter)
    buttom_shop_5.bind("<Button-1>",ชุดบักเก็ตฟอร์วันมิล)

    buttom_shop_6 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_6.place(x=312,y=964)
    def on_enter(e):
        buttom_shop_6.config(cursor='hand2')
    buttom_shop_6.bind("<Enter>",on_enter)
    buttom_shop_6.bind("<Button-1>",แซนเดอร์_ไก่ฮิต)

    buttom_shop_7 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_7.place(x=138,y=1146)
    def on_enter(e):
        buttom_shop_7.config(cursor='hand2')
    buttom_shop_7.bind("<Enter>",on_enter)
    buttom_shop_7.bind("<Button-1>",เฮลิเดย์_บักเก็ต)

    buttom_shop_8 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_8.place(x=312,y=1146)
    def on_enter(e):
        buttom_shop_8.config(cursor='hand2')
    buttom_shop_8.bind("<Enter>",on_enter)
    buttom_shop_8.bind("<Button-1>",อิ่มสุขใจ)

    buttom_shop_9 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_9.place(x=137,y=1336)
    def on_enter(e):
        buttom_shop_9.config(cursor='hand2')
    buttom_shop_9.bind("<Enter>",on_enter)
    buttom_shop_9.bind("<Button-1>",แซนเดอร์ส_คอมโบ)

    buttom_shop_10 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_10.place(x=311,y=1336)
    def on_enter(e):
        buttom_shop_10.config(cursor='hand2')
    buttom_shop_10.bind("<Enter>",on_enter)
    buttom_shop_10.bind("<Button-1>",สแน็คสนุก)


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

    #-------------------------------------------------------- ปุ่มสั่ง 6 สินค้า ----------------
    buttom_shop_1 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_1.place(x=136,y=598)
    def on_enter(e):
        buttom_shop_1.config(cursor='hand2')
    buttom_shop_1.bind("<Enter>",on_enter)
    buttom_shop_1.bind("<Button-1>")

    buttom_shop_2 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_2.place(x=310,y=598)
    def on_enter(e):
        buttom_shop_2.config(cursor='hand2')
    buttom_shop_2.bind("<Enter>",on_enter)
    buttom_shop_2.bind("<Button-1>")

    buttom_shop_3 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_3.place(x=136,y=780)
    def on_enter(e):
        buttom_shop_3.config(cursor='hand2')
    buttom_shop_3.bind("<Enter>",on_enter)
    buttom_shop_3.bind("<Button-1>")

    buttom_shop_4 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_4.place(x=310,y=780)
    def on_enter(e):
        buttom_shop_4.config(cursor='hand2')
    buttom_shop_4.bind("<Enter>",on_enter)
    buttom_shop_4.bind("<Button-1>")

    buttom_shop_5 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_5.place(x=137,y=962)
    def on_enter(e):
        buttom_shop_5.config(cursor='hand2')
    buttom_shop_5.bind("<Enter>",on_enter)
    buttom_shop_5.bind("<Button-1>")

    buttom_shop_6 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_6.place(x=311,y=962)
    def on_enter(e):
        buttom_shop_6.config(cursor='hand2')
    buttom_shop_6.bind("<Enter>",on_enter)
    buttom_shop_6.bind("<Button-1>")


    buttom_shop_7 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_7.place(x=137,y=1142)
    def on_enter(e):
        buttom_shop_7.config(cursor='hand2')
    buttom_shop_7.bind("<Enter>",on_enter)
    buttom_shop_7.bind("<Button-1>")


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
shop_buttom = PhotoImage(file='image_2\shop_buttom.png')
home1()
root.mainloop()