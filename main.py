import pygame
from pygame import *
from random import randint 
from functions.menu import draw_menu, draw_level_menu, draw_language_menu
from functions.launcher import draw_game, spawn_object

pygame.init()

# Window setup
window_width, window_height = 800, 600
window = display.set_mode((window_width, window_height))
display.set_caption('Corn Ninja')

# Load images
background_main_menu = image.load('assets/img/background_main_menu.jpg').convert()
background_play = image.load('assets/img/background_play.jpg').convert()
corn_yellow = image.load('assets/img/corn_yellow.jpg').convert()
corn_red = image.load('assets/img/corn_red.jpg').convert()
popcorn_yellow = image.load('assets/img/popcorn_yellow.jpg').convert()
button_play = image.load('assets/img/button_play.jpg').convert()
button_lang = image.load('assets/img/button_lang.png').convert()

# Resize images if necessary
background_main_menu = transform.scale(background_main_menu, (window_width, window_height))
background_play = transform.scale(background_play, (window_width, window_height))
corn= transform.scale(corn, (50, 50))
popcorn = transform.scale(popcorn, (50, 50))
play_button = transform.scale(button_play, (70, 70))
lang_button = transform.scale(button_lang, (70, 70))


# Initial parameters
running = True
state = 0  # Initial state (menu)

# Game objects
objects = []  # List to store moving objects (corn and popcorn)

# Main game loop
clock = time.Clock()  # Create a clock object to control frame rate
while running:
    for evt in event.get():  # Renamed the loop variable to 'evt'
        if evt.type == QUIT:
            running = False
            quit()

    keys = key.get_pressed()

    if state == 0:  # Main menu
        draw_menu(window, background_main_menu, play_button, lang_button)
        if keys[K_p]:  # Press 'P' to go to the difficulty menu
            state = 1
        if keys[K_l]:  # Press 'L' to go to the language menu
            state = 2

    elif state == 1:  # Difficulty menu
        draw_level_menu(window)
        if keys[K_e]:  # Press 'E' to select Easy and go to the game
            state = 3
        if keys[K_h]:  # Press 'H' to select Hard (not implemented yet)
            pass
        if keys[K_ESCAPE]:  # Press 'ESC' to return to the main menu
            state = 0

    elif state == 2:  # Language menu
        draw_language_menu(window)
        if keys[K_ESCAPE]:  # Press 'ESC' to return to the main menu
            state = 0

    elif state == 3:  # Game state
        draw_game(window, background_play, objects, corn_yellow, corn_red, popcorn_yellow, window_width, window_height)
        if keys[K_ESCAPE]:  # Press 'ESC' to return to the main menu
            state = 0

        # Spawn new objects randomly
        if randint(0, 100) < 5:  # 5% chance to spawn an object each frame
            spawn_object(window_height, objects)

    display.flip()
    clock.tick(30)  # Limit the frame rate to 30 FPS