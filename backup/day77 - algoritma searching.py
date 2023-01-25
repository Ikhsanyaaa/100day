#algoritma searching

angka = [1,2,3,4,5,6,7,8,9]
ketemu = False
cari = int(input("masukkan angka : "))
panjang = len(angka)
index = 0
while index < panjang : 
    if cari == angka[index] : 
        ketemu = True
        break
    else : 
        index += 1

if ketemu == False : 
    print(cari,"tidak ada dalam angka")
else :
    print(cari,"ditemukan pada indeks ke-",index)