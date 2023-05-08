from tkinter import *

root = Tk()

# สร้าง StringVar เพื่อเก็บข้อมูลใน Label
label_text = StringVar()

# กำหนดค่าเริ่มต้นให้กับ Label
label_text.set("Enter your name:")

# สร้าง Label
label = Label(root, textvariable=label_text)

# สร้าง Entry สำหรับกรอกข้อมูล
entry = Entry(root)

# กำหนดตำแหน่งของ Label และ Entry ด้วย grid
label.grid(row=0, column=0)
entry.grid(row=0, column=1)

root.mainloop()
