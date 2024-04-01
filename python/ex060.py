x = int(input('Digite um número: '))
y = x
f = 1
while x != 1:
    f = x*f
    x = x - 1
print('O fatorial de {} é: {}'.format(y, f))