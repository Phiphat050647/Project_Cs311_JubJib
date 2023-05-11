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
def creatconnection():
    global conn,cursor
    conn = sqlite3.connect('JukJik_database.db')
    cursor = conn.cursor()

def buttom_revese(event):
    canvas_1.destroy()
    in_shop_page.destroy()
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

    def check_cart():
        if len(data) == 0 :
            cart_shop.config(image=cart)
        elif len(data) > 0 :
            cart_shop.config(image=cart_act)
            count = 0
            for i in range(len(data)):
                count += data[i][2]
                Label(in_shop_page,text=count,font='Helvetica 7 bold',fg='#ffffff',bg='#FF7622').place(x=333,y=20)

    cart_shop = Label(in_shop_page,relief=FLAT,image=cart,width=45,height=50,bg='#ffffff',border=0)
    cart_shop.place(x=308,y=17)
    def on_enter(e):
        cart_shop.config(cursor='hand2')
    cart_shop.bind("<Enter>", on_enter)
    cart_shop.bind("<Button-1>", buttom_revese)


    sql = "select * from shop_3"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    amount_ชาเขียวนม = Label(in_shop_page,text=result[0][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ชาเขียวนม.place(x=104,y=578)

    amount_ช็อกโกแลต = Label(in_shop_page,text=result[1][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ช็อกโกแลต.place(x=280,y=578)

    amount_นมสด = Label(in_shop_page,text=result[2][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_นมสด.place(x=104,y=760)

    amount_สตรอเบอร์รี่ชีสเค้ก = Label(in_shop_page,text=result[3][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_สตรอเบอร์รี่ชีสเค้ก.place(x=280,y=760)

    amount_คาปูชิโน่ = Label(in_shop_page,text=result[4][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_คาปูชิโน่.place(x=104,y=942)
    
    amount_ไลท์คอฟฟี่ฮันนี่ = Label(in_shop_page,text=result[5][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ไลท์คอฟฟี่ฮันนี่.place(x=280,y=942)


    check_cart()
    #-------------------------------------------------------- สินค้า 6 สินค้า ----------------
    def ชาเขียว(event):
        check = False
        for item in data:
            if item[1] == 'ชาเขียว':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ชาเขียว' :
                        if data[i][2] == result[0][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[0][1]) + ' แก้วเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 50
        if not check:
            data.append(['Cafe Amazon','ชาเขียว',1,50])
        check_cart()
        print(data)
        
    def ช็อกโกแลต(event):
        check = False
        for item in data:
            if item[1] == 'ช็อกโกแลต':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ช็อกโกแลต' :
                        if data[i][2] == result[1][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[1][1]) + ' แก้วเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 50
        if not check:
            data.append(['Cafe Amazon','ช็อกโกแลต',1,50])
        check_cart()
        print(data)
    def นมสด_fresh_milk(event):
        check = False
        for item in data:
            if item[1] == 'นมสด(Fresh Milk)':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'นมสด(Fresh Milk)' :
                        if data[i][2] == result[2][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[2][1]) + ' แก้วเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 50
        if not check:
            data.append(['Cafe Amazon','นมสด(Fresh Milk)',1,50])
        check_cart()
        print(data)
    def สตรอเบอร์รี่ชีสเค้ก(event):
        check = False
        for item in data:
            if item[1] == 'สตรอเบอร์รี่ชีสเค้ก':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'สตรอเบอร์รี่ชีสเค้ก' :
                        if data[i][2] == result[3][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[3][1]) + ' แก้วเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 70
        if not check:
            data.append(['Cafe Amazon','สตรอเบอร์รี่ชีสเค้ก',1,70])
        check_cart()
        print(data)
    def คาปูชิโน่(event):
        check = False
        for item in data:
            if item[1] == 'คาปูชิโน่':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'คาปูชิโน่' :
                        if data[i][2] == result[4][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[4][1]) + ' แก้วเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 60
        if not check:
            data.append(['Cafe Amazon','คาปูชิโน่',1,60])
        check_cart()
        print(data)
    def ไลท์คอฟฟี่ฮันนี่(event):
        check = False
        for item in data:
            if item[1] == 'ไลท์คอฟฟี่ฮันนี่':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ไลท์คอฟฟี่ฮันนี่' :
                        if data[i][2] == result[5][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[5][1]) + ' แก้วเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 55
        if not check:
            data.append(['Cafe Amazon','ไลท์คอฟฟี่ฮันนี่',1,55])
        check_cart()
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

    def check_cart():
        if len(data) == 0 :
            cart_shop.config(image=cart)
        elif len(data) > 0 :
            cart_shop.config(image=cart_act)
            count = 0
            for i in range(len(data)):
                count += data[i][2]
                Label(in_shop_page,text=count,font='Helvetica 7 bold',fg='#ffffff',bg='#FF7622').place(x=333,y=20)

    cart_shop = Label(in_shop_page,relief=FLAT,image=cart,width=45,height=50,bg='#ffffff',border=0)
    cart_shop.place(x=308,y=17)
    def on_enter(e):
        cart_shop.config(cursor='hand2')
    cart_shop.bind("<Enter>", on_enter)
    cart_shop.bind("<Button-1>", buttom_revese)


    sql = "select * from shop_2"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    amount_ไก่ทอด = Label(in_shop_page,text=result[0][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ไก่ทอด.place(x=104,y=580)

    amount_ข้าวไก่แซ่บโบว์ล = Label(in_shop_page,text=result[1][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ข้าวไก่แซ่บโบว์ล.place(x=280,y=580)

    amount_ซิงเกอร์เบอร์เกอร์ = Label(in_shop_page,text=result[2][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ซิงเกอร์เบอร์เกอร์.place(x=104,y=762)

    amount_เฟรนช์ฟรายส์ = Label(in_shop_page,text=result[3][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_เฟรนช์ฟรายส์.place(x=280,y=762)

    amount_ชุดบักเก็ตฟอร์วันมิล = Label(in_shop_page,text=result[4][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ชุดบักเก็ตฟอร์วันมิล.place(x=104,y=944)
    
    amount_แซนเดอร์_ไก่ฮิต = Label(in_shop_page,text=result[5][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_แซนเดอร์_ไก่ฮิต.place(x=280,y=944)

    amount_เฮลิเดย์_บักเก็ต = Label(in_shop_page,text=result[6][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_เฮลิเดย์_บักเก็ต.place(x=104,y=1126)
    
    amount_อิ่มสุขใจ = Label(in_shop_page,text=result[7][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_อิ่มสุขใจ.place(x=280,y=1126)

    amount_แซนเดอร์ส_คอมโบ = Label(in_shop_page,text=result[8][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_แซนเดอร์ส_คอมโบ.place(x=104,y=1316)
    
    amount_สแน็คสนุก = Label(in_shop_page,text=result[9][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_สแน็คสนุก.place(x=280,y=1316)
  

    check_cart()
    
     #-------------------------------------------------------- สินค้า 10 สินค้า ----------------
    def ไก่ทอด_1_ชิ้น(event):
        check = False
        for item in data:
            if item[1] == 'ไก่ทอด':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ไก่ทอด' :
                        if data[i][2] == result[0][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[0][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 45
        if not check:
            data.append(['KFC สาขา รังสิต','ไก่ทอด',1,45])
        check_cart()
        print(data)
    def ข้าวไก่แซ่บโบว์ล(event):
        check = False
        for item in data:
            if item[1] == 'ข้าวไก่แซ่บโบว์ล':
                check = True
                break
                break
        for i in range(len(data)):
                    if data[i][1] == 'ข้าวไก่แซ่บโบว์ล' :
                        if data[i][2] == result[1][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[1][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 69
        if not check:
            data.append(['KFC สาขา รังสิต','ข้าวไก่แซ่บโบว์ล',1,69])
        check_cart()
        print(data)
    def ซิงเกอร์เบอร์เกอร์(event):
        check = False
        for item in data:
            if item[1] == 'ซิงเกอร์เบอร์เกอร์':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ซิงเกอร์เบอร์เกอร์' :
                        if data[i][2] == result[2][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[2][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 75
        if not check:
            data.append(['KFC สาขา รังสิต','ซิงเกอร์เบอร์เกอร์',1,75])
        check_cart()
        print(data)
    def เฟรนช์ฟรายส์(event):
        check = False
        for item in data:
            if item[1] == 'เฟรนช์ฟรายส์':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'เฟรนช์ฟรายส์' :
                        if data[i][2] == result[3][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[3][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 65
        if not check:
            data.append(['KFC สาขา รังสิต','เฟรนช์ฟรายส์',1,75])
        check_cart()
        print(data)
    def ชุดบักเก็ตฟอร์วันมิล(event):
        check = False
        for item in data:
            if item[1] == 'ชุดบักเก็ตฟอร์วันมิล':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ชุดบักเก็ตฟอร์วันมิล' :
                        if data[i][2] == result[4][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[4][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 109
        if not check:
            data.append(['KFC สาขา รังสิต','ชุดบักเก็ตฟอร์วันมิล',1,109])
        check_cart()
        print(data)
    def แซนเดอร์_ไก่ฮิต(event):
        check = False
        for item in data:
            if item[1] == 'แซนเดอร์ ไก่ฮิต':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'แซนเดอร์ ไก่ฮิต' :
                        if data[i][2] == result[5][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[5][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 209
        if not check:
            data.append(['KFC สาขา รังสิต','แซนเดอร์ ไก่ฮิต',1,209])
        check_cart()
        print(data)
    def เฮลิเดย์_บักเก็ต(event):
        check = False
        for item in data:
            if item[1] == 'เฮลิเดย์ บักเก็ต':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'เฮลิเดย์ บักเก็ต' :
                        if data[i][2] == result[6][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[6][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 399
        if not check:
            data.append(['KFC สาขา รังสิต','เฮลิเดย์ บักเก็ต',1,399])
        check_cart()
        print(data)
    def อิ่มสุขใจ(event):
        check = False
        for item in data:
            if item[1] == 'Set อิ่มสุขใจ':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'Set อิ่มสุขใจ' :
                        if data[i][2] == result[7][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[7][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 429
        if not check:
            data.append(['KFC สาขา รังสิต','Set อิ่มสุขใจ',1,429])
        check_cart()
        print(data)
    def แซนเดอร์ส_คอมโบ(event):
        check = False
        for item in data:
            if item[1] == 'แซนเดอร์ส คอมโบ':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'แซนเดอร์ส คอมโบ' :
                        if data[i][2] == result[8][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[8][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 99
        if not check:
            data.append(['KFC สาขา รังสิต','แซนเดอร์ส คอมโบ',1,99])
        check_cart()
        print(data)
    def สแน็คสนุก(event):
        check = False
        for item in data:
            if item[1] == 'สแน็คสนุก':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'สแน็คสนุก' :
                        if data[i][2] == result[9][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[9][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 169
        if not check:
            data.append(['KFC สาขา รังสิต','สแน็คสนุก',1,169])
        check_cart()
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
    global canvas_1,in_shop_page,in_shop,cart_shop

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
    
    def check_cart():
        if len(data) == 0 :
            cart_shop.config(image=cart)
        elif len(data) > 0 :
            cart_shop.config(image=cart_act)
            count = 0
            for i in range(len(data)):
                count += data[i][2]
                Label(in_shop_page,text=count,font='Helvetica 7 bold',fg='#ffffff',bg='#FF7622').place(x=333,y=20)

    cart_shop = Label(in_shop_page,relief=FLAT,image=cart,width=45,height=50,bg='#ffffff',border=0)
    cart_shop.place(x=308,y=17)
    def on_enter(e):
        cart_shop.config(cursor='hand2')
    cart_shop.bind("<Enter>", on_enter)
    cart_shop.bind("<Button-1>", buttom_revese)
    check_cart()

    sql = "select * from shop_1"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    
    amount_พัดกระเพรา = Label(in_shop_page,text=result[0][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_พัดกระเพรา.place(x=104,y=578)

    amount_ข้าวหมูกระเทียม = Label(in_shop_page,text=result[1][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ข้าวหมูกระเทียม.place(x=280,y=578)

    amount_ข้าวพัด = Label(in_shop_page,text=result[2][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ข้าวพัด.place(x=104,y=760)

    amount_ข้าวมันไก่ = Label(in_shop_page,text=result[3][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ข้าวมันไก่.place(x=280,y=760)

    amount_ข้าวพัดพริกแกงหมู = Label(in_shop_page,text=result[4][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ข้าวพัดพริกแกงหมู.place(x=104,y=942)
    
    amount_ข้าวลาบหมู = Label(in_shop_page,text=result[5][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ข้าวลาบหมู.place(x=280,y=942)

    amount_ข้าวลาบหมู = Label(in_shop_page,text=result[6][1],font='Helvetica 8 bold',fg='#646982',bg='#ffffff')
    amount_ข้าวลาบหมู.place(x=104,y=1124)
    
    
    #-------------------------------------------------------- สินค้า 6 สินค้า ----------------
    def พัดกระเพราหมู(event):
        check = False
        for item in data:
            if item[1] == 'พัดกระเพราหมู':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'พัดกระเพราหมู' :
                        if data[i][2] == result[0][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[0][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 50

        if not check:
            data.append(['ร้านป้าแจ๋ม เบอร์ตอง','พัดกระเพราหมู',1,50])

        check_cart()
        print(data)
    def ข้าวหมูกระเทียม(event):
        check = False
        for item in data:
            if item[1] == 'ข้าวหมูกระเทียม':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ข้าวหมูกระเทียม' :
                        if data[i][2] == result[1][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[1][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 45
        if not check:
            data.append(['ร้านป้าแจ๋ม เบอร์ตอง','ข้าวหมูกระเทียม',1,45])
        check_cart()
        print(data)
    def ข้าวพัด(event):
        check = False
        for item in data:
            if item[1] == 'ข้าวพัด':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ข้าวพัด' :
                        if data[i][2] == result[2][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[2][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 40
        if not check:
            data.append(['ร้านป้าแจ๋ม เบอร์ตอง','ข้าวพัด',1,40])
        check_cart()
        print(data)
    def ข้าวมันไก่(event):
        check = False
        for item in data:
            if item[1] == 'ข้าวมันไก่':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ข้าวมันไก่' :
                        if data[i][2] == result[3][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[3][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 40
        if not check:
            data.append(['ร้านป้าแจ๋ม เบอร์ตอง','ข้าวมันไก่',1,40])
        check_cart()
        print(data)
    def ข้าวพัดพริกแกงหมู(event):
        check = False
        for item in data:
            if item[1] == 'ข้าวพัดพริกแกงหมู':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ข้าวพัดพริกแกงหมู' :
                        if data[i][2] == result[4][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[4][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 50
        if not check:
            data.append(['ร้านป้าแจ๋ม เบอร์ตอง','ข้าวพัดพริกแกงหมู',1,50])
        check_cart()
        print(data)
    def ข้าวลาบหมู(event):
        check = False
        for item in data:
            if item[1] == 'ข้าวลาบหมู':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'ข้าวลาบหมู' :
                        if data[i][2] == result[5][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[5][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 60
        if not check:
            data.append(['ร้านป้าแจ๋ม เบอร์ตอง','ข้าวลาบหมู',1,60])
        check_cart()
        print(data)
    def พัดซีอิ้ว(event):
        check = False
        for item in data:
            if item[1] == 'พัดซีอิ้ว':
                check = True
                break
        for i in range(len(data)):
                    if data[i][1] == 'พัดซีอิ้ว' :
                        if data[i][2] == result[6][1] :
                            messagebox.showwarning('แจ้งเตือน', 'เมนูนี้มีจำกัดเพียง ' + str(result[6][1]) + ' จานเท่านั้น')
                        else :
                            data[i][2] += 1
                            data[i][3] += 50
        if not check:
            data.append(['ร้านป้าแจ๋ม เบอร์ตอง','พัดซีอิ้ว',1,50])
        check_cart()
        print(data)
    #-------------------------------------------------------- ปุ่มสั่ง 6 สินค้า ----------------
    buttom_shop_1 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_1.place(x=136,y=598)
    def on_enter(e):
        buttom_shop_1.config(cursor='hand2')
    buttom_shop_1.bind("<Enter>",on_enter)
    buttom_shop_1.bind("<Button-1>",พัดกระเพราหมู)

    buttom_shop_2 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_2.place(x=310,y=598)
    def on_enter(e):
        buttom_shop_2.config(cursor='hand2')
    buttom_shop_2.bind("<Enter>",on_enter)
    buttom_shop_2.bind("<Button-1>",ข้าวหมูกระเทียม)

    buttom_shop_3 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_3.place(x=136,y=780)
    def on_enter(e):
        buttom_shop_3.config(cursor='hand2')
    buttom_shop_3.bind("<Enter>",on_enter)
    buttom_shop_3.bind("<Button-1>",ข้าวพัด)

    buttom_shop_4 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_4.place(x=310,y=780)
    def on_enter(e):
        buttom_shop_4.config(cursor='hand2')
    buttom_shop_4.bind("<Enter>",on_enter)
    buttom_shop_4.bind("<Button-1>",ข้าวมันไก่)

    buttom_shop_5 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_5.place(x=137,y=962)
    def on_enter(e):
        buttom_shop_5.config(cursor='hand2')
    buttom_shop_5.bind("<Enter>",on_enter)
    buttom_shop_5.bind("<Button-1>",ข้าวพัดพริกแกงหมู)

    buttom_shop_6 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_6.place(x=311,y=962)
    def on_enter(e):
        buttom_shop_6.config(cursor='hand2')
    buttom_shop_6.bind("<Enter>",on_enter)
    buttom_shop_6.bind("<Button-1>",ข้าวลาบหมู)

    buttom_shop_7 = Label(in_shop_page,relief=FLAT,image=shop_buttom,width=30,height=30,bg='#ffffff',border=0)
    buttom_shop_7.place(x=137,y=1144)
    def on_enter(e):
        buttom_shop_7.config(cursor='hand2')
    buttom_shop_7.bind("<Enter>",on_enter)
    buttom_shop_7.bind("<Button-1>",พัดซีอิ้ว)


    in_shop_page.update_idletasks()
    canvas_1.config(scrollregion=canvas_1.bbox('all'))

def pag_edit(event):
    global canvas_1,in_shop_page,in_shop,cart_shop
    canvas_1.destroy()
    in_shop_page.destroy()

    canvas_1 = Canvas(root, bg='yellow',width=375, height=812 ,scrollregion=(0,0,375,812))
    canvas_1.pack()
    in_shop_page = Frame(canvas_1,bg='#ffffff')

    canvas_1.create_window((0,0), window=in_shop_page, anchor=NW)

    editpag = Label(in_shop_page,relief=FLAT,image=edite,width=375,height=812)
    editpag.pack()
    
def proflie_pag(event):
    global canvas_1,in_shop_page,in_shop,cart_shop

    canvas.destroy()
    Label_buttom.destroy()
    home_1.destroy()

    canvas_1 = Canvas(root, bg='yellow',width=375, height=812)
    canvas_1.pack()
    in_shop_page = Frame(canvas_1,bg='#ffffff')

    canvas_1.create_window((0,0), window=in_shop_page, anchor=NW)

    proflie_label = Label(in_shop_page,relief=FLAT,image=proflie,width=375,height=812)
    proflie_label.pack()
    
    cartgo = Label(in_shop_page,relief=FLAT,image=cart_warp,width=327,height=77,bg='#ffffff',border=0)
    cartgo.place(x=24,y=406)
    def on_enter(e):
        cartgo.config(cursor='hand2')
    cartgo.bind("<Enter>",on_enter)
    cartgo.bind("<Button-1>", in_shop_1)

    log_put = Label(in_shop_page,relief=FLAT,image=logout,width=327,height=80,bg='#ffffff',border=0)
    log_put.place(x=30,y=700)
    def on_enter(e):
        log_put.config(cursor='hand2')
    log_put.bind("<Enter>",on_enter)
    log_put.bind("<Button-1>", in_shop_1)

    edit_but = Label(in_shop_page,relief=FLAT,image=buttom_edite,width=327,height=142,bg='#ffffff',border=0)
    edit_but.place(x=26,y=253)
    def on_enter(e):
        edit_but.config(cursor='hand2')
    edit_but.bind("<Enter>",on_enter)
    edit_but.bind("<Button-1>", pag_edit)


    revese = Label(in_shop_page,relief=FLAT,image=buttom_back,width=45,height=45,bg='#ffffff',border=0)
    revese.place(x=25,y=51)
    def on_enter(e):
        revese.config(cursor='hand2')
    revese.bind("<Enter>",on_enter)
    revese.bind("<Button-1>", buttom_revese)
     
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



    buttom_menu = Label(splash_page,relief=FLAT,image=menu_buttom,width=45,height=45,bg='#ffffff',border=0)
    buttom_menu.place(x=29,y=16)
    def on_enter(e):
        buttom_menu.config(cursor='hand2')
    buttom_menu.bind("<Enter>",on_enter)
    buttom_menu.bind("<Button-1>", proflie_pag)

    def check_cart():
        if len(data) == 0 :
            cart_shop.config(image=cart)
        elif len(data) > 0 :
            cart_shop.config(image=cart_act)
            count = 0
            for i in range(len(data)):
                count += data[i][2]
                Label(splash_page,text=count,font='Helvetica 7 bold',fg='#ffffff',bg='#FF7622').place(x=335,y=20)

    cart_shop = Label(splash_page,relief=FLAT,image=cart,width=45,height=50,bg='#ffffff',border=0)
    cart_shop.place(x=311,y=17)
    def on_enter(e):
        cart_shop.config(cursor='hand2')
    cart_shop.bind("<Enter>", on_enter)
    cart_shop.bind("<Button-1>", buttom_revese)

    check_cart()
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
data_shop = PhotoImage(file='image_2\data_shop.png')
cart = PhotoImage(file='image_2\Cart.png')
cart_act = PhotoImage(file='image_2\Cart_act.png')
proflie = PhotoImage(file='image_2\Personal_Profiles.png')
menu_buttom = PhotoImage(file='image_2\Menu.png')
cart_warp = PhotoImage(file='image_2\cart_warp.png')
logout = PhotoImage(file='image_2\Logout.png')
edite = PhotoImage(file='image_2\Edit Profile.png')
buttom_edite = PhotoImage(file='image_2\\buttom_edite.png')

creatconnection()
home1()
root.mainloop()