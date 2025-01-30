import pygame
from pygame import *
from random import randint 
from functions.menu import draw_menu, draw_level_menu, draw_language_menu
from functions.launcher import draw_game, spawn_object

pygame.init()

# Window setup
window_width, window_height = 900, 700
window = display.set_mode((window_width, window_height))
display.set_caption('Corn Ninja')

# Load images
background = image.load('assets/img/cinema.png').convert()
corn = image.load('assets/img/mais.jpg').convert()
corn_red = image.load('assets/img/mais_rouge.jpg').convert()
popcorn = image.load('assets/img/popcorn.jpg').convert()

# Resize images if necessary
background = transform.scale(background, (window_width, window_height))
corn= transform.scale(corn, (50, 50))
corn_red= transform.scale(corn_red, (50, 50))
popcorn = transform.scale(popcorn, (50, 50))

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
        draw_menu(window)
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
        draw_game(window, background, objects, corn, corn_red, popcorn, window_width, window_height)
        if keys[K_ESCAPE]:  # Press 'ESC' to return to the main menu
            state = 0

        # Spawn new objects randomly
        if randint(0, 100) < 5:  # 5% chance to spawn an object each frame
            spawn_object(window_height, objects)

    display.flip()
    clock.tick(30)  # Limit the frame rate to 30 FPS