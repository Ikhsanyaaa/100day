class luas_bangun():
    def persegi():
        sisi = float(input("masukkan panjang sisi : "))
        luas = sisi * sisi
        print("luas persegi : ",luas)
        luas_bangun.ulang()

    def segitiga():
        alas = float(input("masukkan panjang alas : "))
        tinggi = float(input("masukkan tinggi : "))
        luas = alas * tinggi / 2
        print("luas segitiga : ",luas)
        luas_bangun.ulang()

    def lingkaran():
        jari2 = float(input("masukkan panjang jari-jari : "))
        if jari2 % 7 == 0 : 
            phi = 22/7
        else : 
            phi = 3.14
        luas = phi * jari2 * jari2
        print("luas lingkaran : ",luas)
        luas_bangun.ulang()

    def menu():
        print("="*10, "menu", "="*10)
        print('''1. persegi
2. segitiga 
3. lingkaran
4.menu sebelumnya''')
        pilih = int(input("masukkan kode menu : "))
        if pilih == 1 : 
            luas_bangun.persegi()
        elif pilih == 2 : 
            luas_bangun.segitiga()
        elif pilih == 3 : 
            luas_bangun.lingkaran()
        elif pilih == 4 : 
            menu.menu_awal()
        else : 
            luas_bangun.menu()

    def ulang() : 
        tanya = str(input("apakah anda masih ingin menghitung luas bangun? (y/t) : "))
        if tanya == "y" : 
            luas_bangun.menu()
        elif tanya == "t" : 
            print("program selesai")
        else : 
            print("kode yang anda masukkan salah, pilih antara y atau t ")
            luas_bangun.ulang()

class volume_bangun():
    def balok():
        panjang = float(input("masukkan panjang : "))
        lebar = float(input("masukkan lebar : "))
        tinggi = float(input("masukkan tinggi : "))
        volume = panjang * tinggi * lebar
        print("volume balok = ",volume)
        volume_bangun.ulang()

    def limas():
        alas_segitiga = float(input("masukkan panjang alas segitiga : "))
        tinggi_segitiga = float(input("masukkan tinggi alas segitiga : "))
        luas_alas = alas_segitiga * tinggi_segitiga / 2
        tinggi_limas = float(input("masukkan tinggi limas : "))
        volume = 1/3 * (luas_alas * tinggi_limas)
        print("volume limas segitiga : ",volume)
        volume_bangun.ulang()

    def tabung():
        jari2 = float(input("masukkan panjang jari-jari lingkaran : "))
        tinggi = float(input("masukkan tinggi tabung : "))
        if jari2 % 7 == 0 :
            phi = 22/7
        else : 
            phi = 3.14
        luas_alas = phi * jari2 * jari2
        volume = luas_alas * tinggi
        print("volume tabung = ",volume)
        volume_bangun.ulang()

    def menu():
        print("="*10, "menu", "="*10)
        print('''1. balok
2. limas segitiga 
3. tabung
4.menu sebelumnya''')
        pilih = int(input("masukkan kode menu : "))
        if pilih == 1 : 
            volume_bangun.balok()
        elif pilih == 2 : 
            volume_bangun.limas()
        elif pilih == 3 : 
            volume_bangun.tabung()
        elif pilih == 4 : 
            menu.menu_awal()
        else : 
            volume_bangun.menu()

    def ulang() : 
        tanya = str(input("apakah anda masih ingin menghitung volume bangun? (y/t) : "))
        if tanya == "y" : 
            volume_bangun.menu()
        elif tanya == "t" : 
            print("program selesai")
        else : 
            print("kode yang anda masukkan salah, pilih antara y atau t ")
            volume_bangun.ulang()


class menu() : 
    def menu_awal():
        print("="*10, "menu", "="*10)
        print("menghitung luas dan volume")
        print('''1. menghitung luas bangun datar
2. menghitung volume bangun ruang''')
        pilih = int(input("masukkan kode menu : "))
        if pilih == 1 : 
            luas_bangun.menu()
        elif pilih == 2 : 
            volume_bangun.menu()
        else : 
            print("kode yang anda masukkan salah!")
            menu.menu_awal()
            
menu.menu_awal()
            
