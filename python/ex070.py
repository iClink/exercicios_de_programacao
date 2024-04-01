s = pb = pc = pbb = n = 0

while True:
    nome = input('Qual o nome do produto: ')
    preco = float(input('Qual o preço do produto: '))

    while preco < 0:
        preco = float(input('Qual o preço do produto: '))

    if pb == 0 or preco < pbb:
        pb = nome
        pbb = preco

    if preco > 1000:
        pc += 1

    s = s + preco

    n = input('Deseja continuar? [S/N] ').upper()

    while n != 'S' and n != 'N':
        n = input('Deseja continuar? [S/N] ').upper()

    if n == 'N':
        break

print(f'''\nO total gasto na compra foi: R${s:.2f}
{pc} Custam mais de R$1000,00
O produto mais barato foi: {pb}''')
