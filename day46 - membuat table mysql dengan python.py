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
print(nama,nim,umur, "berhasil ditambahkan!")
print("menampilkan data")
cursor.execute("select*from mhs")
hasil = cursor.fetchall()
for data in hasil : 
    print(data)
print("mengupdate data")
nim_baru = input("masukkan nim baru : ")
umur_baru = input("masukkan umur baru : ")
cursor.execute(f'''update mhs set nim = "{nim_baru}", umur = "{umur_baru}" where nama = "{nama}"''')
db.commit()
print("update berhasil!")
print("menghapus data")
data_hapus = input("masukkan data yang ingin dihapus")
field_hapus = input("masukkan field yang ingin dihapus : ")
cursor.execute(f"delete from mhs where {field_hapus} = {data_hapus}")
print("berhasil dihapus")
db.commit()