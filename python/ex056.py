mi = 0
idade = 0
hidade = 0
count = 0
hnome = 0
c = 0
for c in range(1, 5):
    nome = input('Digite o nome da {}ª pessoa: '.format(c))
    idade = float(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = int(input('Digite o sexo da {}ª pessoa, \n[1] para masculino\n[2] para feminino:  '.format(c)))
    mi = mi + idade
    if sexo == 1 and idade > hidade:
        hnome = nome
        hidade = idade
    if sexo == 2 and idade < 20:
        count = count + 1

print('A média de idade é de: {:.2f}'.format(mi/c))

if hnome == 0:
    print('Não há homens.')
else:
    print('O nome do homem mais velho é: {}'.format(hnome))

if count == 0:
    print('Não há mulheres')
else:
    print('Há {} mulheres com menos de 20 anos'.format(count))
