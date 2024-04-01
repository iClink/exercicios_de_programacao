x = int(input('Qual a velocidade, em km, do carro? '))
if x > 80:
    y = (x-80)*7
    print('Você foi multado, e deverá pagar uma multa de: {:.2f}R$ reais'.format(y))
else:
    print('Tudo certo, está liberado.')