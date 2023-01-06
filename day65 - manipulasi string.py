#manipulasi string

#memanggil indeks dalam string
nama = "ikhsan"
inisial = nama[0]
panggilan = nama[3:6]
print("hai nama saya adalah",nama,"inisial saya adalah",inisial)
print("kamu bisa panggil saya",panggilan)

#mengecek awalan & akhiran dalam string
nama = "ikhsan"
print("apakah nama berawalan dari i? :",nama.startswith("i"))
print("apakah nama berawalan dari a? :",nama.startswith("a"))
print("apakah nama berawalan dari m? :",nama.endswith("m"))
print("apakah nama berawalan dari n? :",nama.endswith("n"))

#menggabungkan string dengan integer
tanggal = 27
bulan = "november"
kelahiran = str(tanggal) + bulan
print("saya lahir pada tanggal :",kelahiran)

