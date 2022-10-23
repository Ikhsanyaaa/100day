#membuat kalkulator sederhana menggunakan fungsi input, aritmatika dan percabangan

angka1 = int(input("masukkan angka : "))
operator = int(input('''1. penjumlahan
2. pengurangan
3. perkalian
4. pembagian
pilih operator : '''))
angka2 = int(input("masukkan angka : "))
if operator == 1 :
    print(angka1, "+", angka2, "=", angka1 + angka2)
elif operator == 2 :
    print(angka1, "-", angka2, "=", angka1 - angka2)
elif operator == 3 :
    print(angka1, "*", angka2, "=", angka1 * angka2)
elif operator == 4 :
    print(angka1, "/", angka2, "=", angka1 / angka2)
