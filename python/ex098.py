from time import sleep


def contador(a, b, c):
    if c == 0:
        c = 1

    print(f'Contagem de {a} até {b} de {c} em {c}: ')

    if a > b and c > 0 or a < b and c < 0:
        c = -c

    print(c)

    if b > a:
        for z in range(a, b+1, c):
            print(f'{z}', end=' ')
            sleep(0.5)
        print()
        print('Contagem concluída\n')

    if a == b:
        print('Contagem concluída\n')

    if a > b:
        for z in range(a, b-1, c):
            print(f'{z}', end=' ')
            sleep(0.5)
        print()
        print('Contagem concluída\n')


contador(1, 10, 1)
contador(10, 2, 2)
print('Agora é sua vez de personalizar a contagem!')
x = int(input('Início: '))
y = int(input('Fim: '))
p = int(input('Passo: '))
print()
contador(x, y, p)
