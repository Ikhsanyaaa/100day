#membuat game ular tangga
import random
posisi1 = 0
posisi2 = 0
lempar = 0
menang = False
def dadu():
    global lempar
    lempar = random.randint(1,6)

def ular1():
    global lempar
    global posisi1
    if posisi1 == 99 : 
        posisi1 = 63
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 97 : 
        posisi1 = 87
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 92 : 
        posisi1 = 25
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 90 : 
        posisi1 = 48
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 85 : 
        posisi1 = 59
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 83 : 
        posisi1 = 45
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 75 : 
        posisi1 = 28
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 60 : 
        posisi1 = 23
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 56 : 
        posisi1 = 1
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 54 : 
        posisi1 = 36
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 51 : 
        posisi1 = 6
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 39 : 
        posisi1 = 5
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 26 : 
        posisi1 = 10
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 18 : 
        posisi1 = 1
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 8 : 
        posisi1 = 4
        print("anda dimakan ular dan turun ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    else : 
        menang1()

def ular2():
    global lempar
    global posisi2
    if posisi2 == 99 : 
        posisi2 = 63
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 97 : 
        posisi2 = 87
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 92 : 
        posisi2 = 25
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 90 : 
        posisi2 = 48
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 85 : 
        posisi2 = 59
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 83 : 
        posisi2 = 45
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 75 : 
        posisi2 = 28
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 60 : 
        posisi2 = 23
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 56 : 
        posisi2 = 1
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 54 : 
        posisi2 = 36
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 51 : 
        posisi2 = 6
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 39 : 
        posisi2 = 5
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 26 : 
        posisi2 = 10
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 18 : 
        posisi2 = 1
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 8 : 
        posisi2 = 4
        print("anda dimakan ular dan turun ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    else : 
        menang2()
    

def tangga1():
    global lempar
    global posisi1
    if posisi1 == 3 : 
        posisi1 =20
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 6 : 
        posisi1 = 14
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 11 : 
        posisi1 = 28
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 15 : 
        posisi1 = 34
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 17 : 
        posisi1 = 74
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 22 : 
        posisi1 = 37
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 38 : 
        posisi1 = 59
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 49 : 
        posisi1 = 67
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 57 : 
        posisi1 = 76
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 61 : 
        posisi1 = 78
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 73 : 
        posisi1 = 86
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 81 : 
        posisi1 = 98
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    elif posisi1 == 88 : 
        posisi1 = 91
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player1()
        else : 
            player2()
    else : 
        ular1()

def tangga2():
    global lempar
    global posisi2
    if posisi2 == 3 : 
        posisi2 =20
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 6 : 
        posisi2 = 14
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 11 : 
        posisi2 = 28
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 15 : 
        posisi2 = 34
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 17 : 
        posisi2 = 74
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 22 : 
        posisi2 = 37
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 38 : 
        posisi2 = 59
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 49 : 
        posisi2 = 67
        print("anda naik tangga ke : ",posisi1)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 57 : 
        posisi2 = 76
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 61 : 
        posisi2 = 78
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 73 : 
        posisi2 = 86
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 81 : 
        posisi2 = 98
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    elif posisi2 == 88 : 
        posisi2 = 91
        print("anda naik tangga ke : ",posisi2)
        if lempar == 6 : 
            player2()
        else : 
            player1()
    else : 
        ular2()


def menang1():
    global menang
    global posisi1
    global lempar
    if posisi1 >= 100 :
        menang = True
        awalplayer1()
    else : 
        if lempar == 6 : 
            player1()
        else : 
            player2()
def menang2():
    global menang
    global posisi2
    global lempar
    if posisi2 >= 100 :
        menang = True
        awalplayer2()
    else : 
        if lempar == 6 : 
            player2()
        else : 
            player1()
    
def player1():
    global posisi1
    global lempar
    print("===giliran player 1===")
    s = input("tekan apa saja untuk roll")
    dadu()
    print("dadu yang keluar adalah angka : ",lempar)
    posisi1 = posisi1 + lempar
    print("posisi anda sekarang : ",posisi1)
    tangga1()


def player2(): 
    global lempar
    global posisi2
    print("===giliran player 2===")
    s = input("tekan apa saja untuk roll")
    dadu()
    print("dadu yang keluar adalah angka : ",lempar)
    posisi2 = posisi2 + lempar
    print("posisi anda sekarang : ",posisi2)
    tangga2()

def awalplayer1():
    global menang
    global lempar
    global posisi1
    if menang == True :
        print("player 2 menang,permainan selesai")
    else : 
        if posisi1  > 0 : 
            player1()
        else :
            coba = 3
            while coba != 0 : 
                print("giliran player 1")
                s = input("roll sampai dapat 6 untuk start")
                print("sisa kesempatan : ",coba-1)
                dadu()
                print("dadu yang keluar adalah angka : ",lempar)
                coba -= 1
                if lempar == 6 :
                    print("anda bisa masuk start")
                    posisi1 = 1 
                    awalplayer2()
                if coba == 0 :
                    print("kesempatan anda berakhir")
                    coba == 3
                    awalplayer2()

def awalplayer2():
    global menang
    global lempar
    global posisi2
    if menang == True :
        print("player dua menang,permainan selesai")
    else : 
        if posisi2 > 0 : 
            player2()
        else : 
            coba = 3
            while coba != 0 : 
                print("giliran player2")
                s = input("roll sampai dapat 6 untuk start")
                print("sisa kesempatan : ",coba-1)
                dadu()
                print("dadu yang keluar adalah angka : ",lempar)
                coba -= 1
                if lempar == 6 : 
                    print("anda bisa masuk start")
                    posisi2 = 1
                    awalplayer1()
                if coba == 0 :
                    print("kesempatan anda berakhir")
                    coba == 3
                    awalplayer1() 

awalplayer1()


