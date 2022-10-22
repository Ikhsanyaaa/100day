#percabangan / kondisi

a = 2
b = 3
hasil = a + b
#if
#if adalah perintah dimana kita bisa memberikan perintah sesuai kondisi yang diberikan
if hasil == 5 : 
    print("hasilnya adalah 5")
    #perintah print diatas hanya akan dijalankan apabila kondisi yang diberikan bernilai True
    #karena hasil == 5 maka print akan dieksekusi

#elif
#elif disimi pilihan kedua setelah if, jadi apabila kondisi if tidak terpenuhi maka akan mengarah ke elif

if hasil == 4 : 
    print("hasilnya adalah 4")
    #karena kondisi if diatas bernilai False maka perintah print diatas tidak akan dieksekusi
elif hasil == 5 :
    print("ternyata hasil nya adalah 5")
    #karena kondisi pertama diatas tidak dieksekusi maka akan berlanjut ke kondisi kedua di elif
    #dan kondisi pada elif bernilai True maka akan dieksekusi


#else
#else disini sebagai pilihan terakhir, dimana apabila kondisi if dan elif keduanya tidak terpenuhi atau bernilai False
#else tidak membutuhkan syarat atau kondisi dikarenakan else sudah memiliki syarat yakni semua syarat selain if dan elif

if hasil == 3 : 
    print("apakah hasilnya adalah 3?")
    #kondisi if bernilai False
elif hasil == 4 :
    print("mungkinkan hasilnya adalah 4?")
    #kondisi elif juga bernilai False
else :
    print("kalian salah, hasilnya adalah 5")