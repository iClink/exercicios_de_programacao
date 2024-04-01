x = float(input('Qual o valor da casa? '))
y = float(input('Qual seu salário? '))
z = int(input('Em quantos anos vai pagar? '))
z = z*12
print('O valor da prestação será: R${:.2f} reais'.format(x/z))
if (x/z) > (y*0.3):
    print('Você não é elegível para este empréstimo.')
else:
    print('Você é elegível para este empréstimo')