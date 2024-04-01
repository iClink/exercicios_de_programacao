print('\nDigite o comprimento de 3 retas para saber se elas formam um triandgulo\n')
a = float(input('O comprimento da reta A é: '))
b = float(input('O comprimento da reta B é: '))
c = float(input('O comprimento da reta C é: '))
if a + b > c and b + c > a and a + c > b:
    print('Estas retas formam um triangulo')

    if a == b == c:
        print('Este triangulo é equilátero')
    elif a == b or a == c or b == c:
        print('Este triangulo é Isóceles')
    elif a != b and b != c and c != a:
        print('Este triangulo é escaleno')
else:
    print('Essas retas não formam um triangulo')
