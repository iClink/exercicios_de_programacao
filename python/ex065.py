n, count, nc, s, maior, menor = 0, 0, 0, 0, 0, 0

while nc != -1:
    n = int(input('Digite um valor,[-1] para parar: '))
    if n == -1:
        nc = -1
        n = 0
        print('A média dos numeros é: {:.2f}, o maior foi: {}, o menor foi: {}'.format(s/count, maior, menor))
        x = int(input('Quer continuar? [1]sim [-1]não: '))
        if x == -1:
            nc = -1
        else:
            nc = 0
    s = n + s
    count += 1
    if n > maior:
        maior = n
    if n < menor or menor == 0:
        menor = n
