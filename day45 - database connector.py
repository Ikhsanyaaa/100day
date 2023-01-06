import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "kr_d0221075")
if db.is_connected():
    print("berhasil terhubung")
cursor = db.cursor()
cursor.execute('''insert into dosen
values
("19901227201901","Dr.Sinta, M.kes","Majene",3,"002233","1990/12/27"),
("19901227201902","Dr. Mirna, S.si,M.Si","Polewali",2,"002244","1989/12/27"),
("19901227201903","Dr.Firman, S.Kom.,M.Kom","Majene",1,"002255","1980/12/27"),
("19901227201904","Dr. Herman S.Kom.,M.Kom","Mamuju",1,"002266","1970/12/27")
''')
db.commit()
print("ok")


