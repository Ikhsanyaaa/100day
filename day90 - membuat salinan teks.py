#mengcopy kodingan ke dalam txt

nama_catatan = str(input("buat nama file untuk text : "))
catatan = open(f"{nama_catatan}.txt","x")
nama_file = str(input("masukkan nama file yang ingin di copy : "))
catatan = open(f"{nama_file}.py","r")
isi = catatan.read()
catatan = open(f"{nama_catatan}.txt","w")
catatan.write(isi)
print("catatan berhasil dicopy")