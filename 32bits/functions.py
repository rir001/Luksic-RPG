import pygame
import tablero

bit = 16
step = bit * 6

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h


class mapa():
    def __init__(self, pos, name):
        self.x = pos[0]
        self.y = pos[1]
        self.update(0, 0)
        self.surf = pygame.image.load(f'Maps/{name}.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (len(tablero.tabla[1]) * step, len(tablero.tabla) * step)).convert_alpha()

    def update(self, x, y):
        self.pos_x = self.x * step + x - step/2
        self.pos_y = self.y * step + y - step/2
    
    def prints(self, screen):
        return screen.blit(self.surf, (self.pos_x , self.pos_y))


class people():
    def __init__(self, pos, name):
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.update(0, 0)
        self.load()
        self.see = 'front'
    
    def update(self, x, y):
        self.pos_x = self.x * step + x - step/2
        self.pos_y = self.y * step + y - step/2
    
    
    def load(self):
        self.dir =  {'front': pygame.image.load(f'Textures/{self.name}/0-0.png'),
                     'back':  pygame.image.load(f'Textures/{self.name}/3-0.png'),
                     'left':  pygame.image.load(f'Textures/{self.name}/1-0.png'),
                     'right': pygame.image.load(f'Textures/{self.name}/2-0.png'),
                    }

        for n in self.dir:
            self.dir[n] = pygame.transform.scale(self.dir[n], (step, step*2)).convert_alpha()


    def prints(self, screen):
        return screen.blit(self.dir[self.see], (self.pos_x , self.pos_y-step))
    


class player():
    def __init__(self):
        self.load()
        self.update('back')
        self.step = 0

    def update(self, see):
        self.see = see
        self.surf = self.dir[see][0]
    
    
    def load(self):
        self.dir =  {'front': [pygame.image.load('Textures/player/0-0.png'),
                               pygame.image.load('Textures/player/0-1.png'),
                               pygame.image.load('Textures/player/0-3.png')
                               ],
                     'back':  [pygame.image.load('Textures/player/3-0.png'),
                               pygame.image.load('Textures/player/3-1.png'),
                               pygame.image.load('Textures/player/3-3.png')
                               ],
                     'left':  [pygame.image.load('Textures/player/1-0.png'),
                               pygame.image.load('Textures/player/1-1.png'),
                               pygame.image.load('Textures/player/1-3.png')
                               ],
                     'right': [pygame.image.load('Textures/player/2-0.png'),
                               pygame.image.load('Textures/player/2-1.png'),
                               pygame.image.load('Textures/player/2-3.png')
                               ]}
        for n in self.dir:
            for m in range(len(self.dir[n])):
                self.dir[n][m] = pygame.transform.scale(self.dir[n][m], (step, step*2)).convert_alpha()

    
    def prints(self, screen, frames, z, goo, a):

        if 1 < z < frames-1 and goo:
            if a%2 == 0:
                self.surf = self.dir[self.see][1]
            else:
                self.surf = self.dir[self.see][2]
        else:
            self.surf = self.dir[self.see][0]
        return screen.blit(self.surf, (SCREEN_WIDTH/2-step/2, SCREEN_HEIGHT/2-(step*1.5)))

