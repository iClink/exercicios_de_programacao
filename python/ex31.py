x = int(input('Qual a distancia, em km, que irá viajar? '))
if x>200:
    print('Sua viagem custará: {:.2f}R$ reais'.format(x*0.45))
else:
    print('Sua viagem custará: {:.2f}R$ reais'.format(x*0.50))