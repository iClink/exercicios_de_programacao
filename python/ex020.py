from random import *
print('{:=^30}\n'.format(str(' Exercício 020 ')))
#------------------------------------------------
print('Vamos sortear um dos 4 alunos:')
x1 = input('Digite o nome do primeiro aluno: ')
x2 = input('Digite o nome do segundo aluno: ')
x3 = input('Digite o nome do terceiro aluno: ')
x4 = input('Digite o nome do quarto aluno: ')
pool = [x1, x2, x3, x4]
shuffle(pool)
print('\nA ordem de apresentação é: \n1ª{};\n2ª{};\n3ª{};\n4ª{};'.format(pool[0], pool[1], pool[2], pool[3]))