n, s, c = 0, 0, 0
while True:
    s = s + n
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
print(f'Foram digitados {c} valores, que somam {s}')