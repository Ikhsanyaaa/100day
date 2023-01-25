import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("kalkulator")
window.geometry("400x300")
angka1 = 0
angka2 = 0
hasil = 0

def hasil_akhir():
    global hasil
    hasill = Label(window, text=hasil).place(x=210, y = 122)

def penjumlahan():
    global angka1, angka2, hasil
    angka1= int(entry_angka1.get())
    angka2= int(entry_angka2.get())
    hasil = angka1 + angka2
    button_hasil = Button(window, text="  =  ", command=hasil_akhir).place(x=170, y = 120)

def pengurangan():
    global angka1, angka2, hasil
    angka1= int(entry_angka1.get())
    angka2= int(entry_angka2.get())
    hasil = angka1 - angka2
    button_hasil = Button(window, text="  =  ", command=hasil_akhir).place(x=170, y = 120)

def perkalian():
    global angka1, angka2, hasil
    angka1= int(entry_angka1.get())
    angka2= int(entry_angka2.get())
    hasil = angka1 * angka2
    button_hasil = Button(window, text="  =  ", command=hasil_akhir).place(x=170, y = 120)

def pembagian():
    global angka1, angka2, hasil
    angka1= int(entry_angka1.get())
    angka2= int(entry_angka2.get())
    hasil = angka1 / angka2
    button_hasil = Button(window, text="  =  ", command=hasil_akhir).place(x=170, y = 120)
    
label_judul = Label(window, text="kalkulator", bg="black", fg="white").place(x=165, y=0)
entry_angka1 = Entry(window, width=15)
entry_angka1.place(x=145, y= 30)
entry_angka2 = Entry(window, width=15)
entry_angka2.place(x=145, y=60)

tambah = Button(window, text="  +  ", command=penjumlahan).place(x=110, y = 90)
kurang = Button(window, text="  -  ",command = pengurangan).place(x=150, y = 90)
kali = Button(window, text="  x  ",command = perkalian).place(x=190, y = 90)
bagi = Button(window, text="  /  ",command = pembagian).place(x=230, y = 90)

window.mainloop()