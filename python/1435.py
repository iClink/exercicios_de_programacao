def geraMatriz(M):
    n = len(M)

    half = (n + 1) // 2
    linhai = coli = 0  # linha inicial e coluna inicial onde o preenchimento da matriz será feito
    linhaf = colf = n - 1  # linha final e coluna final onde o preenchimento da matriz será feito

    # val são os valores a serem inseridos na matriz
    for val in range(1, half + 1):

        for j in range(coli, colf + 1):
            M[linhai][j] = val
            M[linhaf][j] = val

        for i in range(linhai, linhaf):
            M[i][coli] = val
            M[i][colf] = val

        linhai += 1
        linhaf -= 1
        coli += 1
        colf -= 1


# =====================================

def imprimeMatriz(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            fim = " " if j != n - 1 else ""
            print(f"{M[i][j]:>3}", end=fim)
        print("")  # pula uma linha após imprimir uma linha inteira da matriz



# =====================================

def main():
    n = int(input())

    while n != 0:
        M = [[-1] * n for i in range(n)]
        geraMatriz(M)
        imprimeMatriz(M)
        n = int(input())


main()
