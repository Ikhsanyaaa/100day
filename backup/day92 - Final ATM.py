import mysql.connector
import random

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = ""
)
cursor = db.cursor()
# cursor.execute("create database ATM")
cursor.execute("use ATM")
# cursor.execute('''create table data(no_rekening char(20) not null primary key,
# nama varchar(20) not null,
# pin varchar(6) not null,
# saldo int(20) not null)''')

def buat_akun():
    no_rek = []
    pin = []
    saldo = 0
    print("silahkan  buat akun anda terlebih dahulu")
    nama = str(input("masukkan nama : "))

    #membuat no rekening acak menggunakan random
    while len(no_rek) < 10 : 
        angka = random.randint(0,9)
        no_rek.append(str(angka))
    no_rek = [no_rek[0] + no_rek[1] + no_rek[2] + no_rek[3] + no_rek[4] + no_rek[5] + no_rek[6] + no_rek[7] + no_rek[8] + no_rek[9]]
    no_rek = no_rek[0]

    #membuat pin acak menggunakan random
    while len(pin) < 6 : 
        angka = random.randint(0,9)
        pin.append(str(angka))
    pin = [pin[0] + pin[1] + pin[2] + pin[3] + pin[4] + pin[5]]
    pin = pin[0]
    print("akun anda berhasil dibuat : ")
    data = f'''nama : {nama}
nomor rekening : {no_rek}
PIN : {pin}
saldo : Rp.{saldo}'''

    #mencetak akun dalam txt biar tidak lupa 
    akun = open(f"data ATM {nama}.txt","x")
    akun.write(data)
    akun.close()
    print("silahkan memeriksa file txt untuk melihat data anda")

    #memasukkan data ke dalam database
    cursor.execute(f'''insert into data
values
("{no_rek}","{nama}","{pin}",{saldo})''')
    db.commit()

def login():
    global pin
    global no_rek
    no_rek = str(input("masukkan no rekening anda : "))
    pin = str(input("masukkan pin anda : "))
    cursor.execute("select no_rekening,pin from data")
    data = cursor.fetchall()
    ketemu = False
    for akun in data :
        panjang = len(data)
        index = 0
        while index < panjang : 
            if akun[0] == no_rek and akun[1] == pin : 
                ketemu = True
                break
            else : 
                ketemu == False
                index += 1
    if ketemu == True : 
        print("login berhasil, selamat datang")
        menu()
    else :
        print("no_rek/password salah")
        login()

def menu():
    masukkan_pin()
    print('''1. setoran tunai
2. penarikan
3. transfer uang
4. ganti pin
5. keluar''')
    pilih = int(input("masukkan kode menu : "))
    if pilih == 1 : 
        setoran()
    elif pilih == 2 : 
        penarikan()
    elif pilih == 3 :
        transfer()
    elif pilih == 4 : 
        ganti_pin()
    elif pilih == 5 : 
        print("silahkan ambil kartu ATM anda")
    else : 
        print("masukkan kode menu dengan benar!")
        menu()

def masukkan_pin():
    kesempatan = 3
    while kesempatan != 0 : 
        if kesempatan == 1 : 
            print("jika salah memasukkan pin sekali lagi, atm anda akan terblokir")
        masukkan = str(input("masukkan pin : "))
        if masukkan != pin : 
            print("pin yang anda masukkan salah!")
            kesempatan -= 1
        else : 
            break

def setoran():
    uang = int(input("silahkan masukkan uang anda : "))
    #mengupdate saldo dalam database
    cursor.execute(f"select saldo from data where no_rekening = '{no_rek}'")
    saldo = cursor.fetchall()
    for i in saldo : 
        for j in i : 
            saldo = j
    uang_sekarang = saldo + uang
    cursor.execute(f"update data set saldo = {uang_sekarang} where no_rekening = '{no_rek}'")
    db.commit()
    while True : 
        tanya = str(input("apakah anda ingin mencetak struk? (y/t)"))
        if tanya == "y" : 
            cursor.execute(f"select * from data where no_rekening = '{no_rek}'")
            data = cursor.fetchall()
            for akun in data : 
                struk = open(f"struk setoran {akun[1]}","x")
                teks = f'''===struk setoran===
atas nama : {akun[1]}
no rekening : {akun[0]}
jumlah setoran : {uang}
saldo saat ini : {akun[3]}'''
                struk.write(teks)
                struk.close()
                print("struk berhasil dicetak")
                menu()
        else : 
            menu()

