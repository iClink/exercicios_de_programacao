x = float(input('Digite o preço do produto: '))
print( """Para pagamento a vista(dinheiro/cheque):(1)'
Para pagamento a vista(cartão):(2)
Para pagamento em até 2x no cartão (3)
Para pagamento em até 3x no cartão (4)""")

y = int(input('Digite a forma de pagamento: '))
if y == 1:
    print('O total a pagar será: R${:.2f}'.format((x*0.9)))
elif y == 2:
    print('O total a pagar será: R${:.2f}'.format((x*0.95)))
elif y == 3:
    print('O total a pagar será: R${:.2f} de 2 parcelas de: R${:.2f} '.format(x, (x/2) ))
elif y == 4:
    print('O total a pagar será: R${:.2f} de 3 parcelas de: R${:.2f}'.format((x*1.20), ((x*1.20)/3)))
else:
    print('Forma de pagamento não encontrada')