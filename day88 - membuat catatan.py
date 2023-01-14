def menu():
    print('''1. membuat catatan baru
2. menulis catatan
3. menampilkan catatan
4. menghapus isi catatan''')
    pil = int(input("masukkan kode menu : "))
    if pil == 1 : 
        membuat()
    elif pil == 2 : 
        menulis()
    elif pil == 3 : 
        menampilkan()
    elif pil == 4 : 
        menghapus()
    else : 
        print("kode menu tidak ada!")
        menu()

def membuat():
    nama_file = str(input("buat judul catatan : "))
    catatan = open(f"{nama_file}.txt","x")
    print("catatan berhasil dibuat")
    menu()

def menulis():
    nama_file = nama_file = str(input("masukkan judul catatan : "))
    while True :
        teks = str(input(f"silahkan menulis teks\ntulis selesai untuk mengakhiri catatan\n"))
        if teks == "selesai" : 
            print("catatan berhasil dibuat!")
            break
        else : 
            catatan = open(f"{nama_file}.txt","a")
            catatan.write(f"\n{teks}")
            catatan.close()
        
    menu()

def menampilkan():
    nama_file = nama_file = str(input("masukkan judul catatan : "))
    catatan = open(f"{nama_file}.txt","r")
    print(catatan.read())
    catatan.close()
    pil = str(input("ingin menampilkan catatan lain? (y/t) : "))
    if pil == "y" : 
        menampilkan()
    elif pil == "t" : 
        menu()
    else : 
        print("kode eror")
        menu()

def menghapus():
    nama_file = nama_file = str(input("masukkan judul catatan : "))
    catatan = open(f"{nama_file}.txt","w")
    teks = ""
    catatan.write(teks)
    catatan.close()
    print("isi catatan berhasil dihapus")
    menu()

menu()