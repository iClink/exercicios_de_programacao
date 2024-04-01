print('Programa iniciado')
m = 'x'
while m != 5:
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    m = int(input('O que deseja fazer?\n[1] Somar;\n[2] Multiplicar;\n[3] Maior;\n[4] Digitar novos valores;\n[5] Finalizar o programa.\n'))
    if m == 1:
        print('A soma dos valores é: {:.2f}'.format(n1+n2))

    if m == 2:
        print('A multiplicação dos valores é: {:.2f}'.format(n1*n2))

    if m == 3:
        if n1 > n2:
            print('O valor {} é maior que {}'.format(n1,n2))
        elif n1 < n2:
            print('O valor {} é maior que {}'.format(n2, n1))
        else:
            print('Os valores são iguais')

    m = int(input('Deseja continuar? \n[4] sim, [5] não\n'))

print('Programa finalizado')