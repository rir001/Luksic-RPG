import pygame
# import images
import tablero
from pygame.locals import *

class mapa():
    def __init__(self, pos, name):
        self.x_c = pos[0]
        self.y_c = pos[1]
        self.update(0, 0)
        self.surf = pygame.image.load(f'{name}.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (len(tablero.tabla[1]) * step, len(tablero.tabla) * step)).convert_alpha()

    def update(self, x, y):
        self.pos_x = self.x_c * step + x - step/2
        self.pos_y = self.y_c * step + y - step/2
    
    def prints(self):
        screen.blit(self.surf, (self.pos_x , self.pos_y))

class people():
    def __init__(self, pos, name):
        self.x_c = pos[0]
        self.y_c = pos[1]
        self.update(0, 0)
        self.name = name
        self.see = 0
    
    def update(self, x, y):
        self.pos_x = self.x_c * step + x - step/2
        self.pos_y = self.y_c * step + y - step/2
    
    def prints(self):
        direct = ('front', 'back', 'left', 'right')
        self.surf = pygame.image.load(f'sprites/{self.name}/{direct[self.see]}.png')
        self.surf = pygame.transform.scale(self.surf, (96, 96)).convert_alpha()
        screen.blit(self.surf, (self.pos_x , self.pos_y))

class player():
    def __init__(self, name):
        self.name = name
        self.surf = pygame.image.load('sprites/player/back.png')
        self.surf = pygame.transform.scale(self.surf, (96, 96)).convert_alpha()

    def update(self, see):
        direct = ('front', 'back', 'left', 'right')
        self.surf = pygame.image.load(f'sprites/player/{direct[see]}.png')
        self.surf = pygame.transform.scale(self.surf, (96, 96)).convert_alpha()
    
    def prints(self):
        screen.blit(self.surf, (SCREEN_WIDTH/2-step/2,SCREEN_HEIGHT/2-step/2))

        
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

flags = FULLSCREEN | DOUBLEBUF
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, 16)
#screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
xx, yy = 0, 0

step = 64 * 1.5 # images.step

player = player('player')

murallas = []
sillas = []
personas = [[], []]

mapa = mapa([-(len(tablero.tabla[0])-1)/2, -(len(tablero.tabla)-1)/2+3], 'map')

for n in range(len(tablero.tabla)):
    for m in range(len(tablero.tabla[0])):
        coordenadas = (m-((len(tablero.tabla[0])-1)/2),n-((len(tablero.tabla)-1)/2)+3)
        if tablero.tabla[n][m][0] == 1:
            murallas.append(coordenadas)
        elif tablero.tabla[n][m][0] == 2:
            sillas.append(coordenadas)
        elif tablero.tabla[n][m][0] == 3:
            personas[0].append(coordenadas)
            personas[1].append(people(coordenadas, tablero.tabla[n][m][2]))


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
        
    
    frames = 24
    for _ in range(1, frames + 1):
        player.update(view)
        screen.fill((0, 0, 0))
        x += (step/frames) * go[0]
        y += (step/frames) * go[1]
        mapa.update(x, y)
        mapa.prints()
        player.prints()
        for n in personas[1]:
            n.update(x,y)
            n.prints()
        pygame.display.flip()


    xx -= go[0]
    yy -= go[1]
    go = (0,0)
    