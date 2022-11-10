#menmbah list
#menghapus list 
#mengedit list
#mencari list beserta indeks nya
#menampilkan indeks

barang = []

def menu():
    print("=" * 25)
    print("barang yang telah anda pilih : ")
    menampilkan()

    print('''
    1. menambahkan barang 
    2. menghapus barang yang telah dipilih
    3. mengganti barang yang telah dipilih
    4. mencari barang yang telah dipilih''')
    pilihan = int(input("selamat datang di toko kami, silahkan pilih menu diatas!"))
    if pilihan == 1 :
        menambah()
    elif pilihan == 2 :
        menghapus()
    elif pilihan == 3 :
        mengedit()
    elif pilihan == 4 :
        mencari()
    else :
        print("masukkan piilihan dengan benar!")
        menu()
def menambah():
    while True :
        barang_baru = str(input("masukkan barang yang ingin ditamnahkan : "))
        barang.append(barang_baru)
        udah = str(input("apakah anda masih ingin menambahkan barang (y/t) : "))
        if udah == "t":
            menu()
            break
        elif udah != "t" and udah != "y" :
            print("masukan pilihan dengan benar!")
            menu()

def menghapus():
    while True :
        barang_usang = str(input("masukkan barang yang ingin dihapus : "))
        barang.remove(barang_usang)
        udah = str(input("apakah anda masih ingin menghapus barang (y/t) : "))
        if udah == "t":
            menu()
            break
        elif udah != "t" and udah != "y" :
            print("masukan pilihan dengan benar!")
            menu()

def mengedit():
    cari = str(input("masukkan barang yang ingin diganti : "))
    ketemu = False
    for i in range(0, len(barang)):
        if cari == barang[i]:
            ketemu = True
            if ketemu :
                ganti = str(input("masukkan barang baru : "))
                barang [barang.index(cari)] = ganti
                print("barang sukses diganti")
                menu()
            else : 
                print("barang yang dimasukkan tidak ditemukan dalam list!")
                menu()
def mencari():
    cari = str(input("masukkan barang yang ingin dicari : "))
    ketemu = False
    for i in range(0, len(barang)):
        if cari == barang[i]:
            ketemu = True
            if ketemu  :
                print(cari, "ditemukan pada indeks : ", barang.index(cari))
                menu()
            else :
                print("barang", cari, "tidak ditemukan!")
                menu()

def menampilkan():
    for i in barang :
        print(i)

menu()