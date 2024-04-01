from random import randint
maior = 0
x = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
for k, v in x.items():
    print(f'{k} tirou {v}')
    if v > maior:
        maior = v
print('-='*30)

lugar = []
while True:
    for k, v in x.items():
        if v == maior:
            lugar.append(k)
            lugar.append(v)
    maior -= 1
    if maior == 0:
        break
n = 1
c = 0
while True:
    print(f'O {lugar[c]} ficou em {n}ª lugar')
    n += 1
    c += 2
    if n == 5:
        break
