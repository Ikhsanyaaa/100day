vektor_u = [0,0,-1]
vektor_v = [1,1,1]
vektor_hasil = []
for i in range(3) :
    hasil = vektor_u[i] * vektor_v[i]
    vektor_hasil.append(hasil)
print("vektor u * vektor v = ",hasil)
skalar = sum(vektor_hasil)
print("hasil = ",skalar)
if skalar < 0 : 
    print("vektor membentuk sudut tumpul")
elif skalar > 0 : 
    print("vektor membentuk sudut lancip")
else : 
    print("vektor membentuk sudut ortogonal")