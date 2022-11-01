def buat_akun():
    while True : 
        pin_baru = int(input("buat pin anda : "))
        if len(str(pin_baru)) != 6 :
            print("masukkan pin sebanyak 6 digit!")
        else : 
            pin = pin_baru
            return pin