import pygame
from pygame import *

pygame.init()

screen = pygame.display.set_mode((850,600))                 
display.set_caption("Ninja Fruit")
background = pygame.image.load("img/cinema.png").convert()


running = True
while running :
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            continuer = False
            quit()
        
pygame.quit()