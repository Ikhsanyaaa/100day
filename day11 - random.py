#membuat program batu gunting kertas
import random
pilihan = ["batu", "gunting", "kertas"]
bot = pilihan[random.randint(0,2)]
def batu():
    if bot == "batu" :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("seri")
    elif bot == "gunting" :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda menang")
    else : 
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda kalah")
def gunting():
    if bot == "batu" :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda kalah")
    elif bot == "gunting" :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("seri")
    else : 
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda menang")
def kertas():
    if bot == "batu" :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda menang")
    elif bot == "gunting" :
        print("anda memilih :",player)
        print("lawan memilih : ",bot)
        print("anda kalah")
    else : 
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


