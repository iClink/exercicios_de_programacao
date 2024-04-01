
valor = int(input('Qual será o valor sacado? '))

v50 = valor//50
v20 = (valor % 50)//20
v10 = ((valor % 50) % 20)//10
v1 = (((valor % 50) % 20) % 10)//1

print(f'''\nTotal de {v50} cédulas de R$50
Total de {v20} cédulas de R$20
Total de {v10} cédulas de R$10
Total de {v1} cédulas de R$1''')
