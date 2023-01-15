import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

cursor = db.cursor()

def pilih_database():
    cursor.execute("show databases")
    databases = cursor.fetchall()
    for database in databases :
        for data in database : 
            print(data)
    pilih = str(input("pilih database : "))
    ketemu = False
    for database in databases :
        for data in database : 
            panjang = len(database)
            index = 0
            while index < panjang : 
                if data == pilih : 
                    ketemu = True
                    break
                else : 
                    ketemu == False
                    index += 1
    if ketemu == True : 
        cursor.execute(f"use {pilih}")
        pilih_table()
    else :
        print("database tidak ada")
        pilih_database()

def pilih_table():
    global nama_table
    cursor.execute("show tables")
    tables = cursor.fetchall()
    for table in tables : 
        for tab in table : 
            print(tab)

    nama_table = str(input("pilih table : "))
    ketemu = False
    for table in tables : 
        for tab in table :   
            panjang = len(table)
            index = 0
            while index < panjang : 
                if tab == nama_table : 
                    ketemu = True
                    break
                else : 
                    ketemu == False
                    index += 1
    if ketemu == True : 
        cetak()
    else :
        print("table tidak ditemukan!")
        pilih_database()

def cetak():
    #membuat file
    nama_file = str(input("buat nama file : "))
    catatan = open(f"{nama_file}.txt","x")
    #mencetak file
    cursor.execute(f"desc {nama_table}")
    isi = cursor.fetchall()
    field = []
    for i in isi :       
        field.append(i[0])
 
    catatan = open(f"{nama_file}.txt","a")
    for i in field : 
        teks = i.center(20,"-")
        catatan.write("+")
        catatan.write(f"{teks}")
    
    panjang_field = len(field)
    index = 0 
    cursor.execute(f"select * from {nama_table}")
    data = cursor.fetchall()
    for i in data :
        while index < panjang_field :
            record = data[index]
            catatan.write(f"\n")
            for i in record : 
                i = str(i)
                teks = i.center(20,"-")
                catatan.write("|")
                catatan.write(f"{teks}")
            catatan.write(f"\n")
            index += 1
    print("catatan database berhasil dibuat")
    catatan.close()

pilih_database()
    



