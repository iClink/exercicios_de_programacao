lista = []
c = 0
while True:
    x = int(input('Digite um valor: ').strip())
    print('Valor adicionado a lista!\n', '=-'*20)
    lista.append(x)
    c += 1
    y = input('Deseja continuar? [N/S]').lower().strip()
    if y == 'n':
        print('=-'*20)
        break
print(f'\nForam digitados {c} valores\n')
lista.sort(reverse=True)
print(f'A ordem decrescente da lista é: {lista}\n')
if '5' in lista:
    print('Há o valor 5 na lista')
else:
    print('Não há o valor 5 na lista')