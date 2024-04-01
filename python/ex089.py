x, y = [], []
while True:
    y.append(input('Nome: ').strip())
    y.append(float(input('Nota 1: ')))
    y.append(float(input('Nota 2: ')))
    x.append(y[:])
    y.clear()
    z = input('Deseja continuar? [S/N]: ').lower()
    if z == 'n':
        break

print('-=' * 30)
print(f'''{'No.':<8}{'Nome':<30}MÉDIA
{'-' * 60}''')

for c, v in enumerate(x):
    media = (v[1] + v[2]) / 2
    print(f'''{c:<8}{v[0]:<30}{media:.1f}''')

print('-'*60)

while True:
    z = int(input('Deseja mostrar notas de qual aluno? (Digite número do aluno, 999 interrompe): '))
    print(f'Notas de {x[z][0]}, são: {x[z][1:]}')
    print('--'*30)
    if z == 999:
        break
