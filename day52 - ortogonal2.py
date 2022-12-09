u = [1,2,-2]
v = [3,0,1]
uv = [] #hasil kali u dengan v
#mengalikan u dengan v
for i in range(3) : 
    nilai = u[i] * v[i]
    uv.append(nilai)
hasil = sum(uv)
print("u . v = ",uv)
print("u . v = ",uv[0], "+", uv[1], "+", uv[2], "=", hasil)