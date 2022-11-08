hasil = 0

def awal():
    operator = str(input("+ - x / "))
    if operator == "+" : 
        awal.angka2 = int(input("masukkan angka : "))
        penjumlahan()
        

def penjumlahan():
    global hasil
    hasil = angka1 + awal.angka2
    print(hasil)

angka1 = int(input("masukkana angka : "))
awal()