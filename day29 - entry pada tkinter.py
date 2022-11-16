#membuat interface

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("interface")
window.geometry("300x200")

def cetak():
    nama = entry_nama.get()
    label_nama = Label(window, text=nama)
    label_nama.pack()
judul = Label(window, text="menampilkan nama", font=15, bg = "blue", fg="white").pack() 
label_nama = Label(window, text="nama ")
label_nama.pack()
entry_nama = Entry(window)
entry_nama.pack()
nama = entry_nama.get()
tk.Button(window, text="cetak",command= cetak).pack()
  
window.mainloop()
