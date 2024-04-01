lista, p, i = [], [], []

while True:
    x = int(input('Digite um valor: '))
    lista.append(x)

    if x % 2 == 0:
        p.append(x)
    else:
        i.append(x)
    y = input('Quer continuar? [N/S] ').strip().lower()
    print(f'''{'-='*20}\n''')
    if y == 'n':
        break

print(f'''Os valores digitados foram: {lista}
Os valores pares foram: {p}
Os valores impares digitados foram: {i}''')