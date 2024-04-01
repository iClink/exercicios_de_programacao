sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite seu sexo:\n[M] para masculino;\n[F] para feminino: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Dígito inválido, favor digitar novamente: ')
if sexo == 'F':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'

print('Confirmado, seu sexo é {}'.format(sexo))