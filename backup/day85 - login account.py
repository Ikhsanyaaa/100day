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
        menu()
    else :
        print("username/password salah")
        login()

menu()
