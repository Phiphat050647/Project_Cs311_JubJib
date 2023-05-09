from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=200)
canvas.pack(side=LEFT)

scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=LEFT, fill=Y)

frame = Frame(canvas, bg='white')
canvas.create_window((0,0), window=frame, anchor=NW)

# สร้าง label และเพิ่มเข้าไปใน frame
label1 = Label(frame, text='Label 1')
label1.pack()

label2 = Label(frame, text='Label 2')
label2.pack()

# เชื่อม scrollbar กับ canvas
canvas.config(yscrollcommand=scrollbar.set)

# ตั้งค่า scrollregion ของ canvas เพื่อให้ scrollbar ทำงานได้ถูกต้อง
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox('all'))

root.mainloop()