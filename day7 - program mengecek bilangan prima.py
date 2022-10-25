#input bilangan yang ingin dicek apakah bilangan prima atau bukan
x = int(input("masukkan bilangan prima : "))
#mengatur pembagi = 2
pembagi = 2

#dikarenakan bilangan prima hanya bisa dibagi dengan 1 dan dirinya sendiri
#maka dilakukan perulangan dimana pembagi akan terus bertambah
#apabila sisa bagi dari x % pembagi nilainya bukan nol
while x % pembagi != 0 :
    pembagi = pembagi + 1
    #pembagi bertambah satu hingga bernilai bilangan yang diinputkan sebelumnya

if pembagi == x :
    print(x, "adalah bilangan prima")
    #jika pembagi bernilai dengan bilangan x maka bilangan x adalah bilangan prima
else : 
    print(x, "bukan bilangan prima")
    #namun jika x % pembagi = 0 namun pembaginya bukan dari bilangan x
    #maka bilangan x bukanlah bilangan prima
