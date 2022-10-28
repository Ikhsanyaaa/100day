#program menghitung bangun ruang

def balok():
    panjang = int(input("masukkan panjang dalam cm : "))
    lebar = int(input("masukkan lebar dalam cm : "))
    tinggi = int(input("masukkan tinggi dalam cm : "))
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 *(panjang * lebar + panjang * tinggi + lebar * tinggi)
    print("volume balok adalah : ",volume, "cm")
    print("luas permukaan balok adalah",luas_permukaan, "cm") 

def kubus():
    rusuk = int(input("masukkan panjang rusuk dalam cm : "))
    volume = rusuk * rusuk * rusuk
    luas_permukaan = 6 * (rusuk) ** 2
    print("volume kubus adalah : ",volume, "cm")
    print("luas permukaan kubus adalah : ", luas_permukaan, "cm")

def tabung():
    diameter = int(input("masukkan panjang diameter lingkaran dalam cm : "))
    tinggi = int(input("masukkan tinggi dalam cm : "))
    jari2 = diameter / 2
    phi =  22/7 
    luas_alas = phi * (jari2 ** 2)
    volume = luas_alas * tinggi
    luas_permukaan = 2 * phi * jari2 * (jari2 + tinggi)
    print("volume tabung adalah : ",volume,"cm")
    print("luas permukaan tabung adalah : ",luas_permukaan,"cm")

def kerucut():
    diameter = int(input("masukkan panjang diameter lingkaran dalam cm : "))
    tinggi = int(input("masukkan tinggi dalam cm : "))
    jari2 = diameter / 2
    phi =  22/7 
    luas_alas = phi * (jari2 ** 2)
    sisi_miring = (((diameter/2)**2 )+ tinggi**2) ** 0.5
    luas_selimut = phi * jari2 * sisi_miring
    volume = 1/3 * luas_alas
    luas_permukaan = luas_alas + luas_selimut
    print("volume kerucut adalah : ",volume,"cm")
    print("luas permukaan kerucut adalah : ",luas_permukaan,"cm")

print('''1. kubus
2. balok
3. tabung 
4. kerucut''')
def menu():
    objek = int(input("masukkan angka bangun datar yang ingin dicari : "))
    if objek == 1 : 
        kubus()
    elif objek == 2 : 
        balok()
    elif objek == 3 : 
        tabung()
    elif objek == 4 :
        kerucut()
    else :
        print("masukkan pilihan dengan benar!")

menu()
