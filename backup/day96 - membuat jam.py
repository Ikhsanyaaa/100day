import time

def tampilkan_jam():
    print("tekan ctrl + C pada terminal untuk kembali ke menu")
    while True : 
        try :
            waktu = time.localtime()
            jam = waktu.tm_hour
            menit = waktu.tm_min
            detik = waktu.tm_sec
            print(f"Waktu sekarang : {jam}:{menit}:{detik}")
            time.sleep(1)
        except KeyboardInterrupt :
            print("selesai")
            menu()

def stopwatch():
    print("tekan ctrl + C pada terminal untuk kembali ke menu")
    jam = 0
    menit = 0
    detik = 0
    while True : 
        try :     
            if detik == 60 : 
                detik -= 60
                menit += 1
            if menit == 60 : 
                menit -= 60
                jam += 1
            print(f"stopwatch : {jam}:{menit}:{detik}")
            detik += 1
            time.sleep(1)
        except KeyboardInterrupt :
            print("selesai")
            menu()

def menu():
    pil = int(input('''1. menampilkan jam
2. stopwatch
pilih menu diatas : '''))
    if pil == 1 : 
        tampilkan_jam()
    elif pil == 2 :
        stopwatch()
    else : 
        print("masukkan pilihan dengan benar!")
        menu()

menu()