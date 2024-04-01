geral = list()
dados = list()
ma = me = c = 0
while True:
    x = input('Digite o nome: ')
    y = int(input('Digite o peso: '))
    dados.append(y)
    dados.append(x)
    if me == 0 or y < me:
        me = y
    if y > ma:
        ma = y
    c += 1
    geral.append(dados[:])
    dados.clear()
    z = input('Deseja continuar ? [N/S] ').lower().strip()
    if z == 'n':
        break

print(f'''{'-='*30}
Foram cadastradas {c} pessoas
{'-=' * 30}''')
n = 0
print(f'As pessoas mais leves, pesando {me}, são: ', end=' ')

for c in geral:
    if c[n] == me:
        print(c[n + 1], end=' ')

print(f'''
{'-='*30}''')
print(f'As pessoas mais pesadas, pesando {ma}, são: ', end=' ')
for c in geral:
    if c[n] == ma:
        print(c[n + 1], end=' ')