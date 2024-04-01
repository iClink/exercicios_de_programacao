x = int(input('Digite sua data de nascimento: '))
y = (2022-x)
if y <= 9:
    print('Mirim')
elif y > 9 and y <= 14:
    print('Infantil')
elif y > 14 and y <= 19:
    print('Junior')
elif y > 19 and y <= 20:
    print('Senior')
elif y > 20:
    print('Master')