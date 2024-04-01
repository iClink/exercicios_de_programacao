x = dict()
y = []
while True:
    total = 0
    print('--'*30)
    x['nome'] = input('Nome do Jogador: ').title()
    x['partida'] = []
    p = int(input(f'Quantas partidas {x["nome"]} jogou? '))
    for c in range(0, p):
        g = int(input(f'Quantos gols na partida {c + 1}? '))
        x['partida'].append(g)
        total = total + g
    x['total'] = total
    y.append(x.copy())
    x.clear()
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar in 'Nn':
        break

print('-='*35)
print(f'''{"cod":<3} {"nome":<15} {"Gols":<10} {'Total':>5}
{"--"*35}''')
for c, n in enumerate(y):
    print(f'{c:<4}', end='')
    for d in n.values():
        print(f'{str(d):<15}', end='')
    print()

print('-='*35)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(y):
        print('Erro, favor selecionar um número de jogador válido.')
    else:
        print(f'--- Levantamento do jogador {y[busca]["nome"]}: ')
        for c, v in enumerate(y[busca]['partida']):
            print(f'No jogo {c+1}, foram feitos {v} gols.')
        print('--'*40)
print('<<<ENCERRADO>>>')
