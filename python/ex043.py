x = float(input('Digite seu peso (em  kg): '))
y = float(input('Digite sua altura (em metros): '))
i = x/(y**2)
if i < 18.5:
    print('Abaixo do peso')
elif i >= 18.5 and i < 25:
    print('Peso ideal')
elif i >= 25 and i < 30:
    print('Sobrepeso')
elif i >= 30 and i < 40:
    print('Obesidade')
elif i > 40:
    print('Obesidade mórbida')