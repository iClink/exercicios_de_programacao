from random import choice
n, c = 0, 0
while True:
    while n != 1 and n != 2:
        n = int(input('''Selecione: 
[1]Par
[2]ímpar\n'''))
        if n != 1 and n != 2:
            print('Tente Novamente')
    if n == 1:

        n = int(input('Digite o valor: '))
        s = choice([0, 1])

        print(f'Eu escolhi {s}, você escolheu {n}')

        if ((n+s)%2) == 0:

            c += 1
            print("Você ganhou essa, vamos de novo!")
            n = 0
        else:
            break
    if n == 2:

        n = int(input('Digite o valor: '))
        s = choice([0, 1])

        print(f'Eu escolhi {s}, você escolheu {n}')

        if ((n + s) % 2) != 0:

            c += 1
            print("Você ganhou essa, vamos de novo!")
            n = 0
        else:
            break


print(f'Há, você perdeu, mas ganhou {c} vezes seguidas, parabéns')