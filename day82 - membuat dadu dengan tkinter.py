#daduuu

import tkinter
from tkinter import *
import random

window = tkinter.Tk()
window.geometry("500x400")
window.title("pelempar dadu")

angka = random.randint(1,6)

def satu():
    global angka
    label_teks = Label(window, text=f"angka yang kaluar : {angka}")
    label_teks.place(x = 150, y =40)
    frame_dadu = Frame(window, width=160, height=160, bg="black")
    frame_dadu.place(x = 150, y = 70)
    canvas_titik = Canvas(window, width=140, height=140,bg="black")
    canvas_titik.place(x = 170, y =60)
    canvas_titik.create_oval(125,50,50,125, width=3, fill="white")

tombol_mulai = Button(text="tekan disini untuk melempar dadu", command=satu)
tombol_mulai.place(x = 150,y=10)





window.mainloop()