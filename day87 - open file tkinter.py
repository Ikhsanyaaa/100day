#membuat file teks dengan python
#pesan : jika sudah mengisi di menu 1, jika ingin menampilkan silahkan run ulang programnya dan pilih menu kedua

def menu() : 
    print("="*5,"menulis teks","="*5)
    print('''1.mengisi teks biodata
2. menampilkan teks biodata''')    
    pilih = int(input("masukkan kode menu diatas : "))
    if pilih == 1 : 
        menulis()
    elif pilih == 2 : 
        tampilkan()
    else : 
        print("masukkan kode menu dengan benar!")
        menu()
    

def menulis():
    from tkinter.filedialog import askopenfilename
    print("pilih file txt")
    nama_file = askopenfilename(filetypes=[("Text file","*.txt"),("All files","*.*")])
    file = open(nama_file, "w")
    nama = str(input("masukkan nama anda : "))
    nim = str(input("masukkan nim anda : "))
    umur = int(input("masukkan umur anda : "))
    teks = "Nama: {}\nUmur: {}\nNim: {}".format(nama, umur, nim)
    file.write(teks)
    file.close()
    print("teks berhasil ditulis")
    menu()


def tampilkan(): 
    from tkinter.filedialog import askopenfilename
    nama_file = askopenfilename(filetypes=[("Text file","*.txt"),("All files","*.*")])
    file = open(nama_file, "r")
    isi = file.read()
    print(isi)
    menu()

menu()

