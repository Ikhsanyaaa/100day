#fungsi untuk mengimport fungsi-fungsi didalam modul
import tkinter
from tkinter import *
from tkinter import messagebox


window = tkinter.Tk()  #membuat tampilan window
window.title("belajar tkinter")  #menentukan judul dari window
window.geometry("500x400")  #menentukan ukuran window


def terklik(): #membuat fungsi dimana aksinya adalah menampilkan pesan
    messagebox.showinfo("selesai","data anda sudah direkam")

label_bio = Label(window, text= "memasukkan biodata", bg= "black", fg= "white").place(x= 200, y = 10) #membuat judul dengan label
label_nama = Label(window, text="nama").place(x= 10, y = 40) #membuat tulisan nama dengan label
label_nim = Label(window, text="nim").place(x= 10, y = 60) #membuat tulisan nim dengan label
entry_nama = Entry(window, width = 16).place(x= 50, y = 40) #membuat entry/input nama dengan entry
entry_nim = Entry(window, width = 16).place(x= 50, y = 60) #membuat entry/input nim dengan entry
label_jurusan = Label(window, text= "jurusan").place(x = 10, y = 80)#membuat label jurusan dengan label

#membuat pilihan radiobox 
inf = Radiobutton(window, text ="informatika", value = 1).place(x= 100, y = 80) 
pwk = Radiobutton(window, text ="pwk", value = 2).place(x= 200, y = 80)
sipil = Radiobutton(window, text ="teknik sipil", value = 3).place(x= 300, y = 80)

kipk = Checkbutton(window, text="penerima kip?").place(x=10, y = 100) # membuat pilihan centang dengan checkbox
label_nilai = Label(window, text="masukkan nilai anda dalam skala 1-10 ").place(x=10,y=120) #membuat tulisan keterangan dengan label
nilai = Spinbox(window,from_=0, to=10).place(x=225, y=120) #membuat spinbox nilai
submit = Button(window, text="kirim", command=terklik).place(x=10, y=140) #membuat tombol/button kirim
scale = Scale(length=400, from_=  0, to=100).place(x= 450) #membuat scale yang ada di sebelah kanan window

window.mainloop() #berfungsi sebagai pengulang agar window berjalan terus menerus