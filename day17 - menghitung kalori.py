#program menghitung kebutuhan kalori

def laki():
    berat = float(input("masukkan berat badan anda dalam kilogram : "))
    tinggi = float(input("masukkan tinggi badan anda dalam cm : "))
    usia = float(input("masukkan usia anda sekarang : "))
    while True : 
        keseharian = int(input("dari skala 1 - 8, seberapa aktif anda beraktivitas atau berolahraga : "))
        if keseharian == 1 : 
            aktivitas = 1.2
            break
        elif keseharian == 2 : 
            aktivitas = 1.3
            break
        elif keseharian == 3 : 
            aktivitas = 1.4
            break
        elif keseharian == 4 : 
            aktivitas = 1.5
            break
        elif keseharian == 5 : 
            aktivitas = 1.6
            break
        elif keseharian == 6 : 
            aktivitas = 1.7
            break
        elif keseharian == 7 : 
            aktivitas = 1.8
            break
        elif keseharian == 8 : 
            aktivitas = 1.9
            break
        else : 
            print("pilihan tersebut tidak tersedia")
    BMR = 66.5 + (13.75 * berat) + (5.003 * tinggi) - (6.75 * usia)
    kalori = BMR * aktivitas
    print(nama,"kebutuhan kalori anda adalah sebanyak : ",kalori,"kkal")

def wanita():
    berat = float(input("masukkan berat badan anda dalam kilogram : "))
    tinggi = float(input("masukkan tinggi badan anda dalam cm : "))
    usia = float(input("masukkan usia anda sekarang : "))
    while True : 
        keseharian = int(input("dari skala 1 - 8, seberapa aktif anda beraktivitas atau berolahraga : "))
        if keseharian == 1 : 
            aktivitas = 1.2
            break
        elif keseharian == 2 : 
            aktivitas = 1.3
            break
        elif keseharian == 3 : 
            aktivitas = 1.4
            break
        elif keseharian == 4 : 
            aktivitas = 1.5
            break
        elif keseharian == 5 : 
            aktivitas = 1.6
            break
        elif keseharian == 6 : 
            aktivitas = 1.7
            break
        elif keseharian == 7 : 
            aktivitas = 1.8
            break
        elif keseharian == 8 : 
            aktivitas = 1.9
            break
        else : 
            print("pilihan tersebut tidak tersedia")
    BMR = 665.1 + (9.563 * berat) + (1.850 * tinggi) - (4.676 * usia)
    kalori = BMR * aktivitas
    print(nama,"kebutuhan kalori anda adalah sebanyak : ",kalori,"kkal")

nama = str(input("masukkan nama anda : "))
while True : 
    gender = int(input('''1. laki-laki
2. wanita
pilih gender anda : '''))
    if gender == 1 :
        laki()
        break
    elif gender == 2 : 
        wanita()
        break
    else : 
        print("masukkan pilihan dengan benar!")