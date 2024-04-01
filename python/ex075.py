q = int(input('digite um valor: '))
w = int(input('digite um valor: '))
e = int(input('digite um valor: '))
r = int(input('digite um valor: '))
t = (q, w, e, r)
print(f'Voce digitou os valores: {t}')

print(f'O numero 9 apareceu {t.count(9)} vezes')

if 3 in t:
    print(f'O primeiro numero 3 foi o {t.index(3)+1}ª a ser inserido')
else:
    print('Não há nenhum número 3')

if t[0] % 2 != 0 and t[1] % 2 != 0 and t[2] % 2 != 0 and t[3] % 2 != 0:
    print("não há numeros pares")
else:
    print('Os valores pares digitados foram: ', end=' ')
    n = 0
    while n != 4:
        if t[n] % 2 == 0:
            print(t[n], end=' ')
        n += 1
