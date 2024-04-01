n, count, nc, s = 0, -1, 0, 0

while nc != 999:
    s = n + s
    count += 1
    n = int(input('Digite um valor: '))
    if n == 999:
        nc = 999
print('A soma dos numeros é: {}, foram somados {} números'.format(s, count))
