from math import *
print('{:=^30}\n'.format(str(' Exercício 017 ')))
#------------------------------------------------
print('Vamos calcular a hipotenusa de um triangulo retângulo.')
x = float(input('Insira o cateto adjacente: '))
y = float(input('Insira o cateto oposto: '))
h = sqrt((pow(x,2)+pow(y,2)))
print('A hipotenusa deste triângulo é: {:.2f}'.format(h))
