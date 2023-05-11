import sqlite3
from tkinter import *
from tkinter import messagebox


master = Tk()
w = Canvas(master, width=100, height=100)
w.config(bg='white')
w.create_oval(90,90,110,110, width=0, fill = "ivory3")
w = Canvas(master, width=200, height=200)
w.pack()
mainloop()