import pygame
print('{:=^30}\n'.format(str(' Exercício 021 ')))
#------------------------------------------------
x = input('Digite o nome da sua musica preferida: ')
print('\nSua musica {}, passará a tocar agora'.format(x))
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(x)
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
