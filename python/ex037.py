x = int(input('Digite um número: '))
y = int(input('Escolha para qual base quer converte-lo:\nBinário, digite 1\nOctal, digite 2\nHexadecimal, digite 3 '))
if y == 1:
    print('Em binário é: {}'.format(bin(x)[2:]))
elif y == 2:
    print('Em octal é: {}'.format(oct(x)[2:]))

elif y == 3:
    print('Em hexadecimal é: {}'.format(hex(x)[2:]))

else:
    print('Formato não encontrado')
