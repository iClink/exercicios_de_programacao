from random import randint
from time import sleep
numeros = []


def sorteio():
    print('Sorteando 5 valores à lista: ', end=' ')
    for c in range(0, 5):
        x = randint(0, 10)
        print(x, end=' ')
        sleep(0.7)
        numeros.append(x)
    print('. Pronto!')


def somapar(a):
    soma = 0
    for c in a:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {a}, temos: {soma}')


sorteio()
somapar(numeros)
