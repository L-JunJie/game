import pygame
class Renwu(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        position=230,230
        self.img=pygame.image.load('rwu1.PNG')
        self.rect=self.img.get_rect()
        self.rect.center=position
        self.imge=self.img
    def move_left(self):
        self.speed=[-5,0]
        if self.rect.left<=0:
            self.rect.left=0
        else:
            self.rect=self.rect.move(self.speed)

    def move_right(self):
        self.speed = [5, 0]
        if self.rect.right>=1140:
            self.rect.right = 1140
        else:
            self.rect = self.rect.move(self.speed)
    def move_up(self):
        self.speed = [0,-5]
        if self.rect.top<=0:
            self.rect.top = 0
        else:
            self.rect = self.rect.move(self.speed)
    def move_down(self):
        self.speed = [0,5]
        if self.rect.bottom>=720:
            self.rect.bottom = 720
        else:
            self.rect = self.rect.move(self.speed)