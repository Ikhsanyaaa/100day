import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = ''

)

cursor = con.cursor()
#cursor.execute('create database mk_python')
cursor.execute('use mk_python')

#cursor.execute('''
#create table nilai(
#nim char(10) not null,
#nama varchar(25) not null,
#alamat varchar(30) not null,
#jenis_kelamin enum ('l','p') not null)
#''')

#cursor.execute('''
#insert into nilai(nim,nama,alamat,jenis_kelamin)
#values
#('D0221074','muslih','jaksel','l'),
#('D0221073','jojo','sendana','l'),
#('D0221072','lee','bandung','l'),
#('D0221071','aqmal','bogor','l'),
#('D0221070','putu','topoyo','p')
#''')

#con.commit()

#cursor.execute('''
#update nilai set nim = 'D0221075',jenis_kelamin = 'l' where nama ='putu'
#''')

cursor.execute('''
delete from nilai where alamat ="topoyo"
''')

con.commit()



print('program berhasil')