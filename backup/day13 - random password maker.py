import random  
import string
def membuat():
    huruf_kecil = string.ascii_lowercase
    huruf_besar = string.ascii_uppercase
    angka = string.digits
    semua = huruf_kecil + huruf_besar + angka
    panjang = int(input("masukkan panjang digit password : "))
    password = "".join(random.sample(semua, panjang))
    print("password anda adalah : ",password)
    ulang()

def ulang():
    tanya = str(input("apakah anda masih ingin membuat password (y/t) :"))
    if tanya == "y" :
        membuat()
    elif tanya == "t" :
        print("program berakhir")
    else : 
        print("masukkan jawaban dengan benar!")
        ulang()

membuat()