import random
y = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10]
x = 11
z = 12
tentativas = 0
while z != x:
    x = random.choice(y)
    tentativas += 1
    z = int(input('Tente adivinhar o meu número, entre 0 e 10: '))
    print('O numero que pensei foi: {}'.format(x))
    if z == x:
        print('Você ganhou, com {} tentativas, parabéns!'.format(tentativas))
    else:
        print('Você perdeu, tente novamente')
