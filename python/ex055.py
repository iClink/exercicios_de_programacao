maior = 0
menor = 0
for c in range(1,6):
    x = float(input('Digite o {}ª peso: '.format(c)))
    if x > maior:
        maior = x
    if x < menor or menor == 0:
        menor = x
print('O maior peso é: {:.2f} e o menor peso é: {:.2f}'.format(maior, menor))