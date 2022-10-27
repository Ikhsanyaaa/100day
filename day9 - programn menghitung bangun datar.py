#program menghitung bangun ruang

def persegi_panjang():
    panjang = int(input("masukkan panjang dalam cm : "))
    lebar = int(input("masukkan lebar dalam cm : "))
    luas = panjang * lebar
    keliling = (panjang + lebar) * 2
    print("luas persegi panjang adalah : ",luas,"cm")
    print("keliling persegi panjang adalah : ", keliling,"cm") 

def persegi():
    rusuk = int(input("masukkan panjang rusuk dalam cm : "))
    luas = rusuk * rusuk
    keliling = 4 * rusuk
    print("luas persegi adalah : ", luas,"cm")
    print("keliling persegi adalah : ", keliling,"cm")

def segitiga():
    alas = int(input("masukkan panjang alas dalam cm : "))
    tinggi = int(input("masukkan tinggi segitiga dalam cm : "))
    sisi_miring = (((alas/2)**2 )+ tinggi**2) ** 0.5
    luas = alas * tinggi / 2
    keliling = (sisi_miring * 2) + alas
    print("luas segitiga adalah : ",luas,"cm")
    print("keliling segitiga adalah : ",keliling,"cm")

def lingkaran():
    diameter = int(input("masukkan panjang diameter lingkaran dalam cm : "))
    jari2 = diameter / 2
    phi =  22/7
    luas = phi * (jari2 ** 2)
    keliling = phi * diameter
    print("luas lingkaran adalah : ",luas,"cm")
    print("keliling lingkaran adalah : ",keliling,"cm")

print('''1. persegi
2. persegi panjang
3. segitiga 
4. lingkaran''')

objek = int(input("masukkan angka bangun datar yang ingin dicari : "))
if objek == 1 : 
    persegi()
elif objek == 2 : 
    persegi_panjang()
elif objek == 3 : 
    segitiga()
elif objek == 4 :
    lingkaran()
else :
    print("masukkan pilihan dengan benar!")
