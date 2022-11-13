#membuat fungsi halo menggunakan library tkinter

import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("ehem ehem")
window.geometry("600x400")

def say_hello():
    tkinter.Label(window, text="haloo sinar:*").pack()
tkinter.Button(window, text= "klik disini!", command = say_hello).pack()

window.mainloop()