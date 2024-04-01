a = f = 0
y = input('Digite sua expressão matemática: ')
a = y.count('(')
f = y.count(')')
if a == f:
    print('A expressão é válida')
else:
    print('A expressão é inválida')