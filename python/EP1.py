def binariador(x, binario):
    tarefas = 0

    for i in range(0, 8):
        binario[i] += x % 2
        tarefas += x % 2
        x = x // 2

    return binario, tarefas

def saida(binario, mais, mais_tarefas, menos, menos_tarefas):
    parafusar = ['capo', 'tampa do porta-malas', 'eixos', 'rodas', 'motor', 'portas', 'chassi', 'assoalho']
    maior = menor = binario[0]
    posicao_maior = posicao_menor = 0

    for i in range(8):
        if maior < binario[i]:
            maior = binario[i]
            posicao_maior = i

        if menor > binario[i]:
            menor = binario[i]
            posicao_menor = i

        print(f'{i + 1}. parafusar {parafusar[i]}: {binario[i]}.')

    print(f'''A tarefa mais realizada foi parafusar {parafusar[posicao_maior]}: {binario[posicao_maior]} vezes.
A tarefa menos realizada foi parafusar {parafusar[posicao_menor]}: {binario[posicao_menor]} vezes.
A instrucao que exigiu menos tarefas simultaneas do robo foi a {menos}: {menos_tarefas} tarefas.
A instrucao que exigiu mais tarefas simultaneas do robo foi a {mais}: {mais_tarefas} tarefas.
''')


def main():
    contador = 0
    lista = []
    for i in range(0, 8):
        lista.append(0)

    while True:
        decimal = int(input())

        if decimal == 0:
            break

        binario, tarefas = binariador(decimal, lista)

        if contador == 0:
            mais = menos = decimal
            mais_tarefas = menos_tarefas = tarefas

        else:
            if mais_tarefas <= tarefas:
                mais_tarefas = tarefas
                mais = decimal

            if menos_tarefas >= tarefas:
                menos_tarefas = tarefas
                menos = decimal
        contador +=1

    saida(binario, mais, mais_tarefas, menos, menos_tarefas)


main()
