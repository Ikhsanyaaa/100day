import os

def rename():
    nama_file = str(input("masukkan nama file yang ingin diganti : "))
    format = str(input("masukkan format file : "))
    try : 
        file = open(f"{nama_file}.{format}","r")
    except FileNotFoundError :
        print("file tidak ditemukan!")
        rename()
    isi = file.read()
    new_file = str(input("masukkan nama baru : "))
    file = open(f"{new_file}.{format}","x")
    file = open(f"{new_file}.{format}","w")
    file.write(isi)
    file.close()
    os.remove(f"{nama_file}.{format}")
    print("nama file berhasil diganti")
    ulang()

def ulang():
    tanya = str(input("ingin mengganti file yang lain? (y/t) : "))
    if tanya == "y" : 
        rename()
    elif tanya == "t" :
        print("program selesai")
    else : 
        print("masukkan jawaban dengan benar!")
        ulang()

rename()