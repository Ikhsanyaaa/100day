berhenti = True

def menu():
    print("selamat datangdi program beasiswa unsulbar")
    print()
    print("Silahkan masukkan identitas anda")
    nama=input("masukkan nama anda :")
    nim=input("Masukkan nim anda (tanpa titik) :")
    print()

    pilih = 1
    while pilih != 0:
        print("Daftar beasiswa yang tersedia")
        print("1.Beasiswa berprestasi")
        print("2.Beasiswa kurang mampu")
        
        pilih=int(input("Masukkan pilihan anda (1/2):"))
        print()
        if pilih == 1:
            nilai = float(input("Masukkan nilai IPK :"))
            if nilai >= 3.5:
                print("\n\n")
                print("NAMA\t:",nama)
                print("NIM\t :",nim)
                print()
                print("Selamat anda lolos seleksi beasiswa Berprestasi")
                print("\n\n")
            else:
                print("Mohon maaf anda belum lolos seleksi beasiswa berprestasi")
            
        elif pilih == 2:
            penghasilan=int(input("Masukkan penghasilan orang tua perbulan (tanpa titik) :"))
            if penghasilan <= 1500000:
                print("\n\n")
                print("NAMA\t:",nama)
                print("NIM\t:",nim)
                print()
                print("Selamat anda lolos seleksi beasiswa kurang mampu")
                print("\n\n")
            else:
                print("Mohon maaf anda belum lolos seleksi beasiswa kurang mampu")
                print()
            ulang()
                
        else:
            print("Masukkan pilihan anda dengan benar!")
            print()
def ulang():
    while True:
        kembali = input("Apakah ingin memeriksa Kembali seleksi [y/t] :")
        if kembali == 'y' or kembali == 'Y':
            menu()
        elif kembali == 't' or kembali == 'T':
            global berhenti
            berhenti = False
            break
        else:
            print("Masukkan pilihan dengan benar!")      
menu()