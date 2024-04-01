lista = []
maior = 0
for c in range(0, 5):
    x = int(input('Digite um valor: '))
    n = 0

    if x > maior:
        maior = x
        lista.append(x)
        print(f'O número {x} foi adicionado ao final da lista... \n', '-='*20, '\n')
    else:
        while True:
            if x < lista[n]:
                lista.insert(n, x)
                print(f'O número {x} foi adicionado a posição {n}\n', '-='*20, '\n')
                break
            else:
                n += 1

print(f'{lista}')

