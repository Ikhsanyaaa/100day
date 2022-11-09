#dan hasilnya masih bisa di operasikan kembali

def lagi():
    global hasil
    while True : 
        operator = int(input('''1. penjumlahan
2. penguragan
3. perkalian
4. pembagian
5. keluar
pilih operator : '''))
        if operator == 1 : 
            angka2 = int(input("masukkan angka : "))
            hasil = hasil + angka2
            print(hasil)
            lagi()
        elif operator == 2 : 
            angka2 = int(input("masukkan angka : "))
            hasil = hasil - angka2
            print(hasil)
            lagi()
        elif operator == 3 : 
            angka2 = int(input("masukkan angka : "))
            hasil = hasil * angka2
            print(hasil)
            lagi()
        elif operator == 4 : 
            angka2 = int(input("masukkan angka : "))
            hasil = hasil / angka2
            print(hasil)
            lagi()
        elif operator == 5 : 
            print('program berakhir')
            break

        else : 
            print("masukkan pilihan dengan benar!")


angka1 = int(input("masukkan angka : "))
while True : 
    operator = int(input('''1. penjumlahan
2. penguragan
3. perkalian
4. pembagian
5. keluar
pilih operator : '''))
    if operator == 1 : 
        angka2 = int(input("masukkan angka : "))
        hasil = angka1 + angka2
        print(hasil)
        lagi()
    elif operator == 2 : 
        angka2 = int(input("masukkan angka : "))
        hasil = angka1 - angka2
        print(hasil)
        lagi()
    elif operator == 3 : 
        angka2 = int(input("masukkan angka : "))
        hasil = angka1 * angka2
        print(hasil)
        lagi()
    elif operator == 4 : 
        angka2 = int(input("masukkan angka : "))
        hasil = angka1 / angka2
        print(hasil)
        lagi()
    elif operator == 5 : 
        print('program berakhir')
        break
    else : 
        print("masukkan pilihan dengan benar!")