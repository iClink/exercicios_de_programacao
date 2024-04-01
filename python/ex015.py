print('{:=^30}\n'.format(str(' Exercício 015 ')))
#------------------------------------------------
print('Vamos calcular o preço do aluguel do carro;')
d = int(input('Insira por quantos dias ele foi alugado: '))
k = float(input('Insira quantos Km foram percorridos: '))
print('O Preço total do aluguel é de: {:.2f}R$'.format((d*60)+(k*0.15)))