import pygame
import sys
import renwu
import pb
from pygame.locals import *
pygame.init()
size=width,height=1140,720
screen=pygame.display.set_mode(size)
Renwu=renwu.Renwu()
i=0
group=pygame.sprite.Group()
if __name__=='__main__':
 while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    background = pygame.image.load('780.jfif')#加载图片
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(Renwu.img,Renwu.rect)
    i+=1
    if i%50==0:
        pib=pb.Pig()
        group.add(pib)
    for p in group.sprites():
        p.move()
        screen.blit(p.img,p.rect)
        if pygame.sprite.collide_circle(Renwu,p):
            final='game over'
            ft=pygame.font.SysFont('Arial',800)
            font=pygame.font.SysFont(None,50)
            ft1=font.render(final,1,(255,0,0))
            screen.blit(ft1,[screen.get_width()/2-ft1.get_width()/2,100])
            break
    pygame.display.update()
    key=pygame.key.get_pressed()
    if key[K_LEFT]:
        Renwu.move_left()
    if key[K_RIGHT]:
        Renwu.move_right()
    if key[K_UP]:
        Renwu.move_up()
    if key[K_DOWN]:
        Renwu.move_down()


