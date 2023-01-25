import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "")
cursor = db.cursor()
field = []
def cek():
    if db.is_connected():
        print("berhasil terhubung dengan database")
        menu()
def membuat():
    database = str(input("masukkan nama database : "))
    cursor.execute(f"create database {database}")
    print("database berhasil dibuat!")
    cursor.execute(f"use {database}")
    print("database berhasil digunakan!")
    menu()
def buat_table():
    global table
    table = str(input("masukkan nama table : "))
    nama_field = str(input("masukkan nama field : "))
    tipedata = str(input("masukkan tipe data field : "))
    karakter = int(input("masukkan batas karakter : "))
    field.append(nama_field)
    cursor.execute(f'create table {table}({nama_field} {tipedata} ({karakter}) not null)')
    menu()
def menambah_field() : 
    global table
    global field
    nama_field = str(input("masukkan nama field : "))
    field.append(nama_field)
    tipedata = str(input("masukkan tipe data field : "))
    karakter = int(input("masukkan batas karakter : "))
    cursor.execute(f'''alter table {table}
add ({nama_field} {tipedata} ({karakter}) not null)''')
    menu()
def mengisi_field():
    global table
    nim = input("masukkan nim : ")
    nama = input("masukkan nama : ")
    cursor.execute(f'''insert into {table}
values
("{nim}","{nama}")''')
    print("data berhasil ditambahkan ke dalam database")
    db.commit()
    menu()

def mengupdate():
    global table
    global field
    field_cari = input("masukkan field data yang ingin di update : ")
    for i in field : 
        if i != field_cari :
            print(field_cari,"tidak ditemukan!")
        else : 
            data_baru = input("masukkan data baru : ")
            cursor.execute(f'''update {table} set {field_cari} = "{data_baru}"''')
            print("data berhasil di update")
            db.commit()
            menu()

def menghapus():
    global table
    global field
    field_cari = input("masukkan field data yang ingin dihapus : ")
    for i in field : 
        if i != field_cari :
            print(field_cari,"tidak ditemukan!")
        else : 
            cursor.execute(f"select*from {table}")
            hasil = cursor.fetchall()
            data_hapus = input("masukkan data yang ingin dihapus : ")
            for i in hasil : 
                if i != data_hapus :
                    print(field_cari,"tidak ditemukan!")
                    cursor.execute(f'''delete from {table} where {field_cari} = "{data_hapus}"''')
                    print("data berhasil dihapus")
                    db.commit()
                    menu()

def menampilkan():
    global table
    global field
    cursor.execute(f"select*from {table}")
    hasil = cursor.fetchall()
    for i in hasil : 
        print(i)
        menu()

def menu():
    pilih = int(input('''======menu======
1.mengecek koneksi
2.membuat database
3.membuat table
4.menambah field
5.mengisi field
6. mengupdate
7. menghapus
8. menampilkan
masukkan menu diatas : '''))
    if pilih == 1 : 
        cek()
    elif pilih == 2 : 
        membuat()
    elif pilih == 3 :
        buat_table()
    elif pilih == 4 : 
        menambah_field()
    elif pilih == 5 : 
        mengisi_field()
    elif pilih == 6 : 
        mengupdate()
    elif pilih == 7 : 
        menghapus()
    elif pilih == 8 : 
        menampilkan()

menu()