import pygame
from random import randint 
from functions.menu import draw_main_menu, draw_level_menu, draw_language_menu
from functions.launcher import *
from functions.button_events import *
from module.constant import *
from functions.collision_object_events import *

pygame.init()
pygame.mixer.init()

# Load sounds & music
cinema_sound = pygame.mixer.Sound('assets/snd/cinema.wav')
game_music = 'assets/snd/music.wav'

popcorn_snd = pygame.mixer.Sound('assets/snd/popcorn.mp3')

font = pygame.font.Font(None, 56)  
font.set_bold(True)

# Initial parameters
running = True
state = 0  # Initial state (menu)
clock = time.Clock()  # Create a clock object to control frame rate
cinema_on = False  # Set to False to ensure cinema_sound plays initially
music_on = False

# Game objects
objects = []  # List to store moving objects (corn and popcorn)
special_objects_easy = []  # List to store special objects (chicken, ice, heart)

# Play the initial cinema sound
cinema_sound.play(-1)
cinema_on = True

# Main game loop
while running:
    # Get mouse position and click status
    mouse_pos = pygame.mouse.get_pos()
    state = button_events(state, mouse_pos)
    
    if state == 0:  # Main menu
        draw_main_menu(WINDOW, BACKGROUND_MAIN_MENU, BUTTON_PLAY, BUTTON_LANG)
        if not cinema_on:
            pygame.mixer.music.stop()
            cinema_sound.play(-1)
            cinema_on = True
            music_on = False

    elif state == 1:  # Difficulty menu
        draw_level_menu(WINDOW, BACKGROUND_MAIN_MENU)
        if not cinema_on:
            pygame.mixer.music.stop()
            cinema_sound.play(-1)
            cinema_on = True
            music_on = False
            
    elif state == 2:  # Language menu
        draw_language_menu(WINDOW, BACKGROUND_MAIN_MENU)
        if not cinema_on:
            pygame.mixer.music.stop()
            cinema_sound.play(-1)
            cinema_on = True
            music_on = False
            
    elif state == 3:  # Game state
        draw_game(WINDOW, BACKGROUND_PLAY, 
                  BOX, 
                  objects, special_objects_easy, 
                  font,
                  CORN_YELLOW, CORN_RED, CORN_BLUE, CORN_GREEN, 
                  BOMB, ICE, LIFE, 
                  WINDOW_WIDTH, WINDOW_HEIGHT)
        if not music_on:
            cinema_sound.stop()
            pygame.mixer.music.load(game_music)
            pygame.mixer.music.play(-1)
            cinema_on = False
            music_on = True

       
        # Spawn new objects with a natural movement
        if randint(0, 100) < 2:  # 2% chance to spawn an object each frame
            spawn_corn(WINDOW_HEIGHT, objects)

        # Spawn special objects (with a delay and lower probability)
        current_time = pygame.time.get_ticks()
        if current_time - start_time > special_spawn_delay and randint(0, 300) < 2:  
            spawn_specials_easy(WINDOW_HEIGHT, special_objects_easy)

        # Remove off-screen objects
        objects = [obj for obj in objects if -50 < obj["x"] < WINDOW_WIDTH + 50 and -50 < obj["y"] < WINDOW_HEIGHT + 50]
        special_objects_easy = [obj for obj in special_objects_easy if -50 < obj["x"] < WINDOW_WIDTH + 50 and -50 < obj["y"] < WINDOW_HEIGHT + 50]

    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 30 FPS