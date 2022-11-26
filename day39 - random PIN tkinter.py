import tkinter
from tkinter import *
import random

PIN = []
window = tkinter.Tk()
window.title("random pin")
window.geometry("500x400")

def ganti():
    global PIN
    while len(PIN) > 0 :
        PIN.pop()
    a = 0
    digit = int(entry_digit.get())
    while a < digit : 
        angka = random.randint(1,9)
        PIN.append(angka)
        a += 1
    label_teks = Label(window, text="pin anda : ")
    label_teks.place(x=10, y=50)
    label_PIN = Label(window, text=PIN,bg="black", fg="white")
    label_PIN.place(x = 60, y = 50)
    button_ganti = Button(window, text="ganti", command=buat_pin2)
    button_ganti.place(x = 60,y = 70)

def buat_pin2():
    global PIN
    while len(PIN) > 0 :
        PIN.pop()
    a = 0
    digit = int(entry_digit.get())
    while a < digit : 
        angka = random.randint(1,9)
        PIN.append(angka)
        a += 1
    label_teks = Label(window, text="pin anda : ")
    label_teks.place(x=10, y=50)
    label_PIN = Label(window, text=PIN,bg="black", fg="white")
    label_PIN.place(x = 60, y = 50)
    button_ganti = Button(window, text="ganti", command=ganti)
    button_ganti.place(x = 60,y = 70)
label_digit = Label(window, text="berapa digit pin yang anda inginkan")
label_digit.place(x=10, y=10)
entry_digit = Entry(window, width=16)
entry_digit.place(x=10, y= 35)
konfir = Button(window, text="konfirmasi", command=buat_pin2)
konfir.place(x = 120, y= 30)

window.mainloop()