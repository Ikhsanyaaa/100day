#membuat program batu gunting kertas
import random
pilihan = ["batu", "gunting", "kertas"]
bot = pilihan[random.randint(0,2)]
def batu():
    if bot == pilihan[0] :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("seri")
    elif bot == pilihan[1] :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda menang")
    elif bot == pilihan[2] :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda kalah")
def gunting():
    if bot == pilihan[0] :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda kalah")
    elif bot == pilihan[1] :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("seri")
    elif bot == pilihan[2] :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda menang")
def kertas():
    if bot == pilihan[0] :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda menang")
    elif bot == pilihan[1] :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda kalah")
    elif bot == pilihan[2] :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("seri")

while True :   
    player = str(input('''batu / gunting / kertas
    masukkan pilihan anda : '''))
    if player ==  "batu" : 
        batu()
    elif player == "gunting" : 
        gunting()
    elif player == "kertas" :
        kertas()
    else :
        print("masukkan pilihan dengan benar!")


