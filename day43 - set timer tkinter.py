import tkinter
from tkinter import *
import time

window = tkinter.Tk()
window.geometry("500x400")

def mulai():
    waktu = int(spinbox_waktu.get())
    detik = waktu*60
    while 0 < detik :
        time.sleep(1)
        label_teks = Label(window, text ="sisa waktu : ")
        label_teks.place(x=10, y = 40)
        label_detik = Label(window, text=detik,bg="black",fg="white")
        label_detik.place(x = 70,y = 40)
        detik -= 1
    selesai = Label(window, text="Waktu habis!")
    selesai.place(x=10, y = 70)

label_waktu = Label(window, text="atur waktu dalam menit : ")
label_waktu.place(x=10,y=10)
spinbox_waktu = Spinbox(window, from_=1,to=100000, width=4)
spinbox_waktu.place(x = 150,y = 10)
tombol_mulai = Button(window,text="mulai",command=mulai)
tombol_mulai.place(x=200,y=10)
window.mainloop()