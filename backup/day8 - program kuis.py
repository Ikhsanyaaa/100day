#membuat program quiz

nilai = 0

print("jawablah pertanyaan dibawah ini!")

print("1. tentukan nilai x dari persamaan 3x = 2x + 4")
jawaban1 = str(input('''a. 1
b. 2
c. 3
d. 4
masukkan pilihan (a/b/c/d) : '''))
if jawaban1 == "d" :
    nilai = nilai + 25
elif jawaban1 != "a" or jawaban1 != "b" or jawaban1 != "c" or jawaban1 != "d" :
    print("masukkan pilihan dengan benar!")

print("2. jika x = 2 dan y adalah 2x-1. maka tentukan nilai dari 9x - 5y")
jawaban2 = str(input('''a. 1
b. 2
c. 3
d. 4
masukkan pilihan (a/b/c/d) : '''))
if jawaban2 == "c" :
    nilai = nilai + 25
elif jawaban2 != "a" or jawaban2 != "b" or jawaban2 != "c" or jawaban2 != "d" :
    print("masukkan pilihan dengan benar!")

print('''3. jika nilai x adalah dua kalinya nilai y dan y adalah nilai x - 2
maka tentukan nilai dari y''')
jawaban3 = str(input('''a. 1
b. 2
c. 3
d. 4
masukkan pilihan (a/b/c/d) : '''))
if jawaban3 == "b" :
    nilai = nilai + 25
elif jawaban3 != "a" or jawaban3 != "b" or jawaban3 != "c" or jawaban3 != "d" :
    print("masukkan pilihan dengan benar!")
print('''4. jika x - 3 = 1 dan 3y + 2 = 11
maka tentukan hasil dari x - y ''')
jawaban4 = str(input('''a. 1
b. 2
c. 3
d. 4
masukkan pilihan (a/b/c/d) : '''))
if jawaban4 == "a" :
    nilai = nilai + 25
elif jawaban4 != "a" or jawaban4 != "b" or jawaban4 != "c" or jawaban4 != "d" :
    print("masukkan pilihan dengan benar!")
print("kuis berakhir, nilai anda adalah : ",nilai, "/100")