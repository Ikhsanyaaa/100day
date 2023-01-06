class BangunDatar :
    def luas(self):
        pass

class BangunRuang :
    def volume(self):
        pass

class persegi(BangunDatar) : 
    def __init__(self, sisi) :
        self.sisi = sisi

    def luas(self) : 
        return self.sisi*self.sisi
class segitiga(BangunDatar) : 
    def __init__(self,alas,tinggi) : 
        self.alas = alas
        self.tinggi = tinggi

    def luas(self) : 
        return self.alas * self.tinggi / 2

# sisi = int(input("masukkan panjang sisi : "))
persegi_baru = persegi(10)
print(persegi.luas(10))