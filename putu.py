import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "andreana"
)

andre=conn.cursor()

andre.execute('create database andre123')

        
andre.execute(
    '''
    create table buku(
    nama varchar (10) not null,
    nim char (10) not null,
    alamat varchar (10) not null
    )
    ''')


andre.execute(
    '''
    insert into buku(nama,nim,alamat)
    values
    ('putu','D0221068','topoyo'),
    ('hana','D0221089','topoyo')
    ''')

conn.commit()


andre.execute('select*from buku')
tampil = andre.fetchall()
for i in tampil:
    print(i)    

andre.execute("show databases")
tampil = andre.fetchall()
for i in tampil:
    print(i)

andre.execute('show tables')
tampil = andre.fetchall()
for i in tampil:
    print(i)

andre.execute('drop table buku')
andre.execute('drop database andreana')


print('program berhasil')