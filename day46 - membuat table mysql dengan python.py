import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "")
if db.is_connected():
    print("berhasil terhubung dengan database")
cursor = db.cursor()
cursor.execute("create database datates")
print("database berhasil dibuat!")
cursor.execute("use datates")
print("database berhasil digunakan!")
cursor.execute("create table mhs(nim char(10) not null primary key, nama varchar(20) not null, umur int(2) not null)")
print("table berhasil dibuat")
nim = input("masukkan nim anda : ")
nama = input("masukkan nama anda : ")
umur = input("masukkan umur anda : ")
cursor.execute(f'''insert into mhs 
values
("{nim}","{nama}",{umur})''')
db.commit()
print("data berhasil ditambahkan ke dalam database")