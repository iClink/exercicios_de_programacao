la = []
while True:
    x = int(input('Digite um valor: '))

    if x in la is not False:
        print('Este numero ja esta na lista...')

    else:
        la.insert(0, x)

    y = input('Quer continuar? [n/s] ')
    if y == 'n':
        break
la.sort()
print('Os numeros não repetidos foram: {}'.format(la))
