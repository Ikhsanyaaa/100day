#program mengisi table mysql aaya 

import mysql.connector
data = []
database = input("pilih database : ")
table = input("pilih table : ")
collumn = int(input("masukkan jumlah kolom table : "))
db = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "")
cursor = db.cursor()
cursor.execute(f"use {database}")
while collumn > 0 : 
    record = input("masukkan record : ")
    tipedata_Record = int(input('''1. char/varchar/date
2. integer
masukkan tipe data record : '''))
    if tipedata_Record == 1:
        data.append(str(record))
        collumn -= 1
    elif tipedata_Record == 2:
        data.append(int(record))
        collumn -= 1
for i in data : 
    cursor.execute(f'''insert into {table}
values
({i})''')
