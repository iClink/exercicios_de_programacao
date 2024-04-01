x = float(input('Digite o primeiro termo: '))
y = float(input('Digite a razão: '))
print(x)
for c in range(1, 10):
    x = x * y
    print('{:.0f}'.format(x))