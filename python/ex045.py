import random
x = str('pedra')
y = str('papel')
z = str('tesoura')
pl = str(input('Digite pedra, papel ou tesoura: '))
pc = [x, y, z]
random.shuffle(pc)
print('Eu escolhi {}, e você {}'.format((pc[0]), pl))
if pc[0] == pl:
    print('Empatamos, vamos denovo!')
elif pc[0] == x and pl == z or pc[0] == y and pl == x or pc[0] == z and pl == y:
    print('Ha, você perdeu, tente novamente')
else:
    print('Parabens, você ganhou')
