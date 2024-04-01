def escreva(msg):
    x = int(len(msg)+4)
    print('~'*x)
    print(f'{msg:^{x}}')
    print('~'*x)


y = input('Digite algo: ')
escreva(y)
