from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from datetime import datetime
import csv

GUI = Tk() # นี่คือหน้าจอหลัก
GUI.title('โปรแกรมคำนวณค่า BMI') #ชื่อโปรแกรม
GUI.geometry('250x200') #ขนาดโปรแกรม

#ตัวแปรพิเศษที่ใช้กับข้อความใน gui
weight = StringVar()
height = StringVar()

#ฟังก์ชั่น save และ คำนวณค่า bmi
def calculate_bmi_save():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    
    #คำนวณค่า BMI
    bmi = weight / (height ** 2)

    #csv
    with open('bmi_data_1.csv','a',encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        t = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        writer.writerow([t, weight, height, bmi])
        
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

    #เคลียร์ค่าในช่อง
    weight_entry.delete(0, END)
    height_entry.delete(0, END)

#คำอธิบายให้ใส่ข้อมูล
L1 = Label(GUI,text='โปรดใส่น้ำหนักและส่วนสูง',font=('Angsana New',20))
L1.pack()

#ใส่น้ำหนัก
weight_label = Label(GUI, text="น้ำหนัก (กิโลกรัม):")
weight_label.pack()

weight_entry = ttk.Entry(GUI,textvariable=weight,font=('Angsana New',15))
weight_entry.pack()

#ใส่ส่วนสูง
height_label = Label(GUI, text="ส่วนสูง (เมตร):")
height_label.pack()

height_entry = ttk.Entry(GUI,textvariable=height,font=('Angsana New',15))
height_entry.pack()

#ปุ่มกด
FB1 = Frame(GUI)
FB1.place(x=80,y=155)
B1 = ttk.Button(FB1,text='คำนวณค่า BMI',command=calculate_bmi_save)
B1.pack(ipadx=5,ipady=5)


GUI.mainloop()
