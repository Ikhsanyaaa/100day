import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("belajar tkinter")
window.geometry("500x400")

def terklik():
    messagebox.showinfo("selesai","data anda sudah direkam")

label_nama = Label(window, text= "memasukkan biodata", bg= "black", fg= "white").place(x= 200, y = 10)
label_nama = Label(window, text="nama").place(x= 10, y = 40)
label_nim = Label(window, text="nim").place(x= 10, y = 60)
entry_nama = Entry(window, width = 16).place(x= 50, y = 40)
entry_nim = Entry(window, width = 16).place(x= 50, y = 60)
label_jurusan = Label(window, text= "jurusan").place(x = 10, y = 80)
inf = Radiobutton(window, text ="informatika", value = 1).place(x= 100, y = 80)
pwk = Radiobutton(window, text ="pwk", value = 2).place(x= 200, y = 80)
sipil = Radiobutton(window, text ="teknik sipil", value = 3).place(x= 300, y = 80)
kipk = Checkbutton(window, text="penerima kip?").place(x=10, y = 100)
label_nilai = Label(window, text="masukkan nilai anda dalam skala 1-10 ").place(x=10,y=120)
nilai = Spinbox(window,from_=0, to=10).place(x=225, y=120)
submit = Button(window, text="kirim", command=terklik).place(x=10, y=140)
scale = Scale(length=400, from_=  0, to=100).place(x= 450)

window.mainloop()