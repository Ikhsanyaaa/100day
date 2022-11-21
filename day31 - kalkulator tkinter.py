#membuat interface

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("interface")
window.geometry("300x200")

def cetak():
    angka1 = int(entry_angka1.get())
    angka2= int(entry_angka2.get())
    hasil = angka1 + angka2
    label_nama = Label(window, text=hasil)
    label_nama.pack()
judul = Label(window, text="menampilkan hasil penjumlahan", font=15, bg = "blue", fg="white").pack() 
label_angka1 = Label(window, text="masukkan angka ")
label_angka1.pack()
entry_angka1 = Entry(window)
entry_angka1.pack()
label_angka2 = Label(window, text="masukkan angka ")
label_angka2.pack()
entry_angka2 = Entry(window)
entry_angka2.pack()
tk.Button(window, text="hasil jumlah",command= cetak).pack()
  
window.mainloop()