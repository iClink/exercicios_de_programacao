from time import sleep
n = 10
print('Iniciando contagem de auto destruição')
for c in range(0, 10):
    print('{}'.format(n))
    n = n-1
    sleep(1)
print('Feliz ano novo')