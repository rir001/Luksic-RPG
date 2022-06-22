import pygame
import images
import tablero
from pygame.locals import *
from functions import *

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

flags = FULLSCREEN | DOUBLEBUF
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, 16)

but = [button(2, 1, 'Generar mapa'), button(2, 2, 'Continuar con mapa precargado')]

run = True
a = 1
while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_UP:
                a = 1
            if event.key == K_DOWN:
                a = 2
            if event.key == K_SPACE:
                generar_mapa = False
                if a == 1:
                    generar_mapa = True
                run = False

        elif event.type == QUIT:
            run = False
    
    screen.fill((50, 50, 50))

    for n in but:
        n.prints(screen, a)
    pygame.display.flip()

if generar_mapa:
    screen.fill((50, 50, 50))

    surf = pygame.image.load('sprites/wait.png')
    screen.blit(surf, (SCREEN_WIDTH - 350 , SCREEN_HEIGHT - 300))

    text = pygame.font.Font('freesansbold.ttf', 64).render('Esto podria tardar unos minutos', True, (255, 255, 255))
    textRect = text.get_rect().center = (100, 300)
    screen.blit(text, textRect)



    pygame.display.flip()
    images.init()
    
x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
xx, yy = 0, 0

player = player('player')

mapa1 = mapa([-(len(tablero.tabla[0])-1)/2, -(len(tablero.tabla)-1)/2+3], 'map1')
mapa2 = mapa([-(len(tablero.tabla[0])-1)/2, -(len(tablero.tabla)-1)/2+3], 'map2')

murallas = []
sillas = []
personas = [[], []]

for n in range(len(tablero.tabla)):
    for m in range(len(tablero.tabla[0])):
        coordenadas = (m-((len(tablero.tabla[0])-1)/2),n-((len(tablero.tabla)-1)/2)+3)
        if tablero.tabla[n][m][0] == 1:
            murallas.append(coordenadas)
        elif tablero.tabla[n][m][0] == 2:
            sillas.append(coordenadas)
        elif tablero.tabla[n][m][0] == 3:
            personas[0].append(coordenadas)
            personas[1].append(people(coordenadas, tablero.tabla[n][m][3]))


lista = [murallas, sillas, personas]
        
view = 1
go = (0,0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_UP:
                if ((xx,yy-1) not in murallas) and ((xx,yy-1) not in sillas) and ((xx,yy-1) not in personas[0]):
                    go = (0,1)
                view = 1
                    
            elif event.key == K_DOWN:
                if ((xx,yy+1) not in murallas) and ((xx,yy) not in sillas) and ((xx,yy+1) not in personas[0]):
                    go = (0,-1)
                view = 0
                    
            elif event.key == K_LEFT:
                if ((xx-1,yy) not in murallas) and ((xx-1,yy) not in personas[0]):
                    go = (1,0)
                view = 2

            elif event.key == K_RIGHT:
                if ((xx+1,yy) not in murallas) and ((xx+1,yy) not in personas[0]):
                    go = (-1,0)
                view = 3
            
            if event.key == K_SPACE:
                if view == 0 and ((xx,yy+1) in personas[0]):
                    personas[1][personas[0].index((xx,yy+1))].see = 1

                elif view == 1 and ((xx,yy-1) in personas[0]):
                    personas[1][personas[0].index((xx,yy-1))].see = 0

                elif view == 2 and ((xx-1,yy) in personas[0]):
                    personas[1][personas[0].index((xx-1,yy))].see = 3

                elif view == 3 and ((xx+1,yy) in personas[0]):
                    personas[1][personas[0].index((xx+1,yy))].see = 2
        
        elif event.type == QUIT:
            run = False
        
    
    frames = 12
    player.update(view)
    for _ in range(1, frames + 1):
        screen.fill((0, 0, 0))
        x += (step/frames) * go[0]
        y += (step/frames) * go[1]
        mapa1.update(x, y)
        mapa2.update(x, y)
        mapa1.prints(screen)
        player.prints(screen)
        for n in personas[1]:
            n.update(x,y)
            n.prints(screen)
        mapa2.prints(screen)
        pygame.display.flip()


    xx -= go[0]
    yy -= go[1]
    go = (0,0)
    
