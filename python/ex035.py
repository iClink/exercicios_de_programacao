print('\nDigite o comprimento de 3 retas para saber se elas formam um triandgulo\n')
a = float(input('O comprimento da reta A é: '))
b = float(input('O comprimento da reta B é: '))
c = float(input('O comprimento da reta C é: '))
if a+b > c and b+c > a and a+c > b:
    print('Estas retas formam um triangulo')

else:
    print('Essas retas não formam um triangulo')
