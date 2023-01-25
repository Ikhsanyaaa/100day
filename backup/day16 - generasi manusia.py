#program mengecek generasi berdasarkan tahun lahir
nama = str(input("masukkan nama anda : "))
tahun_lahir = int(input("masukkan tahun lahir anda : "))
if tahun_lahir >= 1965 and tahun_lahir <= 1979 :
    print(nama,"berdasarkan tahun lahir, anda adalah generasi X")
elif tahun_lahir >= 1980 and tahun_lahir <= 1994 :
    print(nama,"berdasarkan tahun lahir, anda adalah generasi Y")
elif tahun_lahir >1995 : 
    print(nama,"berdasarkan tahun lahir, anda adalah generasi Z")
else :
    print(nama,"anda tidak termasuk generasi x, y, maupun z")