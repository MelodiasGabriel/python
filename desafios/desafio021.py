''' # Código que vi no stackoverflow pra abrir um arquivo, só fiquei curioso :)
def function(file):
    lines = []
    for line in f:
        lines.append(line)
    return lines
with open('notas 3 ano.txt', 'r') as f:
    contents = function(f)
    print(contents)'''

import pygame
pygame.init()
pygame.mixer.music.load('fendesse1.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
