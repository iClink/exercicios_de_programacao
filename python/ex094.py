x = dict()
lista = []
soma = media = 0
while True:
    x['nome'] = str(input('Nome: '))

    while True:
        x['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if x['sexo'] in 'MF':
            break

    x['idade'] = int(input('Idade: '))
    soma = soma + x['idade']
    lista.append(x.copy())
    x.clear()
    y = input('Digite "N" para parar, ou qualquer tecla para continuar ').upper()
    if y == 'N':
        break
media = (soma/len(lista))
print(f'''a) Ao todo, foram cadastradas {len(lista)} pessoas
b) A média de idade é de {media:.2f}
c) As mulheres cadastradas foram: ''', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]};', end=' ')
print()
print('d) Lista das pessoas que estão acima da média: ')
for c in lista:
    if c['idade'] > media:
        for k, v in c.items():
            print(f'{k} = {v}')
