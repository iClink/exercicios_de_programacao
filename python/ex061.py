x = float(input('Digite o primeiro termo: '))
y = float(input('Digite a razão: '))
z = 0
while z != 10:
    print('{:.0f}'.format(x))
    x = x * y
    z += 1