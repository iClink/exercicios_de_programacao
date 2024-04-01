x = int(input('Digite um ano para saber se ele é bissexto: '))
if (x % 400 == 0):
    print('O ano é bissexto')
elif (x % 4 == 0) and (x % 100 != 0):
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
