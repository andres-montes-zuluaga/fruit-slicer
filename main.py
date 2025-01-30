import pygame
from pygame import *
from random import randint 
from functions.menu import draw_main_menu, draw_level_menu, draw_language_menu
from functions.launcher import draw_game, spawn_corn, spawn_specials_easy
from functions.events import handle_events

pygame.init()

# Window setup
window_width, window_height = 800, 600
window = display.set_mode((window_width, window_height))
display.set_caption('Corn Ninja')

# Load images
background_main_menu = image.load('assets/img/background_main_menu.jpg').convert()
background_play = image.load('assets/img/background_play.jpg').convert()
seau = image.load('assets/img/seau.jpg').convert_alpha()
corn_yellow = image.load('assets/img/corn_yellow.jpg').convert()
corn_red = image.load('assets/img/corn_red.jpg').convert()
corn_blue = image.load('assets/img/corn_blue.jpg').convert()
corn_green = image.load('assets/img/corn_green.jpg').convert()
bomb = image.load('assets/img/bomb.png').convert()
ice = image.load('assets/img/ice.png').convert_alpha()
life = image.load('assets/img/life.png').convert_alpha()
button_play = image.load('assets/img/button_play.jpg').convert()
button_lang = image.load('assets/img/button_lang.png').convert()

# Resize images if necessary
background_main_menu = transform.scale(background_main_menu, (window_width, window_height))
background_play = transform.scale(background_play, (window_width, window_height))
seau = transform.scale(seau, (110, 110))
corn_yellow = transform.scale(corn_yellow, (50, 50))
corn_red = transform.scale(corn_red, (50, 50))
corn_blue = transform.scale(corn_blue, (50, 50))
corn_green = transform.scale(corn_green, (50, 50))
bomb = transform.scale(bomb, (100, 100))
ice = transform.scale(ice, (100, 100))
life = transform.scale(life, (100, 100))
play_button = transform.scale(button_play, (70, 70))
lang_button = transform.scale(button_lang, (70, 70))


# Initial parameters
running = True
state = 0  # Initial state (menu)
clock = time.Clock()  # Create a clock object to control frame rate

# Game objects
objects = []  # List to store moving objects (corn and popcorn)
special_objects_easy = []  # List to store special objects (chicken, ice, heart)

# Main game loop

while running:
    # Get mouse position and click status
    mouse_pos = pygame.mouse.get_pos()
    state = handle_events(state, mouse_pos)

    if state == 0:  # Main menu
        draw_main_menu(window, background_main_menu, play_button, lang_button)

    elif state == 1:  # Difficulty menu
        draw_level_menu(window, background_main_menu)

    elif state == 2:  # Language menu
        draw_language_menu(window, background_main_menu)

    elif state == 3:  # Game state
        draw_game(window, background_play, seau, objects, special_objects_easy, corn_yellow, corn_red, corn_blue, corn_green, bomb, ice, life, window_width, window_height)
        # Spawn new objects randomly
        if randint(0, 100) < 1:  # 2% chance to spawn an object each frame
            spawn_corn(window_height, objects)
        # Spawn special_objects_easy randomly
        if randint(0, 200) < 1:  # 0.05% chance to spawn an object each frame
            spawn_specials_easy(window_height, special_objects_easy)
            
    display.flip()
    clock.tick(30)  # Limit the frame rate to 30 FPS