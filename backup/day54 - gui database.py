import tkinter 
from tkinter import *
from tkinter import messagebox
import mysql.connector

window = tkinter.Tk()
window.title("menghubungkan gui ke database")
window.geometry("500x400")

def terklik():
    db = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "")
    cursor = db.cursor()
    cursor.execute("drop database mydata")
    cursor.execute("create database mydata")
    cursor.execute("use mydata")
    cursor.execute('''create table mahasiswa(nim char(10) not null primary key,
nama varchar(20) not null,
umur int(3) not null,
jenis_kelamin enum("P","L") not null,
jurusan varchar(10) not null)''')
    nama = entry_nama.get()
    nim = entry_nim.get()
    umur = spinbox_umur.get()
    jk = jenis_kelamin.get()
    prodi = jurusan.get()
    cursor.execute(f'''insert into mahasiswa
values
("{nim}","{nama}",{umur},"{jk}","{prodi}")''')
    db.commit()
    messagebox.showinfo("selesai","data anda sudah direkam")

label_nama = Label(window, text="nama")
label_nama.place(x=10,y=10)
entry_nama = Entry(window, width= 16)
entry_nama.place(x=60, y= 10)
label_nim = Label(window, text="nim")
label_nim.place(x=10,y=30)
entry_nim = Entry(window, width= 16)
entry_nim.place(x=60, y= 30)
label_umur = Label(window, text="umur")
label_umur.place(x=10,y=50)
spinbox_umur = Spinbox(window, from_=0, to=50, width=16)
spinbox_umur.place(x=60,y=50)
label_jk = Label(window, text="jenis kelamin")
label_jk.place(x=10,y=70)
jenis_kelamin = StringVar()
radiobutton_cowo = Radiobutton(window,variable=jenis_kelamin, text="laki-laki", value="L")
radiobutton_cowo.place(x=100, y=70)
radiobutton_cewe = Radiobutton(window,variable=jenis_kelamin, text="perempuan", value="P")
radiobutton_cewe.place(x=180, y=70)
jurusan = StringVar()
label_jurusan = Label(window, text="jurusan")
label_jurusan.place(x=10,y=90)
inf = Radiobutton(window,variable=jurusan, text="informatika", value = "informatika")
ts = Radiobutton(window,variable=jurusan, text="teknik sipil", value= "teknik sipil")
pwk = Radiobutton(window,variable=jurusan,text="pwk", value="pwk")
inf.place(x=60,y=90)
ts.place(x=160,y=90)
pwk.place(x=260,y=90)
submit = Button(window, text="kirim", command=terklik).place(x=10, y=140)

window.mainloop()