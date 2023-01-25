#menampilkan bilangan ganjil yang bisa dibagi tiga kemudian hasilnya dijunmlahkan

nilai_awal = 1
n = int(input("masukkan batas angka yang ingin ditampilkan : "))
angka = []
for i in range(nilai_awal, (n+1)) :
    if i%2 != 0 and i%3 == 0 :
        angka.append(i)
print("angka yang memenuhi adalah : ",angka)
print("total penjumlahan dari semua angka diatas adalah : ",sum(angka))
