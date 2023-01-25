#membuat program countdown

import time

waktu = int(input("masukkan awal hitungan mundur : "))
while waktu >= 0 : 
    time.sleep(1)
    print("hitungan : ",waktu)
    waktu -= 1
print("hitungan mundur selesai")
        