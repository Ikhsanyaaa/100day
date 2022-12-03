#membuat quiz matematika random
import random

angka1 = random.randint(1,1000)
angka2 = random.randint(1,1000)

def penjumlahan(): 
    hasil = angka1 + angka2
    soal = print(angka1, "+", angka2)
    jawaban = int(input("jawab : "))
    if jawaban != hasil : 
        print("salah")
    else : 
        print("benar")
    menu()

def pengurangan(): 
    hasil = angka1 - angka2
    soal = print(angka1, "-", angka2)
    jawaban = int(input("jawab : "))
    if jawaban != hasil : 
        print("salah")
    else : 
        print("benar")
    menu()

def perkalian():
    hasil = angka1 * angka2
    soal = print(angka1, "*", angka2)
    jawaban = int(input("jawab : "))
    if jawaban != hasil : 
        print("salah")
    else : 
        print("benar")
    menu()

def pembagian(): 
    hasil = angka1 / angka2
    soal = print(angka1, "/", angka2)
    jawaban = int(input("jawab : "))
    if jawaban != hasil : 
        print("salah")
    else : 
        print("benar")
    menu()

def menu():
    soal = int(input('''1. penjumlahan
    2. pengurangan
    3. perkalian
    4. pembagian
    pilih soal dengan operator yang diinginkan : '''))
    if soal == 1 : 
        penjumlahan()
    elif soal == 2 : 
        pengurangan()
    elif soal == 3 :
        perkalian()
    elif soal == 4 : 
        pembagian()
    else : 
        print("pilihan yang anda masukkan salah!")
        menu()

menu()