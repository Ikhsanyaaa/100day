u = [6,1,4]
v = [2,0,-3]

uv = [] #hasil kali u dengan v
#mengalikan u dengan v
for i in range(3) : 
    nilai = u[i] * v[i]
    uv.append(nilai)
print("hasil dari u . v = ",uv)
#menentukan ortogonalitas
skalar = sum(uv)
print(f"{uv[0]} + {uv[1]} + {uv[2]} = {skalar}")
if skalar == 0 : 
    print("vektor adalah ortogonal")
else : 
    print("tidak ortogonal")