def mean():
    data = [0,2,2,1,0,7,5]
    print("data = ",data)
    n = len(data)
    print("n = ",n)
    while len(data) > 2 : 
        print(data)
        data_baru = data[0] + data[1]
        data[0] = data_baru
        del data[1] 
    print(data)
    sigma_x = data[0] + data[1]
    print("sigma x = ",sigma_x)
    mean = float(sigma_x / n)
    print("mean = {:.2f}".format(mean))
    menu()

def modus():
    data = [0,2,2,1,0,7,5]
    print("data = ",data)
    frekuensi = dict.fromkeys(data, 0)
    for key,value in frekuensi.items():
        for i in data : 
            if i == key : 
                frekuensi[key] += 1
    Modus = []
    frekuensi_terbanyak = 0
    print("jumlah frekuensi dari setiap data = ",frekuensi)
    for key,value in frekuensi.items():
        if value >= frekuensi_terbanyak : 
            frekuensi_terbanyak = key
        else : 
            pass
    for key,value in frekuensi.items():
        if value == frekuensi_terbanyak : 
            Modus.append(key)
    print("modus dari data tersebut adalah : ",Modus)
    menu()

def median():
    data = [0,2,2,1,0,7,5]
    print("data = ",data)
    n = len(data)
    for i in range(n):
        for j in range(n-i-1):
            if data[j] > data[j + 1] :
                data[j], data[j+1] = data[j+1] , data[j]
    print("data setelah diurutkan = ",data)
    if n % 2 != 0 :
        index_median = int((n+1)/2)
        print("median = ",data[index_median])
    else : 
        index_median = int((data[1+n/2] + data[1+1+n/2]) / 2)
        print("median = ",median[index_median])
    menu()

def menu():
    print("nama : Muhammad Ikhsan")
    print("nim : D0221075")
    pilih = int(input('''1. mean
2. modus
3. medium
4. keluar
pilih menu diatas dengan memasukkan nomer menu : '''))
    if pilih == 1:
        mean()
    elif pilih == 2:
        modus()
    elif pilih == 3:
        median()
    elif pilih == 4 :
        print("program berakhir")
    else : 
        print("masukkan pilihan dengan benar!")
        menu()

menu()

