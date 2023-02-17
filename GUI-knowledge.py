from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลัก
GUI.title('โปรแกรมคำนวณค่า BMI') #ชื่อโปรแกรม
GUI.geometry('200x200') #ขนาดโปรแกรม

#คำอธิบายให้ใส่ข้อมูล
L1 = Label(GUI,text='โปรดใส่น้ำหนักและส่วนสูง',font=('Angsana New',15),fg='red')
L1.pack()

#ฟังก์ชั่นการคำนวณค่า bmi
def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    #คำนวณค่า bmi
    bmi = weight / (height ** 2)

    #แสดงค่าตาม bmi
    if bmi < 18.5:
        text1 = ' : น้ำหนักน้อย'
        messagebox.showinfo('ค่าดัชนีมวลกายของคุณ','BMI = {:.2f}'.format(bmi) + text1)

    elif bmi >= 18.5 and bmi < 25:
        text2 = ' : น้ำหนักปกติ'
        messagebox.showinfo('ค่าดัชนีมวลกายของคุณ','BMI = {:.2f}'.format(bmi) + text2)

    elif bmi >= 25 and bmi < 30:
        text3 = ' : โรคอ้วนระดับ 1'
        messagebox.showinfo('ค่าดัชนีมวลกายของคุณ','BMI = {:.2f}'.format(bmi) + text3)

    elif bmi >= 30:
        text4 = ' : โรคอ้วนระดับ 2'
        messagebox.showinfo('ค่าดัชนีมวลกายของคุณ','BMI = {:.2f}'.format(bmi) + text4)

#ช่องใส่น้ำหนัก
weight_label = Label(GUI, text="น้ำหนัก (กิโลกรัม):")
weight_label.pack()

weight_entry = Entry(GUI)
weight_entry.pack()

#ช่องใส่ส่วนสูง
height_label = Label(GUI, text="ส่วนสูง (เมตร):")
height_label.pack()

height_entry = Entry(GUI)
height_entry.pack()

#ปุ่มกดคำนวณค่า BMI
FB1 = Frame(GUI)
FB1.place(x=50,y=125)
B2 = ttk.Button(FB1,text='คำนวณค่า BMI',command=calculate_bmi)
B2.pack(ipadx=5,ipady=5)

GUI.mainloop()
