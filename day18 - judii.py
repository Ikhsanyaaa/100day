#judi ganjil genap

import random 

uang = 100000
def hasil():
    global uang
    mata_dadu = random.randint(1,6)
    if mata_dadu % 2 == 0 : 
        angka = "genap"
        print("dadu yang naik adalah angka : ",angka)
    else : 
        angka = "ganjil"
        print("dadu yang naik adalah angka : ",angka)
    if game.pilihan == angka :
        print("anda benar!")
        uang = 2 + menu.taruhan*2
        print("sisa uang anda adalah : ",uang)
        ulang()
    else : 
        print("anda salah")
        print("sisa uang anda adalah : ",uang)
        ulang()
    

def game():
    while True :
        pilihan = int(input('''1. ganjil
2. genap
masukkan pilihan anda : '''))
        if pilihan == 1 :
            game.pilihan = "ganjil"
            hasil()
        elif pilihan == 2 : 
            game.pilihan = "genap"
            hasil()
        else : 
            print("pilihlah salah satu angka diatas!")

def menu():
    print('''welcome to judi gaming
disini kita akan bermain dadu
tebaklah angka dadu yang keluar
apakah ganjil atau genap? ''')
    global uang 
    print("uang anda sekarang : ",uang)
    while True : 
        menu.taruhan = int(input("masukkan jumlah taruhan anda : "))
        if menu.taruhan > uang :
            print("uang anda tidak cukup")
        else : 
            uang = uang - menu.taruhan
            game()

def ulang():
    while True : 
        tanya = str(input("masih ingin bermain? (y/t) : "))
        if tanya == "y" :
            menu()
        elif tanya == "t" : 
            print("game selesai!")
        else : 
            print("masukkan pilihan dengan benar!")

menu()