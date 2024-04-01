import random
y = [1, 2, 3, 4, 5, 0]
x = random.choice(y)
z = int(input('Tente adivinhar o meu número, entre 0 e 5: '))
print('O numero que pensei foi: {}'.format(x))
if z == x :
    print('Você ganhou, parabéns!')
else:
    print('Você perdeu, tente novamente')
