def imprimeMatriz(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            fim = " " if j != n - 1 else ""
            print(f"{M[i][j]:<9}", end=fim)
        print("")


def caso2(n, matriz):
    x = 1

    for linha in matriz:

        for coluna in range(n):
            linha[coluna] = x
            x += 1

    verificador = 0

    for linha in matriz:
        coluna = 0

        if verificador == 0 or verificador == 3:
            while (coluna + 3) <= n:
                linha[coluna] = (((n ** 2) + 1) - linha[coluna])
                linha[coluna + 3] = (((n ** 2) + 1) - linha[coluna + 3])
                coluna += 4

        else:
            coluna = 1
            while coluna < n:
                linha[coluna] = (((n ** 2) + 1) - linha[coluna])
                linha[coluna + 1] = (((n ** 2) + 1) - linha[coluna + 1])
                coluna += 4

        if verificador == 3:
            verificador = 0

        else:
            verificador += 1


    return matriz


def caso1(n, matriz):
    y = n * n
    x = 1
    linha = 0
    coluna = n % 2
    while x <= y:
        matriz[linha][coluna] = x
        x += 1
        linhaanterior = linha
        colunaanterior = coluna

        if linha == 0:
            linha = n - 1
        else:
            linha -= 1

        if coluna == n - 1:
            coluna = 0

        else:
            coluna += 1

        if matriz[linha][coluna] != 0:
            linha = linhaanterior + 1
            coluna = colunaanterior

    return matriz


def main():
    n = int(input())
    matriz = [[0] * n for c in range(n)]

    if n % 2 != 0:
        resposta = caso1(n, matriz)

    elif n % 4 == 0:
        resposta = caso2(n, matriz)

    imprimeMatriz(resposta)


main()
