import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "")
cursor = db.cursor()
field = []
def cek():
    if db.is_connected():
        print("berhasil terhubung dengan database")
def membuat():
    database = str(input("masukkan nama database : "))
    cursor.execute(f"create database {database}")
    print("database berhasil dibuat!")
    cursor.execute(f"use {database}")
print("database berhasil digunakan!")
def buat_table():
    global table
    table = str(input("masukkan nama table : "))
    nama_field = str(input("masukkan nama field : "))
    tipedata = str(input("masukkan tipe data field : "))
    karakter = int(input("masukkan batas karakter : "))
    cursor.execute(f'create table {table}({nama_field} {tipedata} ({karakter} not null)')
def menambah_field() : 
    global table
    global field
    nama_field = str(input("masukkan nama field : "))
    field.append(nama_field)
    tipedata = str(input("masukkan tipe data field : "))
    karakter = int(input("masukkan batas karakter : "))
    cursor.execute(f'''alter table {table}
add ({nama_field} {tipedata} ({karakter} not null)''')
def mengisi_field():
    global table
    field_cari = input("masukkan field yang ingin diisi")
    for i in field : 
        if i != field_cari :
            print(field_cari,"tidak ditemukan!")
        else : 
            print(f"masukkan isi dari field {field_cari}")
            data = input("masukkan isi record : ")
            cursor.execute(f'''update {table} set {field_cari} = '{data}' ''')
            db.commit()
            print("data berhasil ditambahkan ke dalam database")

def menu():
    pilih = str(input('''1.mengecek koneksi
2.membuat database
3.membuat table
4.menambah field
5.mengisi field'''))
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