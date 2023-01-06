#game tebak angka

import random

angka = random.randint(1,10)
kesempatan = 3 
while kesempatan > 0 : 
    print("kamu memiliki : ",kesempatan,"kesempatan untuk menebak angka dari 1 - 10")
    jawaban = int(input("masukkan jawaban 1 - 10 : "))
    if jawaban < angka : 
        print("tebakanmu terlalu kecil")
        kesempatan -= 1
    elif jawaban > angka : 
        print("tebakanmu terlalu besar")
        kesempatan -= 1
    else : 
        print("selamat jawaban anda benar!")
        break
if kesempatan == 0 :
    print("kesempatan habis, game berakhir")
