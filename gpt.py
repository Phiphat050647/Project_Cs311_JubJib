from tkinter import *

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
    return root

def button_click(i):
    print(i)


def make_button_click_command(i):
    return lambda: button_click(i)


def firt_pace() :
    canvas_1 = Canvas(root, bg='#ffffff',width=375, height=812 ,scrollregion=(0,0,375,812))
    canvas_1.pack()
    splash_page = Frame(canvas_1,bg='#ffffff')
    splash_page.pack()
    for i in range(10):
        value = (i + 1) % 10
        row, col = divmod(i, 3)
        btn = Button(splash_page, text=value, padx=40, pady=20, command=make_button_click_command(value))
        btn.grid(row=row + 1, column=col)







root = mainwindow()
root.mainloop()