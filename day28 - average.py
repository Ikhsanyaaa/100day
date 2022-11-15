#program mencari rata-rata
angka = []
def rata_rata():
    stop = False
    while stop == False : 
        masukkan = int(input("masukkan angka : "))
        angka.append(masukkan)
        while True : 
            tanya = str(input('''tekan y untuk menambahkan angka : 
tekan t untuk melihat hasil : '''))
            if tanya == "t" : 
                hasil = sum(angka) / len(angka)
                print("rata-rata nya adalah : ",hasil)
                stop = True
                break
            elif tanya == "y" :
                break
            else : 
                print("masukkan jawaban dengan benar")
rata_rata()

