#program mengisi table mysql aaya 

import mysql.connector
db = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "")
cursor = db.cursor()
cursor.execute("use prafinal")
cursor.execute(f'''insert into supplier
values
("SUP1","CV.IT.INDONESIA"),
("SUP2","CV.SW.INDONESIA"),
("SUP3","CV. MOBILER INDONESIA")''')
print("sudah")
db.commit()