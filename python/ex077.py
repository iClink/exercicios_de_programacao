p = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
     'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
n = 0
while n != len(p):
    print(f'Na palavra {(p[n]).upper()} temos: ', end='')
    print('a '*p[n].count('a'), 'e '*p[n].count('e'), 'i '*p[n].count('i'),
          'o '*p[n].count('o'), 'u '*p[n].count('u'))
    print()
    n += 1
