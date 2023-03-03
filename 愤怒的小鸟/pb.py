import pygame
from random import randint
class Pig(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        y=randint(0,720)
        position=[1140,y]
        self.img = pygame.image.load('pg.png')
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.imge = self.img
        speed=[-4,0]
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)