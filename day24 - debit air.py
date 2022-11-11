# program debit air
def debit() : 
    panjang = int(input("masukkan panjang bak mandi dalam cm: "))
    lebar = int(input("masukkan lebar bak mandi dalam cm: "))
    tinggi = int(input("masukkan tinggi bak mandi dalam cm: "))
    volume = (panjang * lebar * tinggi) / 10
    waktu = int(input("berapa lama hingga air mengisi bak anda dalam menit : "))
    debit_air = volume / (waktu * 60)
    print("debit air anda adalah : ",debit_air,"liter/detik")
    menu()

def mengisi():
    panjang = int(input("masukkan panjang bak mandi dalam cm: "))
    lebar = int(input("masukkan lebar bak mandi dalam cm: "))
    tinggi = int(input("masukkan tinggi bak mandi dalam cm: "))
    volume = (panjang * lebar * tinggi) / 10
    debit = int(input("masukkan debit air perdertik : "))
    waktu = int(volume / (debit * 60))
    print("bak anda akan terisi penuh dalam waktu : ",waktu,"menit")
    menu()

def menu():
    pilihan = int(input('''1. menghitung debit air
2. menghitung lama pengisian bak air
3. keluar
pilihlah menu diatas : '''))
    if pilihan == 1 :
        debit()
    elif pilihan == 2 :
        mengisi()
    elif pilihan == 3 :
        print("program berakhir")

menu()

