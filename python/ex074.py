from random import randint
x = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print(x)
n = 0
maior = -1
menor = -1

while n != 5:
    if maior == -1 or maior < x[n]:
        maior = x[n]
        
    if menor == -1 or menor > x[n]:
        menor = x[n]
    n += 1
print(f'O maior é: {maior} e o menor é: {menor}')