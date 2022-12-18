import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = ""
)
cursor = db.cursor()

cursor.execute("show databases")
databases = cursor.fetchall()
for i in databases : 
    print(i)