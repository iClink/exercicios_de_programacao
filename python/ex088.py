from random import randint
x, y = [], []
z = int(input('Quantos jogos deseja fazer? '))
for c in range(0, z):
    for n in range(0, 6):
        v = randint(1, 60)
        while v in y:
            v = randint(1, 60)
        y.append(v)
    y.sort()
    x.append(y[:])
    y.clear()


print(f'''{'-='*30}''')

for c in x:
    print(f'{c}\n')