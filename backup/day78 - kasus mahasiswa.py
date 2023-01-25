import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = ""
)
cursor = db.cursor()
cursor.execute("create database mahasiswa")
cursor.execute("use mahasiswa")
cursor.execute('''create table mhs(nim char(10) not null primary key,
nama varchar(20) not null,
prodi varchar(20) not null,
angkatan year not null)''')

def menu() : 
    print('''===data mahasiswa===
1. tambah mahasiswa
2. edit mahasiswa
3. delete mahasiswa
4. pencarian mahasiswa 
5. menampilkan data mahasiswa
6. keluar''')
    selesai = False
    while selesai == False : 
        pil = int(input("masukkan kode menu diatas : "))
        if pil == 1 : 
            tambah()
        elif pil == 2 : 
            edit()
        elif pil == 3 : 
            delete()
        elif pil == 4 : 
            pencarian()
        elif pil == 5 : 
            menampilkan()
        elif pil == 6 : 
            print("program selesai")
            selesai = True
            

def tambah():
    nim = str(input("masukkan nim mahasiswa : "))
    nama = str(input("masukkan nama mahasiswa : "))
    prodi = str(input("masukkan prodi mahasiswa : "))
    angkatan = str(input("masukkan tahun angkatan mahasiswa : "))
    cursor.execute(f'''insert into mhs
values
('{nim}','{nama}','{prodi}','{angkatan}')''')
    db.commit()
    print("data berhasil ditambahkan")
    while True : 
        lagi = str(input("masih ingin menambahkan? (y/t) : "))
        if lagi == "y" : 
            tambah()
        elif lagi == "t" : 
            menu()
        else : 
            print("masukkan pilihan dengan benar!")

def edit() : 
    ketemu = False
    field = int(input('''1. nim
2. nama
3. prodi
4. angkatan
masukkan field dari data yang ingin diganti : '''))
    if field == 1 : 
        field = "nim"
    elif field == 2 : 
        field = "nama"
    elif field == 3 : 
        field = "prodi"
    elif field == 4 : 
        field = "angkatan"
    else : 
        print("masukkan pilihan dengan benar!")
        edit()
    cari = str(input("masukkan record data yang ingin diganti : "))
    cursor.execute("select * from mhs")
    data = cursor.fetchall()
    panjang = len(data)
    if panjang > 1 : 
        while panjang > 1 : 
            data_baru = data[-1] + data[-2]
            panjang -= 1
            index = 0
            while index < len(data_baru) : 
                if cari == data_baru[index] : 
                    ketemu = True
                    break
                else : 
                    index += 1
    else : 
        for data_baru in data : 
            index = 0
            while index < len(data_baru) : 
                if cari == data_baru[index] : 
                    ketemu = True
                    break
                else :
                    index += 1      
    if ketemu == False : 
        print(cari,"tidak ada dalam data")
        menu()
    else : 
        data_baru = str(input("masukkan data baru : "))
        cursor.execute(f"update mhs set {field} = '{data_baru}' where {field} = '{cari}'")
        db.commit()
        print("data berhasil diganti")
        menu()

def delete():
    ketemu = False
    field = int(input('''1. nim
2. nama
3. prodi
4. angkatan
masukkan field dari data yang ingin dihapus : '''))
    if field == 1 : 
        field = "nim"
    elif field == 2 : 
        field = "nama"
    elif field == 3 : 
        field = "prodi"
    elif field == 4 : 
        field = "angkatan"
    else : 
        print("masukkan pilihan dengan benar!")
        edit()
    cari = str(input("masukkan record dari data yang ingin dihapus : "))
    cursor.execute("select * from mhs")
    data = cursor.fetchall()
    panjang = len(data)
    if panjang > 1 : 
        while panjang > 1 : 
            data_baru = data[-1] + data[-2]
            panjang -= 1
            index = 0
            while index < len(data_baru) : 
                if cari == data_baru[index] : 
                    ketemu = True
                    break
                else : 
                    index += 1 
    else : 
        for data_baru in data : 
            index = 0
            while index < len(data_baru) : 
                if cari == data_baru[index] : 
                    ketemu = True
                    break
                else :
                    index += 1     
    if ketemu == False : 
        print(cari,"tidak ada dalam data")
        menu()
    else : 
        cursor.execute(f"delete from mhs where {field} = '{cari}'")
        db.commit()
        print("data berhasil dihapus")
        menu()

def pencarian():
    ketemu = False
    cari = str(input("masukkan nim mahasiswa yang ingin dicari : "))
    cursor.execute("select * from mhs")
    data = cursor.fetchall()
    panjang = len(data)
    if panjang > 1 : 
        while panjang > 1 : 
            data_baru = data[-1] + data[-2]
            panjang -= 1
            index = 0
            while index < len(data_baru) : 
                if cari == data_baru[index] : 
                    ketemu = True
                    break
                else : 
                    index += 1 
    else : 
        for data_baru in data : 
            index = 0
            while index < len(data_baru) : 
                if cari == data_baru[index] : 
                    ketemu = True
                    break
                else :
                    index += 1

    if ketemu == False : 
        print(cari,"tidak ada dalam data")
        menu()
    else : 
        print("data ditemukan")
        cursor.execute(f"select * from mhs where nim like '%{cari}%'")
        mahasiswa = cursor.fetchall()
        for i in mahasiswa : 
            print(i)
        menu()

def menampilkan():
    cursor.execute("select*from mhs")
    data = cursor.fetchall()
    for i in data : 
        print("nim :",i[0],", nama :",i[1],", prodi :",i[2],", angkatan :",i[3])
        menu()

menu()
            
    


