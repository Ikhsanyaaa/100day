# program set timer
import time

detik = 1
waktu = float(input("atur berapa menit yang anda inginkan"))
while detik != (waktu*60) :
    time.sleep(1)
    print("detik : ", detik)
    detik += 1
print("selesai")


