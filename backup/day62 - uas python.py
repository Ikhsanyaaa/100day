import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mkpython"
)

cursor = db.cursor()

# cursor.execute("create database mkpython")
print("database berhasil dibuat")
cursor.execute("use mkpython")
# cursor.execute('''create table nilai(nim char(10) not null,
# nama varchar(20) not null,
# alamat varchar(20) not null,
# jeniskelamin enum('p','l') not null)''')
# print("table berhasil dibuat")
# cursor.execute('''insert into nilai
# values
# ("d0221075","muhammad ikhsan","palece","l"),
# ("d0221327","imbar","malunda","l"),
# ("d0221270","intan sari","mateng","p"),
# ("d0221065","marhana","mateng","p"),
# ("d0221068","i putu andreana wirawan","mateng","l")''')
print("data behasil dimasukkan ke dalam database")