x = int(input('Digite um número: '))
flag = 0
for c in range(2, x):
    if x % c == 0:
        flag = 1

if flag == 1:
    print('Ele não é primo')
else:
    print('Ele é primo')