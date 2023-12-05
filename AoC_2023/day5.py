with open('inputs/day5.in','r') as f:
    entradas = f.readlines()
entradas = [entrada.strip() for entrada in entradas]

a,b = entradas[0].split(':')
seeds=b.split()
valores={}
llave=0
for entrada in entradas[1:]:
    if entrada=='':
        llave +=1
        valores[llave]=[]
    elif entrada[0].isdigit():
        entrada = [int(l) for l in entrada.split()]
        valores[llave].append(entrada)

def resolver(intermedio):
    for key in valores.keys():
        for i in range(len(valores[key])):
            if intermedio >= valores[key][i][1] and intermedio < valores[key][i][1] + valores[key][i][2]:
                intermedio = valores[key][i][0]+intermedio-valores[key][i][1]     
                break
    return(intermedio)  

resultado=0   
for seed in seeds:
    intermedio = resolver(int(seed))
    if resultado == 0 or resultado > intermedio:
        resultado = intermedio

print('resultado parte 1',resultado)
seeds2=[]
for i in range(0,len(seeds),2):
    seeds2.append([int(seeds[i]),int(seeds[i+1])])
print(seeds2)
resultado2=0
lista = set()
for seed in seeds2:
    print(seed)
    for j in range(seed[0],seed[0]+seed[1],1):
        if j in lista:
            continue
        else:
            intermedio = resolver(j)
            lista.add(j)
            if resultado2 == 0 or resultado2 > intermedio:
                resultado2 = intermedio
print(resultado2)
