x = {'nome': str(input('Nome: '))}
x['media'] = int(input(f'Média de {x["nome"]}: '))
if x['media'] >= 7:
    x['situação'] = 'Aprovado'
else:
    x['situação'] = 'Reprovado'

print(f'''O nome é: {x["nome"]}
Média é {x["media"]:.2f}
Situação é {x["situação"]}''')
