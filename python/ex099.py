from time import sleep


def maiorf(*num):
    maior = 0
    qnt = len(num)

    print('-='*30)
    print('Analisando os Valores passados ...')
    sleep(0.5)

    for c in num:
        print(c, end=' ')
        if c > maior:
            maior = c

    print(f'''Foram Informados {qnt} valores ao todo.
O maior valor foi {maior}.''')


maiorf(2, 9, 4, 5, 7, 1)
maiorf(10, 9, 45, 100)
maiorf()