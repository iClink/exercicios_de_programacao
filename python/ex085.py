lista = []
pares = []
impares = []

for c in range(0,7):
    x = int(input('Digite um valor: '))
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
pares.sort()
impares.sort()
lista.append(pares[:])
lista.append(impares[:])
print(f'Os numeros pares foram: {lista[0]}\nOs numeros impares foram: {lista[1]}')