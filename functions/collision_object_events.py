import pygame
from pygame.locals import *

def check_collision(obj1, obj2):
    """Vérifie si deux objets sont en collision."""
    rect1 = pygame.Rect(obj1["x"], obj1["y"], 50, 50)  
    rect2 = pygame.Rect(obj2["x"], obj2["y"], 50, 50)
    return rect1.colliderect(rect2)

def handle_collisions(objects, GRAVITY):
    """Gère les collisions en inversant la direction des objets."""
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            if check_collision(objects[i], objects[j]):
                objects[i]["vx"] = objects[i]["vx"] 
                objects[i]["vy"] = objects[i]["vy"] 

                objects[j]["vx"] = objects[j]["vx"] 
                objects[j]["vy"] = objects[j]["vy"] 

                # Ajouter de la gravité après la collision, pour que les objets tombent vers le bas
                objects[i]["vy"] += GRAVITY
                objects[j]["vy"] += GRAVITY