x = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético Goianiense', 'Santos', 'Ceará', 'Internacional', 'Sao Paulo', 'Athletico-PR', 	'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'em ordem: {x[0:5]}')
print('=-'*50)
print(f'Os 4 ultimos: {x[:15:-1]}')
print('=-'*50)
print(f'Em ordem alfabética: {sorted(x)}')
print('=-'*50)
print('A chapecoense ficou em {}ª lugar'.format(x.index('Chapecoense')+1))