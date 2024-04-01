print('{:=^30}\n'.format(str(' Exercício 011 ')))
#------------------------------------------------
print('Vamos determinar a área da parede e sua quantidade de tinta necessaria para ser pintada.')
#------------------------------------------------
la = float(input('Qual a largura, em metros, da parede?\n'))
al = float(input('Qual a altura, em metros, da parade?\n'))
#------------------------------------------------
print('A área da sua parede é igual a: {:.2f}m²;\nA quantidade de tinta necesária para pintar toda essa parede é de: {:.2f} litros.'.format((al*la), (al*la/2)))
