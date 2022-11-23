#membuat program pemilih random

import random

pilihan = []
selesai  = False
def membuat():
    global selesai
    while selesai == False : 
        udah = str(input("apakah anda ingin menambahkan ? (y/t) : "))       
        if udah == "t" : 
            selesai = True
        elif udah != "y" and udah != "t" :
            print("masukkan jawaban dengan benar")
        else : 
            tambahan = input("masukkan hal-hal yang ingin dipilih : ")
            pilihan.append(tambahan) 

def memilih():
    index_terpilih = random.randint(0,len(pilihan)-1)
    print("yang terpilih adalah : ",pilihan[index_terpilih])

membuat()
memilih()