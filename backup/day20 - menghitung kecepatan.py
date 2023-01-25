#menghitung kecepatan rata-rata

jarak = int(input("masukkan jarak awal mula dengan tujuan (m) : "))
waktu = int(input("masukkan waktu tempuh dalam menit : "))
jam = waktu / 60
km = int((jarak/1000)/jam)
print("kecepatan anda adalah : ",km,"km/jam")