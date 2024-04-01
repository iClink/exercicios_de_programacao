x = dict()
x['Nome '] = str(input('Nome: '))
y = int(input('Ano de nascimento: '))
x['idade'] = (2022-y)
x['CTPS'] = int(input('Número da carteira de trabalho (Digite 0 caso não tenha): '))
if x['CTPS'] == 0:
    print('-='*30)
    print(x)
else:
    z = int(input('Digite o ano de contratação: '))
    x['Ano de contratação'] = z
    x['Salário em R$'] = float(input('Digite seu salário em R$: '))
    x['Aposentadoria'] = (z - y) + 35

for k, v in x.items():
    print(f'{k} é {v}')
