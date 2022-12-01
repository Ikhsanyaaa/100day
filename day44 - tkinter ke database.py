#menghubungkan tkinter dengan database

import tkinter
from tkinter import *
import MySQLdb

window = tkinter.Tk()
window.title("database")
window.geometry("500x400")

def submit():
    db = MySQLdb.connect(host = "localhost",user = "root",password = "",database = "datasaya")
    insertdb = db.cursor()
    sql_saya = "insert into register_user values('"+entry_nama.get()+"','"+entry_umur.get()+"','"+entry_alamat.get()+"')"
    insertdb.execute(sql_saya)
    db.commit()
    db.close()

label_nama = Label(window, text="nama : ")
label_nama.place(x = 10, y = 7)
entry_nama = Entry(window, width=16)
entry_nama.place(x = 60, y = 10)
label_umur = Label(window, text="umur : ")
label_umur.place(x = 10, y = 34)
entry_umur = Entry(window, width=16)
entry_umur.place(x = 60, y = 37)
label_alamat = Label(window, text="alamat : ")
label_alamat.place(x = 10, y = 64)
entry_alamat = Entry(window, width=16)
entry_alamat.place(x = 60, y = 67)

button_submit = Button(window, text="submit")
button_submit.place(x = 10, y=100)

window.mainloop()