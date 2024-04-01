def ex():
    print('''
    Controle de Terrenos
    ________________________________''')
    x = float(input('Largura (m): '))
    y = float(input('Comprimento (m): '))
    a = x * y
    print(f'A área do terreno de {x:.2f} x {y:.2f} é de {a:.2f}m²')


ex()
