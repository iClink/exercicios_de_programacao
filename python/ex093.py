x = dict()
x['Nome'] = str(input('Nome do jogador: '))
y = int(input(f'Quantas partidas {x["Nome"]} Jogou? '))
partidas = []
total = 0
for c in range(0, y):
    qg = int(input(f'Quantos gols na partida {c+1}? '))
    total = total + qg
    partidas.append(qg)
x['Gols'] = partidas
x['Total'] = total
print('-='*30)
print(x)
print('-='*30)
for k, v in x.items():
    print(f'O campo {k} tem valor {v}.')
print('-='*30)
print(f'O jogador {x["Nome"]} Jogou {y} partidas.')
for c, v in enumerate(partidas):
    print(f'=> Na partida {c+1}, fez {v} gols')
print(f'Foi um total de {total} gols.')
