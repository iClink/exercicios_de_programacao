from math import *
print('{:=^30}\n'.format(str(' Exercício 018 ')))
#------------------------------------------------
print('Insira um ângulo para estudo: ')
x = float(input(''))
x = radians(x)
print('Sobre o angulo dado, temos:\nSeno = {:.3f}\nCosseno = {:.3f}\nTangente = {:.3f}'.format((sin(x)), (cos(x)), (tan(x))))
