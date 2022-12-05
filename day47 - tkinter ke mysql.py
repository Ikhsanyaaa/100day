import tkinter
from tkinter import *
import mysql.connector

window = tkinter.Tk()
window.geometry("500x400")
window.title("tkinter ke database")

def submit():
    db = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "")
    cursor = db.cursor()
    cursor.execute("create database tkinter")
    cursor.execute("use tkinter")
    cursor.execute("create table mhs(nim char(10) not null primary key, nama varchar(20) not null, umur int(2) not null)")
    nim = nim_entry.get()
    nama = nama_entry.get()
    umur = int(umur_entry.get())
    cursor.execute(f'''insert into mhs 
values
("{nim}","{nama}",{umur})''')
    db.commit()
    selesai_label = Label(window, text="data anda telah dimasukkan ke dalam database")
    selesai_label.place(x= 10, y = 130)

nim_label = Label(window, text="nim")
nim_label.place(x=10,y=10)
nim_entry = Entry(window,width=16)
nim_entry.place(x = 60, y = 10)

nama_label = Label(window, text="nama")
nama_label.place(x=10,y=40)
nama_entry = Entry(window,width=16)
nama_entry.place(x = 60, y = 40)

umur_label = Label(window, text="umur")
umur_label.place(x=10,y=70)
umur_entry = Entry(window,width=16)
umur_entry.place(x = 60, y = 70)

submit_button = Button(window,text="submit",command=submit)
submit_button.place(x= 10, y = 100)
window.mainloop()
