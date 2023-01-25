import time

def pasang_alarm():
    global jam, menit
    jam = int(input("pasang alarm pada jam : "))
    if jam < 0 or jam > 23 : 
        print("masukkan jam dengan format yang benar! (00-23)")
        pasang_alarm()
    else : 
        menit = int(input(f"jam {jam} menit? : "))
        if menit < 0 or menit > 59 : 
            print("masukkan menit dengan format yang benar!")
            pasang_alarm()
        else :
            hitung_waktu()

def hitung_waktu(): 
    while True : 
        waktu = time.localtime()
        jam_sekarang = waktu.tm_hour
        menit_sekarang = waktu.tm_min
        detik_sekarang = waktu.tm_sec
        if detik_sekarang == 60 : 
                detik_sekarang -= 60
                menit_sekarang += 1
        if menit_sekarang == 60 : 
            menit_sekarang -= 60
            jam_sekarang += 1
        detik_sekarang += 1
        time.sleep(1)
        if jam_sekarang == jam and menit_sekarang == menit : 
            print("alarm menyala!")
            break


pasang_alarm()