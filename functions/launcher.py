import pygame
from pygame import *
from random import randint, choice 
from module.constant import *


def draw_letter_above_object(WINDOW, font, obj):
    """
    Draw a random letter above the given object.
    """

    font = pygame.font.Font(None, 56)  # Default system font, size 36
    font.set_bold(True)
    text = font.render(obj["letter"], True, (255, 0, 0))  # Utilise l'objet Font pour rendre le texte
    WINDOW.blit(text, (obj["x"] + 20, obj["y"] - 20))  # Affiche le texte à l'écran

def draw_game(
    WINDOW, BACKGROUND_PLAY, 
    BOX, 
    objects, special_objects_easy, 
    CORN_YELLOW, CORN_RED, CORN_BLUE, CORN_GREEN, 
    BOMB, ICE, LIFE, 
    WINDOW_WIDTH, WINDOW_HEIGHT):
    
    WINDOW.blit(BACKGROUND_PLAY, (0, 0))
    WINDOW.blit(BOX, (0,490))

    # Draw and update objects
    for obj in objects:
        obj["x"] += obj["vx"]  # Update horizontal position
        obj["y"] += obj["vy"]  # Update vertical position
        obj["vy"] += GRAVITY  # Apply gravity

        # Draw the object
        if obj["type"] == "corn_yellow":
            WINDOW.blit(CORN_YELLOW, (obj["x"], obj["y"]))
        elif obj["type"] == "CORN_RED":
            WINDOW.blit(CORN_RED, (obj["x"], obj["y"]))
        elif obj["type"] == "CORN_BLUE":
            WINDOW.blit(CORN_BLUE, (obj["x"], obj["y"]))
        elif obj["type"] == "corn_green":
            WINDOW.blit(CORN_GREEN, (obj["x"], obj["y"]))

        draw_letter_above_object(WINDOW, font, obj)

        # Remove objects that go off-screen
        if obj["x"] > WINDOW_WIDTH or obj["y"] > WINDOW_HEIGHT:
            objects.remove(obj)

    # Draw and update special objects [easy mode]
        # Draw and update objects
    for obj in special_objects_easy:
        obj["x"] += obj["vx"]  # Update horizontal position
        obj["y"] += obj["vy"]  # Update vertical position
        obj["vy"] += GRAVITY  # Apply gravity

        # Draw the special object [easy mode]
        if  obj["type"] == "bomb":
            WINDOW.blit(BOMB, (obj["x"], obj["y"]))
        elif obj["type"] == "ice":
            WINDOW.blit(ICE, (obj["x"], obj["y"]))
        elif obj["type"] == "life":
            WINDOW.blit(LIFE, (obj["x"], obj["y"]))

        draw_letter_above_object(WINDOW, font, obj)

        # Remove special objects [easy mode] that go off-screen
        if obj["x"] > WINDOW_WIDTH or obj["y"] > WINDOW_HEIGHT:
            special_objects_easy.remove(obj)

def spawn_corn(WINDOW_HEIGHT, objects):
    """Spawn a new object (butter or popcorn) with random initial velocity."""
    if randint(0, 3) == 0:
        obj_type = "CORN_YELLOW"
    elif randint(0, 3) == 1:
        obj_type = "CORN_RED"
    elif randint(0, 3) == 2:
        obj_type = "CORN_BLUE"
    else:
        obj_type = "CORN_GREEN"
    x = 0  # Start from the left side of the screen
    y = WINDOW_HEIGHT - 100  # Start near the bottom
    vx = randint(5, 10)  # Random horizontal speed
    vy = randint(-20, -10)  # Random vertical speed (upwards)
    letter = choice ("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # Random letter
    objects.append({
        "type": obj_type, 
        "x": x, "y": y, 
        "vx": vx, "vy": vy, 
        "letter": letter
        })

def spawn_specials_easy(window_height, special_objects_easy):
    """Spawn a new special object (bomb, ice, life) with random initial velocity."""
    if randint(0, 2) == 0:
        obj_type = "BOMB"
    elif randint(0, 2) == 1:
        obj_type = "ICE"
    else:
        obj_type = "LIFE"
    x = 0  # Start from the left side of the screen
    y = window_height - 100  # Start near the bottom
    vx = randint(8, 12)  # Random horizontal speed
    vy = randint(-22, -12)  # Random vertical speed (upwards)
    letter = choice ("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # Random letter
    special_objects_easy.append({
        "type": obj_type, 
        "x": x, "y": y, 
        "vx": vx, "vy": vy, 
        "letter": letter
        })


