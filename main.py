import pygame

pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((850, 600))                 
pygame.display.set_caption("Ninja Fruit")

# Chargement des images
background = pygame.image.load("assets/img/cinema.png").convert()
mais = pygame.image.load("assets/img/mais.jpg").convert()

running = True
while running:
    # Affichage du fond et des éléments
    screen.blit(background, (0, 0))
    screen.blit(mais, (230, 380))
    
    # Ajout d'un rectangle autour du maïs
    pygame.draw.rect(screen, (255, 0, 0), (230, 380, mais.get_width(), mais.get_height()), 3)

    pygame.display.flip()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

pygame.quit()
