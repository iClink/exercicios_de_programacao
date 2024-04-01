x, y = [], []
par = c3 = maior = 0
for c in range(0, 3):
    for n in range(0, 3):
        z = int(input(f'Digite o valor da posição [{c},{n}]: '))
        y.append(z)
        x.append(y[:])
        y.clear()
        if z % 2 == 0:
            par = par + z
        if n == 2:
            c3 = c3 + z
        if c == 1 and z > maior:
            maior = z

print(f'''{'-=' * 30}''')
n = 0
for c in x:
    n += 1
    print(f'{c}', end='')
    if n % 3 == 0:
        print('')
print(f'''{'-=' * 30}
A soma dos numeros pares é: {par}
A soma dos valores da terceira coluna é: {c3}
O maior valor da segunda linha é: {maior}''')
