t = ('lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'compasso', 9.99, 'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)
print(f'''{'='*50}
{'LISTAGEM DE PREÇOS':^50}
{'='*50}''')
n = 0

while n != len(t):
    print('{:.<30} R$ {:>7}'.format(t[n], t[n+1]))
    n += 2
print('='*50)
