#membuat program penampil bilangan

def menu():
    pilihan = int(input('''
1. menampilkan bilangan genap
2. menampilkan bilangan ganjil
3. menampilkan bilangan prima
pilihlah menu diatas : '''))
    if pilihan == 1 :
        genap()
    elif pilihan == 2:
        ganjil()
    elif pilihan == 3 :
        prima()
    else :
        print("masukkan pilihan dengan benar!")
        menu() 

def ulang():
    while True : 
        tanya = str(input("apakah masih ingin mencari bilangan? (y/t) : "))
        if tanya == "y" : 
            menu()
        elif tanya == "t" :
            print("program berakhir")
            break
        else : 
            print("masukkan jawaban dengan benar!")

def genap():
    awal = int(input("masukkan bilangan awal : "))
    akhir = int(input("masukkan bilaangan akhir : "))
    batas = akhir + 1
    for i in range(awal, batas) :
        if i % 2 == 0 :
            print(i)
            ulang()

def ganjil():
    awal = int(input("masukkan bilangan awal : "))
    akhir = int(input("masukkan bilaangan akhir"))
    batas = akhir + 1
    for i in range(awal, batas) :
            print(i)
            ulang()

def prima():
    awal = int(input("masukkan bilangan awal : "))
    akhir = int(input("masukkan bilaangan akhir"))
    batas = akhir + 1
    for i in range(awal,batas):
        if (i==2 or i==3 or i==5 or i==7)or(i != 1 and i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 !=0) :
            print(i)
            ulang()

menu()
