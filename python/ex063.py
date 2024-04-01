n = int(input('Digite o número de termos da Sequência de Fibonacci desejada : '))
cont = 2
fib = [0, 1]
if n > 2:
    print('1° termo : {}'.format(fib[0]))
    print('2° termo : {}'.format(fib[1]))

    while cont < n:
        fib.append(fib[cont-1] + fib[cont-2])
        print('{}° termo : {}'.format(cont+1, fib[cont]))
        cont += 1
elif n == 1:
    print('1° termo : {}'.format(fib[0]))
elif n == 2:
    print('1° termo : {}'.format(fib[0]))
    print('2° termo : {}'.format(fib[1]))

