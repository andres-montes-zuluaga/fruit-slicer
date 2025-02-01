import pygame
from random import randint, choice 
from pygame.locals import *
from module.constant import *
from functions.collision_object_events import *


start_time = pygame.time.get_ticks()
special_spawn_delay = 10000 #delay before special object spawn (milliseconds)


def degrees_to_radians(degrees):
    return (PI * degrees) / 180

# Approximation pour le calcul de cos et sin
def approx_cos(angle_deg):
    # Convertir l'angle en radians
    angle_rad = angle_deg * (3.141592653589793 / 180)
    # Approximation du cosinus via la série de Taylor
    return 1 - (angle_rad**2) / 2 + (angle_rad**4) / 24

def approx_sin(angle_deg):
    # Convertir l'angle en radians
    angle_rad = angle_deg * (3.141592653589793 / 180)
    # Approximation du sinus via la série de Taylor
    return angle_rad - (angle_rad**3) / 6 + (angle_rad**5) / 120

def draw_letter_above_object(WINDOW, font, obj):
    """
    Draw a random letter above the given object.
    """
    text = font.render(obj["letter"], True, (255, 0, 0))  # Utilise l'objet Font pour rendre le texte
    WINDOW.blit(text, (obj["x"] + 20, obj["y"] - 20))  # Affiche le texte à l'écran

def draw_game(
    WINDOW, BACKGROUND_PLAY, 
    BOX, 
    objects, special_objects_easy, 
    font,
    CORN_YELLOW, CORN_RED, CORN_BLUE, CORN_GREEN, 
    BOMB, ICE, LIFE, 
    WINDOW_WIDTH, WINDOW_HEIGHT):

    global start_time, special_spawn_delay

    WINDOW.blit(BACKGROUND_PLAY, (0, 0))
    WINDOW.blit(BOX, (0,490))

    all_objects = objects + special_objects_easy
    handle_collisions(all_objects, GRAVITY)  # Gérer les collisions avant d'afficher

    # Create a stack to hold objects to remove
    to_remove = []

    # Draw and update objects
    for obj in all_objects:
        obj["x"] += obj["vx"]  # Update horizontal position
        obj["y"] += obj["vy"]  # Update vertical position
        obj["vy"] += GRAVITY  # Apply gravity

        # Draw the object
        if obj["type"] == "CORN_YELLOW":
            WINDOW.blit(CORN_YELLOW, (obj["x"], obj["y"]))
        elif obj["type"] == "CORN_RED":
            WINDOW.blit(CORN_RED, (obj["x"], obj["y"]))
        elif obj["type"] == "CORN_BLUE":
            WINDOW.blit(CORN_BLUE, (obj["x"], obj["y"]))
        elif obj["type"] == "CORN_GREEN":
            WINDOW.blit(CORN_GREEN, (obj["x"], obj["y"]))

        draw_letter_above_object(WINDOW, font, obj)

        # Mark objects for removal if they go off-screen
        if obj["x"] > WINDOW_WIDTH or obj["y"] > WINDOW_HEIGHT:
            to_remove.append(obj)

    # Remove objects after iteration
    for obj in to_remove:
        if obj in objects:
            objects.remove(obj)

    # Create a stack to hold spécial objects to remove
    to_remove_specials= []

    # Draw and update special objects [easy mode]
        # Draw and update objects
    for obj in special_objects_easy:
        obj["x"] += obj["vx"]  # Update horizontal position
        obj["y"] += obj["vy"]  # Update vertical position
        obj["vy"] += GRAVITY * 0.4   # Apply gravity

        obj["time"] += 1

        # Draw the special object [easy mode]
        if  obj["type"] == "BOMB":
            WINDOW.blit(BOMB, (obj["x"], obj["y"]))
        elif obj["type"] == "ICE":
            WINDOW.blit(ICE, (obj["x"], obj["y"]))
        elif obj["type"] == "LIFE":
            WINDOW.blit(LIFE, (obj["x"], obj["y"]))

        draw_letter_above_object(WINDOW, font, obj)

        # Remove special objects [easy mode] that go off-screen
        if obj["x"] > WINDOW_WIDTH or obj["y"] > WINDOW_HEIGHT:
            to_remove_specials.append(obj)

def spawn_corn(WINDOW_HEIGHT, objects):
    """Spawn a new object (butter or popcorn) with random initial velocity."""
    obj_type = choice(["CORN_YELLOW", "CORN_RED", "CORN_BLUE", "CORN_GREEN"])
    
    x = 0  # Start from the left side of the screen
    y = WINDOW_HEIGHT - 100  # Start near the bottom

    angle_deg = randint(60, 80)
    speed = randint(15, 20)
 
    vx = speed * approx_cos(angle_deg)
    vy = -speed * approx_sin(angle_deg)

    letter = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # Random letter

    objects.append({
        "type": obj_type, 
        "x": x, "y": y, 
        "vx": vx, "vy": vy, 
        "letter": letter,
        "time": 0
    })

def spawn_specials_easy(WINDOW_HEIGHT, special_objects_easy):

    """Spawn a new special object (bomb, ice, life) with random initial velocity."""
    obj_type = choice(["BOMB", "ICE", "LIFE"])  # Choisir aléatoirement un type d'objet spécial

    x = 0  # Start from the left side of the screen
    y = WINDOW_HEIGHT - randint(50,100)  # Start near the bottom

    angle_deg = randint(60, 80)
    speed = randint(12, 18)  

    vx = speed * approx_cos(angle_deg)
    vy = -speed * approx_sin(angle_deg)

    letter = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # Lettre aléatoire

    special_objects_easy.append({
        "type": obj_type, 
        "x": x, "y": y, 
        "vx": vx, "vy": vy, 
        "letter": letter,
        "time": 0
    })
