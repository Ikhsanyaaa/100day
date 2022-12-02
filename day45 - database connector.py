import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "")
if db.is_connected():
    print("berhasil terhubung")
cursor = db.cursor()
cursor.execute("create database datates")
print("database berhasil dibuat!")
cursor.execute("use datates")
print("database berhasil digunakan!")
cursor.execute("create table andre(nim char(10) not null primary key, nama varchar(20) not null, umur int(2) not null)")
print("table berhasil dibuat")



