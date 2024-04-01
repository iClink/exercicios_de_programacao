cont = 0
x = 0
for c in range(1,8):
    x = int(input('Digite sua idade: '))
    if x >= 18:
        cont = cont + 1
print('{} já são de maior, e {} ainda são de menor'.format(cont, (7-cont)))
