x = float(input('Digite seu salário: '))

if x > 1250:
    print('Seu novo salário será de: {:.2f}R$ reais'.format(x*1.10))
else:
    print('Seu novo salário será de: {:.2f}R$ reais'.format(x*1.15))