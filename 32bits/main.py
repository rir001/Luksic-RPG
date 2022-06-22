import pygame
# import images
import tablero
from functions import *
from pygame.locals import *


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

flags = FULLSCREEN | DOUBLEBUF
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, 16)


x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
xx, yy = 0, 0

player = player()

mapa1 = mapa([-(len(tablero.tabla[0])-1)/2, -(len(tablero.tabla)-1)/2+2], 'down')
mapa2 = mapa([-(len(tablero.tabla[0])-1)/2, -(len(tablero.tabla)-1)/2+2], 'up')

murallas = []
sillas = []
personas = [[], []]

for n in range(len(tablero.tabla)):
    for m in range(len(tablero.tabla[0])):
        coordenadas = (m-((len(tablero.tabla[0])-1)/2),n-((len(tablero.tabla)-1)/2)+2)
        if tablero.tabla[n][m][0] == 1:
            murallas.append(coordenadas)
        elif tablero.tabla[n][m][0] == 2:
            sillas.append(coordenadas)
        elif tablero.tabla[n][m][0] == 3:
            personas[0].append(coordenadas)
            personas[1].append(people(coordenadas, tablero.tabla[n][m][3]))


lista = [murallas, sillas, personas]

go = (0,0)
goo = False
xd = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_UP:
                if ((xx,yy-1) not in murallas) and ((xx,yy-1) not in sillas) and ((xx,yy-1) not in personas[0]):
                    go = (0,1)
                player.update('back')
                goo = True
                xd += 1
                    
            elif event.key == K_DOWN:
                if ((xx,yy+1) not in murallas) and ((xx,yy) not in sillas) and ((xx,yy+1) not in personas[0]):
                    go = (0,-1)
                player.update('front')
                goo = True
                xd += 1
                    
            elif event.key == K_LEFT:
                if ((xx-1,yy) not in murallas) and ((xx-1,yy) not in personas[0]):
                    go = (1,0)
                player.update('left')
                goo = True
                xd += 1

            elif event.key == K_RIGHT:
                if ((xx+1,yy) not in murallas) and ((xx+1,yy) not in personas[0]):
                    go = (-1,0)
                player.update('right')
                goo = True
                xd += 1
            
            if event.key == K_SPACE:
                if player.see == 'front' and ((xx,yy+1) in personas[0]):
                    personas[1][personas[0].index((xx,yy+1))].see = 'back'

                elif player.see == 'back' and ((xx,yy-1) in personas[0]):
                    personas[1][personas[0].index((xx,yy-1))].see = 'front'

                elif player.see == 'left' and ((xx-1,yy) in personas[0]):
                    personas[1][personas[0].index((xx-1,yy))].see = 'right'

                elif player.see == 'right' and ((xx+1,yy) in personas[0]):
                    personas[1][personas[0].index((xx+1,yy))].see = 'left'
        
        elif event.type == QUIT:
            run = False
        
    
    frames = 20
    for z in range(1, frames + 1):
        screen.fill((0, 0, 0))
        x += (step/frames) * go[0]
        y += (step/frames) * go[1]
        mapa1.update(x, y)
        mapa2.update(x, y)
        mapa1.prints(screen)

        player.prints(screen, frames, z, goo, xd)
        
        for n in personas[1]:
            n.update(x,y)
            n.prints(screen)
        
        mapa2.prints(screen)
        
        pygame.display.flip()
    goo = False


    xx -= go[0]
    yy -= go[1]
    go = (0,0)
    
