import pygame
from pygame.locals import *
from pygame import *
from random import randint, choice 
from module.constant import *
from functions.collision_object_events import *
import time


def draw_letter_above_object(WINDOW, font, obj):
    """
    Draw a random letter above the given object.
    """
    text = font.render(obj["letter"], True, (255, 255, 255))  # Utilise l'objet Font pour rendre le texte
    WINDOW.blit(text, (obj["x"] + 15, obj["y"] - 35))  # Affiche le texte à l'écran

def draw_game(
    WINDOW, BACKGROUND_PLAY, 
    BOX, 
    objects, special_objects_easy, 
    font,
    CORN_YELLOW, CORN_RED, CORN_BLUE, CORN_GREEN,
    POPCORN_YELLOW1, POPCORN_YELLOW2, POPCORN_YELLOW3,
    POPCORN_RED1, POPCORN_RED2, POPCORN_RED3,
    POPCORN_BLUE1, POPCORN_BLUE2, POPCORN_BLUE3,
    POPCORN_GREEN1, POPCORN_GREEN2, POPCORN_GREEN3,
    BOMB, ICE, LIFE, 
    WINDOW_WIDTH, WINDOW_HEIGHT):

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
        elif obj["type"] == "POPCORN_YELLOW1":  # Ajout de l'affichage
            WINDOW.blit(POPCORN_YELLOW1, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_YELLOW2":  # Ajout de l'affichage
            WINDOW.blit(POPCORN_YELLOW2, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_YELLOW3":  # Ajout de l'affichage
            WINDOW.blit(POPCORN_YELLOW3, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_RED1":
            WINDOW.blit(POPCORN_RED1, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_RED2":
            WINDOW.blit(POPCORN_RED2, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_RED3":
            WINDOW.blit(POPCORN_RED3, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_BLUE1":
            WINDOW.blit(POPCORN_BLUE1, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_BLUE2":
            WINDOW.blit(POPCORN_BLUE2, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_BLUE3":
            WINDOW.blit(POPCORN_BLUE3, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_GREEN1":
            WINDOW.blit(POPCORN_GREEN1, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_GREEN2":
            WINDOW.blit(POPCORN_GREEN2, (obj["x"], obj["y"]))
        elif obj["type"] == "POPCORN_GREEN3":
            WINDOW.blit(POPCORN_GREEN3, (obj["x"], obj["y"]))

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
        obj["vy"] += GRAVITY   # Apply gravity

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
      # Adjust speed based on object type
    if obj_type in ["CORN_YELLOW", "CORN_RED", "CORN_BLUE", "CORN_GREEN"]:
        vx = randint(5, 10)  # Horizontal speed
        vy = randint(-20, -10)  # Vertical speed (upwards)
    else:
        vx = randint(5, 10)  # Normal speed for other objects
        vy = randint(-20, -10)  # Normal vertical speed

    letter = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # Random letter

    objects.append({
        "type": obj_type, 
        "x": x, "y": y, 
        "vx": vx, "vy": vy, 
        "letter": letter
    })

def spawn_specials_easy(WINDOW_HEIGHT, special_objects_easy):
    """Spawn a new special object (bomb, ice, life) with random initial velocity."""
    obj_type = choice(["BOMB", "ICE", "LIFE"])  # Choisir aléatoirement un type d'objet spécial

    x = 0  # Start from the left side of the screen
    y = WINDOW_HEIGHT - 100  # Start near the bottom

    # Ajuster la vitesse selon l'objet spécial
    if obj_type in ["BOMB", "ICE", "LIFE"]:
        vx = randint(3, 6)  # Vitesse horizontale
        vy = randint(-20, -10)  # Vitesse verticale (vers le haut)

    letter = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # Lettre aléatoire

    special_objects_easy.append({
        "type": obj_type, 
        "x": x, "y": y, 
        "vx": vx, "vy": vy, 
        "letter": letter
    })


#duration = 3  # Ice effect duration in seconds
# Function to freeze all objects
def freeze_objects(duration, objects, special_objects_easy):
    #global objects, special_objects_easy
    original_velocities = []

    # Save original velocities and set them to 0
    for obj in objects + special_objects_easy:
        original_velocities.append((obj["vx"], obj["vy"]))
        obj["vx"] = 0
        obj["vy"] = 0

    # Wait for the specified duration
    time.sleep(duration)

    # Restore original velocities
    for i, obj in enumerate(objects + special_objects_easy):
        obj["vx"], obj["vy"] = original_velocities[i]


def transform_corn_to_popcorn(objects, keys):
    """
    Transforme un objet CORN_X en POPCORN_X1, POPCORN_X2, POPCORN_X3 si la bonne touche est pressée.
    """
    # Dictionnaire des variantes de popcorn pour chaque type de corn
    popcorn_variants = {
        "CORN_YELLOW": ["POPCORN_YELLOW1", "POPCORN_YELLOW2", "POPCORN_YELLOW3"],
        "CORN_RED": ["POPCORN_RED1", "POPCORN_RED2", "POPCORN_RED3"],
        "CORN_BLUE": ["POPCORN_BLUE1", "POPCORN_BLUE2", "POPCORN_BLUE3"],
        "CORN_GREEN": ["POPCORN_GREEN1", "POPCORN_GREEN2", "POPCORN_GREEN3"]
    }

    for obj in objects:
        if obj["type"] in popcorn_variants and keys[pygame.key.key_code(obj["letter"])]:
            obj["type"] = choice(popcorn_variants[obj["type"]])  # Transformation aléatoire en popcorn

def defuse_bomb(objects, special_objects_easy, keys):
    """
    Désactive la bombe si la bonne touche est pressée.
    Retire l'objet de la liste des objets et réinitialise le compte à rebours.
    """
    for obj in special_objects_easy:
        # Vérifier si l'objet est une bombe et si la bonne touche est pressée
        if obj["type"] == "BOMB" and keys[pygame.key.key_code(obj["letter"])]:
            # Retirer la bombe de la liste des objets
            if obj in special_objects_easy:
                special_objects_easy.remove(obj)
                
            # Réinitialiser les paramètres relatifs à la bombe
            global bomb_triggered, bomb_countdown
            bomb_triggered = False
            bomb_countdown = None

            # Affichage de la confirmation si besoin
            print("Bombe désactivée!")