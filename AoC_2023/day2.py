with open('entradas/day2.in','r') as f:
    entradas = f.readlines()

diccionario = {}

for i,entrada in enumerate(entradas):
    llave = i+1
    diccionario[llave]=[]
    entrada=entrada.strip().split(':')
    entrada=entrada[1].split(';')
    entrada=[ bolsa.split() for bolsa in entrada]
    for bolsa in entrada:
        b=[0,0,0]
        if bolsa[1][:3] == 'red':
            b[0] = int(bolsa[0])
        elif bolsa[1][:4] == 'blue':
            b[1] = int(bolsa[0])
        else:
            b[2] = int(bolsa[0])
        if len(bolsa) > 3:
            if bolsa[3][:3] == 'red':
                b[0] = int(bolsa[2])
            elif bolsa[3][:4] == 'blue':
                b[1] = int(bolsa[2])
            else:
                b[2] = int(bolsa[2])
        if len(bolsa) > 5:
            if bolsa[5][:3] == 'red':
                b[0] = int(bolsa[4])
            elif bolsa[5][:4] == 'blue':
                b[1] = int(bolsa[4])
            else:
                b[2] = int(bolsa[4])
        diccionario[llave].append(b)

juego=[12,14,13]
suma=0
for key in diccionario.keys():
    detector=True
    for mano in diccionario[key]:
        if mano[0] > juego[0] or mano[1] > juego[1] or mano[2] > juego[2]:
            detector=False
    if detector:
        suma+=key
print(suma)
suma2=0
for key in diccionario.keys():
    red=0
    blue=0
    green=0
    for mano in diccionario[key]:
        if mano[0] > red:
            red = mano[0]
        if mano[1] > blue:
                blue = mano[1]
        if mano[2] > green:
                green = mano[2]
    suma2+=red*blue*green
print(suma2)