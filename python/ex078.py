maior = menor = 0
valores = []
for c in range(0,5):
    x = int(input(f'Digite um valor para a posição {c}: '))
    valores.append(x)

    if c == 0 and menor == 0 or x < menor:
        menor = x

    if maior == 0 or x > maior:
        maior = x

print(f'\nVoce digitou os valores: {valores}')

print(f'O maior valor digitado foi {maior} nas posições: ', end='')

for c, n in enumerate(valores):
    if n == maior:
        print(f'{c}...', end='')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')

for c, n in enumerate(valores):
    if  n == menor:
        print(f'{c}...', end='')


