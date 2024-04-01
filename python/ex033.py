x = int(input('Digite um numero: '))
y = int(input('Digite outro: '))
z = int(input('Digite outro: '))

if x > y and x > z:
    print('{} é o maior número'.format(x))

if y > x and y > z:
    print('{} é o maior número'.format(y))

if z > x and z > y:
    print('{} é o maior número'.format(z))

if x < y and x < z:
    print('{} é o menor numero'.format(x))

if y < x and y < z:
    print('{} é o menor numero'.format(y))

if z < x and z < y:
    print('{} é o menor número'.format(z))

    