def penarikan():
    uang = int(input("silahkan masukkan uang yang ingin ditarik : "))
    #mengupdate saldo dalam database
    cursor.execute(f"select saldo from data where no_rekening = '{no_rek}'")
    saldo = cursor.fetchall()
    for i in saldo : 
        for j in i : 
            saldo = j

    if uang > saldo : 
        print("saldo anda tidak mencukupi")
        menu()
    else : 
        uang_sekarang = saldo - uang
        cursor.execute(f"update data set saldo = {uang_sekarang} where no_rekening = '{no_rek}'")
        db.commit()
    while True : 
        tanya = str(input("apakah anda ingin mencetak struk? (y/t)"))
        if tanya == "y" : 
            cursor.execute(f"select * from data where no_rekening = '{no_rek}'")
            data = cursor.fetchall()
            for akun in data : 
                struk = open(f"struk penarikan {akun[1]}","x")
                teks = f'''===struk penarikan===
atas nama : {akun[1]}
no rekening : {akun[0]}
jumlah penarikan : {uang}
saldo saat ini : {akun[3]}'''
                struk.write(teks)
                struk.close()
                print("struk berhasil dicetak")
                menu()
        else : 
            menu()

def transfer():
    no_rek_tujuan = str(input("masukkan nomor rekening tujuan : "))
    cursor.execute("select * from data")
    data = cursor.fetchall()
    ketemu = False
    for akun in data :
        panjang = len(data)
        index = 0
        while index < panjang : 
            if akun[0] == no_rek_tujuan : 
                ketemu = True
                saldo_penerima = akun[3]
                break
            else : 
                ketemu == False
                index += 1
    if ketemu == True : 
        uang = int(input("masukkan jumlah transfer : "))
        cursor.execute(f"select saldo from data where no_rekening = '{no_rek}'")
        saldo = cursor.fetchall()
        for i in saldo : 
            for j in i : 
                saldo_pengirim = j
        if uang > saldo_pengirim : 
            print("saldo anda tidak mencukupi")
            menu()
        else : 
            saldo_pengirim -= uang
            saldo_penerima += uang
            cursor.execute(f"update data set saldo = {saldo_penerima} where no_rekening = '{no_rek}'")
            cursor.execute(f"update data set saldo = {saldo_pengirim} where no_rekening = '{no_rek_tujuan}'")
            db.commit()
            while True : 
                tanya = str(input("apakah anda ingin mencetak struk? (y/t)"))
                if tanya == "y" : 
                    cursor.execute(f"select * from data where no_rekening = '{no_rek}'")
                    data = cursor.fetchall()
                    cursor.execute(f"select nama from data where no_rekening = '{no_rek_tujuan}'")
                    data_penerima = cursor.fetchall()
                    for i in data_penerima : 
                        for j in i : 
                            nama_penerima = j
                    for akun in data : 
                        struk = open(f"struk transfer {akun[1]}","x")
                        teks = f'''===struk transfer===
atas nama pengirim : {akun[1]}
no rekening : {akun[0]}
jumlah transfer : {uang}
nama penerima : {nama_penerima}
no rekening : {no_rek_tujuan}'''
                        struk.write(teks)
                        struk.close()
                        print("struk berhasil dicetak")
                        menu()
                else : 
                    menu()
        menu()
    else :
        print("no_rek/password salah")
        login()

def ganti_pin():
    masukkan_pin()
    while True :
        pin_baru = str(input("masukkan pin baru : "))
        if len(pin_baru) != 6 :
                print("masukkan pin sebanyak 6 digit!")
        else : 
            cursor.execute(f"update data set pin = '{pin_baru}' where no_rekening = '{no_rek}'")
            print("pin berhasil diganti!")
            menu()

login()


        