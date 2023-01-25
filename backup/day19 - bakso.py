# #Ibu Ervin berbelanja di pasar, ia membeli 5 kg bakso sapi dan 4 kg bakso ikan dengan harga Rp. 550.000.
# Di pasar yang sama, Bu Feni membeli 4 kg bakso sapi dan 5 kg bakso ikan dengan harga Rp. 530.000. 
# Sedangkan ibu ijah membeli 2 kg bakso spi dan 3 kg bakso ikan. Bu Ijah harus membayar sebesar...

#mencari harga bakso sapi dan bakso ikan
taksiran_harga_bakso_sapi = []
taksiran_harga_bakso_ikan = []
for i in range(0,100000,10000) :
    taksiran_harga_bakso_sapi.append(i)
for i in range(0,100000,10000) :
    taksiran_harga_bakso_ikan.append(i)

for bakso_sapi in taksiran_harga_bakso_sapi : 
    for bakso_ikan in taksiran_harga_bakso_ikan : 
        if (5*bakso_sapi) + (4*bakso_ikan) == 550000 : 
            print("harga bakso sapi adalah : ",bakso_sapi,"/kg")
            print("harga bakso ikan adalah : ",bakso_ikan,"/kg")

            print("maka bu ijah harus membayar sebanyak : Rp.", (2*bakso_sapi) + (3*bakso_ikan))