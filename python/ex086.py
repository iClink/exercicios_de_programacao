x, y = [], []
for c in range(0, 3):
    for n in range(0, 3):
        y.append(int(input(f'Digite o valor da posição [{c},{n}]: ')))
        x.append(y[:])
        y.clear()

print(f'''{'-=' * 30}''')
n = 0
for c in x:
    n += 1
    print(f'{c}', end='')
    if n %3 == 0:
        print('')
