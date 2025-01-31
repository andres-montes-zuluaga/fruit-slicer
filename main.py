import pygame
from pygame import *
from random import randint 
from functions.menu import draw_main_menu, draw_level_menu, draw_language_menu
from functions.launcher import draw_game, spawn_corn, spawn_specials_easy
from functions.events import handle_events

pygame.init()



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
        draw_game(window, background_play, box, objects, special_objects_easy, corn_yellow, corn_red, corn_blue, corn_green, bomb, ice, life, window_width, window_height)
        # Spawn new objects randomly
        if randint(0, 100) < 1:  # 2% chance to spawn an object each frame
            spawn_corn(window_height, objects)
        # Spawn special_objects_easy randomly
        if randint(0, 200) < 1:  # 0.05% chance to spawn an object each frame
            spawn_specials_easy(window_height, special_objects_easy)
            
    display.flip()
    clock.tick(30)  # Limit the frame rate to 30 FPS