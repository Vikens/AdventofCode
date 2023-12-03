with open('entradas/day3.in') as f:
    esquemas=f.readlines()
    
esquemas=[esquema.strip() for esquema in esquemas]

simbolos=[]
gears=[]
ans=0
numero=''
espieza=False
esgear=False
resultado=0

for i,linea in enumerate(esquemas):
    for j,c in enumerate(linea):
        if c.isdigit():
            numero += c
            for k in range(-1,2):
                for l in range(-1,2):
                    if i+k>=0 and j+l>=0 and i+k<len(esquemas) and j+l<len(esquemas[0]):
                        if not(esquemas[i+k][j+l].isdigit()) and esquemas[i+k][j+l] !='.':
                            espieza=True
                        if esquemas[i+k][j+l] == '*':
                            esgear=True
                            posicion=[i+k,j+l]
        else:
            if espieza:
                ans += int(numero)
            if esgear:
                for pos,val in gears:
                    if pos==posicion:
                        resultado += int(numero)*int(val)
                else:
                    gears.append([posicion,numero])
            numero=''
            espieza=False
            esgear=False

print(ans)
print(resultado)
