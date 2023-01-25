#program pencampur warna

import tkinter
from tkinter import *

window = tkinter.Tk()
window.geometry("500x400")
window.title("mencampur warna")

#red
red_label = Label(window, text="Red")
red_label.place(x = 10, y = 10)
red_entry = Spinbox(window, width=6, from_=0 , to=255)
red_entry.place(x = 50, y = 10)

#blue
blue_label = Label(window, text="blue")
blue_label.place(x = 10, y = 30)
blue_entry = Spinbox(window, width=16, from_=0 , to=255)
blue_entry.place(x = 50, y = 30)

#green
green_label = Label(window, text="Green")
green_label.place(x = 10, y = 50)
green_entry = Spinbox(window, width=16, from_=0 , to=255)
green_entry.place(x = 50, y = 50)


def tampilkan() :
    warna = red_entry.get() + blue_entry.get() + green_entry.get()
    warna_frame = str("#" + warna)
    print(warna_frame)
    teks = Label(window, text="warna yang dihasilkan")
    teks.place(x=220,y=10)
    frame = Canvas(window, width=160, height=160, bg=f"{warna_frame}")
    frame.place(x=220, y = 30)


tombol = Button(window, text="tampilkan warna", command=tampilkan)
tombol.place(x=10, y =70)



window.mainloop()