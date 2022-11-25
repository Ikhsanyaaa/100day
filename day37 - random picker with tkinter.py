import random 
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("random picker")
window.geometry("500x400")
pilihan = []
def tampilkan_pilihan() : 
    global pilihan
    # for i in pilihan : 
    #     munculkan = Label(window, text=i)
    #     munculkan.place(x = 220, y = 70)
    munculkan_pilihan = Label(window, text= "yang anda masukkan adalah : ")
    munculkan_pilihan.place(x = 220, y = 70)
    munculkan = Label(window, text=pilihan)
    munculkan.place(x = 220,y = 90)
    tombol_acak = Button(window, text="acak", command=acak)
    tombol_acak.place(x = 220,y = 120)

def acak():
    index = random.randint(0,len(pilihan)-1)
    terpilih = pilihan[index]
    teks = Label(window, text="yang terpilih adalah")
    teks.place(x = 220,y = 150)
    hasil = Label(window, text=terpilih, bg="white", fg= "black", width=16)
    hasil.place(x = 220,y = 180)

def enter():
    masukan = buat.entry_masukkan.get()
    pilihan.append(masukan)
    lagi = Button(window,text = "lagi", command=lagii)
    lagi.place(x = 390, y = 40)
def lagii():
    text_masukkan = Label(window, text="masukkan hal yang ingin anca acak").place(x = 240, y = 10)
    buat.entry_masukkan = Entry(window, width = 20 )
    buat.entry_masukkan.place(x = 220, y = 40)
    oke = Button(window, text="enter", command=enter)
    oke.place(x = 350, y= 40)
    lagi = Button(window,text = "lagi", command=buat)
    lagi.place(x = 390, y = 40)
def buat():
    text_masukkan = Label(window, text="masukkan hal yang ingin anda acak").place(x = 240, y = 10)
    buat.entry_masukkan = Entry(window, width = 20 )
    buat.entry_masukkan.place(x = 220, y = 40)
    oke = Button(window, text="enter", command=enter)
    oke.place(x = 350, y= 40)


buat = Button(window,text="buat", command= buat)
buat.place(x = 10, y = 10)
tampilkan = Button(window,text="tampilkan", command=tampilkan_pilihan)
tampilkan.place(x = 50, y = 10)
window.mainloop()