stack = []

def menu():
    print('''==== stack data ===
1. menambah stack
2. mengeluarkan stack
3. menampilkan data stack
4. mencari isi stack
5. keluar''')
    while True : 
        pilihan = int(input("masukkan kode menu diatas : "))
        if pilihan == 1 :
            menambah()
        elif pilihan == 2 : 
            mengeluarkan()
        elif pilihan == 3 : 
            menampilkan()
        elif pilihan == 4 : 
            mencari()
        elif pilihan == 5 : 
            print("program selesai")
            break

def menambah():
    data = str(input("masukkan data yang ingin ditumpuk : "))
    stack[:0] = [data]
    print("data berhasil dimasukkan kedalam stack")
    while True : 
        lagi = str(input("ingin tambahkan lagi? (y/t) : "))
        if lagi == "y" : 
            menambah()
        elif lagi == "t" : 
            menu()
        else : 
            print("masukkan jawaban dengan benar!")

def mengeluarkan():
    while True : 
        lagi = str(input("apakah anda ingin mengeluarkan satu data tumpukan (y/t) : "))
        if lagi == "y" :
            print("berhasil mengeluarkan",stack[0]) 
            del stack[0]
        elif lagi == "t" : 
            print("kembali ke menu")
            menu()
        else : 
            print("masukkan pilihan dengan benar!")

def menampilkan():
    print("panjang tumpukan : ",len(stack))
    print("data dalam tumpukan : ")
    print("====")
    for i in stack : 
        print(i)
    print("====")
    menu()

def mencari():
    ketemu = False
    cari = str(input("masukkan data yang ingin dicari : "))
    panjang = len(stack)
    index = 0
    while index < panjang : 
        if cari == stack[index] : 
            ketemu = True
            break
        else : 
            index += 1

    if ketemu == False : 
        print("data",cari,"tidak ada dalam tumpukan!")
    else :
        print("data",cari,"ditemukan pada indeks ke-",index)
    
    while True : 
        lagi = str(input("ingin mencari lagi? (y/t) : "))
        if lagi == "y" : 
            mencari()
        elif lagi == "t" : 
            menu()
            break
        else : 
            print("masukkan jawaban dengan benar!")

menu()