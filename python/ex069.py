hc, p18, m20 = 0, 0, 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [F/M]: ').upper()
    if idade > 18:
        p18 += 1
    if sexo == 'M':
        hc += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    n = input('Deseja continuar? [S/N] ').upper()
    if n == 'N':
        break

print(f'''\n{p18} pessoas tem mais de 18 anos;
{hc} homens foram cadastrados
{m20} mulheres tem menos de 20 anos''')