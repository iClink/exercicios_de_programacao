x = input('Insira uma frase: ')
z = x
x = x.strip()
x = x.upper()
x = x.split()
x = ''.join(x)
y = x[::-1]
if y == x:
    print('a frase {} é um palindromo '.format(z))
else:
    print('a frase não é um palindromo.')
