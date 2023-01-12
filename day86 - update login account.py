#membuat akun

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = ""
)
cursor = db.cursor()
cursor.execute("create database akun")
cursor.execute("use akun")
cursor.execute('''create table data(username char(10) not null primary key,
password varchar(20) not null)''')

def menu():
    print('''1. buat akun
2. login''')
    pilihan = int(input("masukkan kode menu diatas : "))
    if pilihan == 1 : 
        buat_akun()
    elif pilihan == 2 : 
        login()
    else : 
        print("masukkan pilihan dengan benar")
        menu()

def buat_akun():
    username = str(input("buat username anda : "))
    cursor.execute("select username from data")
    usrnme = cursor.fetchall()
    for i in usrnme :
        for j in i : 
            if j == username : 
                print("username telah digunakan")
                buat_akun()
    while True : 
        password = str(input("buat password : "))
        konfirmasi = str(input("konfirmasikan password anda : "))
        if konfirmasi != password : 
            print("konfirmasi password salah")
        else : 
            break
    cursor.execute(f'''insert into data
values
("{username}","{password}")''')
    db.commit()
    print("akun berhasil dibuat")
    menu()

def login():
    global username
    global password
    username = str(input("masukkan username anda : "))
    password = str(input("masukkan password anda : "))
    cursor.execute("select * from data")
    data = cursor.fetchall()
    ketemu = False
    for akun in data :
        panjang = len(data)
        index = 0
        while index < panjang : 
            if akun[0] == username and akun[1] == password : 
                ketemu = True
                break
            else : 
                ketemu == False
                index += 1
    if ketemu == True : 
        print("login berhasil, selamat datang",username)
        menu_utama()
    else :
        print("username/password salah")
        login()

def menu_utama():
    print('''1. update biodata
2. tampilkan biodata
3. ganti password
4. log out''')
    while True : 
        pilihan = int(input("masukkan kode menu : "))
        if pilihan == 1 : 
            update_biodata()
            break
        elif pilihan == 2 : 
            tampilkan_biodata()
            break
        elif pilihan == 3 :
            ganti_password()
            break
        elif pilihan == 4 : 
            print("berhasil log out")
            menu()
            break
        else :
            print("masukkan kode menu dengan benar!")


def update_biodata():
    cursor.execute('''alter table data
add nama_lengkap varchar(20) not null,
add umur int(3) not null,
add jenis_kelamin enum("laki-laki","perempuan") not null''')
    nama = str(input("nama lengkap : "))
    umur = int(input("umur: "))
    while True : 
        jk = str(input("jenis kelamin (l/p) : "))
        if jk == "l" : 
            jenis_kelamin = "laki-laki"
            break
        elif jk == "p" : 
            jenis_kelamin = "perempuan"
            break
        else : 
            print("masukkan kode p atau l saja")
    cursor.execute(f'''update data set nama_lengkap = "{nama}",
umur = {umur},
jenis_kelamin = "{jenis_kelamin}" where username = "{username}"''')
    db.commit()
    print("biodata berhasil diupdate!")
    menu_utama()

def tampilkan_biodata():
    cursor.execute(f"select nama_lengkap, umur, jenis_kelamin from data where username = '{username}'")
    biodata = cursor.fetchall()
    for bio in biodata : 
        print("nama lengkap : ",bio[0])
        print("umur : ",bio[1])
        print("jenis kelamin : ",bio[2])
    pilihan = str(input("ingin perbarui biodata? (y/t)"))
    if pilihan == "y" :
        update_biodata()
    elif pilihan == "t" : 
        menu_utama()

def ganti_password() : 
    password_lama = str(input("masukkan password lama anda : "))
    if password_lama != password : 
        print("password anda salah!")
        ganti_password()
    else : 
        password_baru = str(input("masukkan password baru : "))
        cursor.execute(f"update data set password = '{password_baru}' where password = '{password}'")
        db.commit()
        print("password berhasil diganti!")
        menu_utama()

menu()
