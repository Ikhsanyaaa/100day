#membuat program segitiga angka

string = ""

x = int(input("Masukkan angka 1- 9 : "))
baris = x
no = 0
# Looping Baris
while baris >= 0:
	# Looping Kolom Spasi Kosong
	kolom = baris
	while kolom > 0:
		string = string + "   "
		kolom = kolom - 1
	# Looping Kolom Angka Sisi Kiri
	kiri = 1
	while kiri < (x - (baris-1)):
		string = string + " " + str(no) + " "
		kiri = kiri + 1		
	# Looping Kolom Angka Sisi Kanan
	kanan = 1
	while kanan < kiri -1:
		string = string + " " + str(no) + " "
		kanan = kanan + 1	

	string = string + "\n\n"
	baris = baris - 1
	no = no + 1
print (string)