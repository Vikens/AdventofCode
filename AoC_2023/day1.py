with open('entradas/day1.in','r') as f:
    entradas = f.readlines()
entradas = [entrada.strip() for entrada in entradas]

resultado=0
for entrada in entradas:
    numero=''
    for i,c in enumerate(entrada):
        if c.isdecimal():
            numero += c
        for j,val in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if entrada[i:].startswith(val):
                numero += str(j+1)
    resultado += int(numero[0]+numero[-1])

print(resultado)