import pygame
from images import *

step = step * 2

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h


class mapa():
    def __init__(self, pos, name):
        self.x = pos[0]
        self.y = pos[1]
        self.update(0, 0)
        self.surf = pygame.image.load(f'{name}.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (len(tablero.tabla[1]) * step, len(tablero.tabla) * step)).convert_alpha()

    def update(self, x, y):
        self.pos_x = self.x * step + x - step/2
        self.pos_y = self.y * step + y - step/2
    
    def prints(self, screen):
        return screen.blit(self.surf, (self.pos_x , self.pos_y))

class people():
    def __init__(self, pos, name):
        self.x = pos[0]
        self.y = pos[1]
        self.update(0, 0)
        self.name = name
        self.see = 0
    
    def update(self, x, y):
        self.pos_x = self.x * step + x - step/2
        self.pos_y = self.y * step + y - step/2
    
    def prints(self, screen):
        direct = ('front', 'back', 'left', 'right')
        self.surf = pygame.image.load(f'sprites/{self.name}/{direct[self.see]}.png')
        self.surf = pygame.transform.scale(self.surf, (step, step)).convert_alpha()
        return screen.blit(self.surf, (self.pos_x , self.pos_y))

class player():
    def __init__(self, name):
        self.name = name
        self.surf = pygame.image.load('sprites/player/back.png')
        self.surf = pygame.transform.scale(self.surf, (step, step)).convert_alpha()

    def update(self, see):
        direct = ('front', 'back', 'left', 'right')
        self.surf = pygame.image.load(f'sprites/player/{direct[see]}.png')
        self.surf = pygame.transform.scale(self.surf, (step, step)).convert_alpha()
    
    def prints(self, screen):
        return screen.blit(self.surf, (SCREEN_WIDTH/2-step/2, SCREEN_HEIGHT/2-step/2))

class button():
    def __init__(self, num, id, string):
        self.margen = 150
        self.alto = 150
        self.ancho = SCREEN_WIDTH*2/3

        self.x = (SCREEN_WIDTH/2) - self.ancho/2
        self.y = (SCREEN_HEIGHT/num)*id - (SCREEN_HEIGHT/num)/2 - self.alto/2

        self.text = pygame.font.Font('freesansbold.ttf', 64).render(string, True, (35, 35, 35))
        self.textRect = self.text.get_rect().center = (self.x, self.y + 26)

        self.id = id
    
    def update(self, pos):
        self.color = (246, 110, 110)
        if pos == self.id:
            self.color = (174, 236, 152)
    
    def prints(self, screen, pos):
        self.update(pos)
        r = 20
        pygame.draw.rect  (screen, self.color, (self.x                      , self.y - r                , self.ancho - 2 * r  , self.alto        ))
        pygame.draw.rect  (screen, self.color, (self.x - r                  , self.y                    , self.ancho          , self.alto - 2 * r))
        pygame.draw.circle(screen, self.color, (self.x                      , self.y                    ),r)
        pygame.draw.circle(screen, self.color, (self.x + self.ancho - 2*r   , self.y                    ),r)
        pygame.draw.circle(screen, self.color, (self.x                      , self.y + self.alto - 2*r  ),r)
        pygame.draw.circle(screen, self.color, (self.x + self.ancho - 2*r   , self.y + self.alto - 2*r  ),r)
        screen.blit(self.text, self.textRect)
