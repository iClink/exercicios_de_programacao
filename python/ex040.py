x = float(input('insira sua primeira nota: '))
y = float(input('insira sua segunda nota: '))
m = (x+y)/2
if m < 5:
    print('Reprovado')
elif m >= 5  and m < 6.9:
    print('Recuperação')
else:
    print('Aprovado')
