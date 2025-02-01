import pygame
from pygame import *
from random import randint 
from functions.menu import draw_main_menu, draw_level_menu, draw_language_menu
from functions.launcher import draw_game, spawn_corn, spawn_specials_easy, freeze_objects
from functions.button_events import *
from module.constant import *
from functions.collision_object_events import *

pygame.init()
pygame.mixer.init()

# Load sounds & music
cinema_sound = pygame.mixer.Sound('assets/snd/cinema.wav')
game_music = 'assets/snd/music.wav'

popcorn_snd = pygame.mixer.Sound('assets/snd/popcorn.mp3')

# Load images
bomb_big_img = pygame.image.load('assets/img/bomb_big.png')

font = pygame.font.Font(None, 56)  # ✅ Créé UNE SEULE FOIS avant la boucle du jeu
font.set_bold(True)

# Initial parameters
running = True
state = 0  # Initial state (menu)
clock = time.Clock()  # Create a clock object to control frame rate
cinema_on = False  # Set to False to ensure cinema_sound plays initially
music_on = False
bomb_countdown = None  # Countdown timer for bomb
bomb_triggered = False  # Flag to check if bomb is triggered

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

        # Check for bomb countdown
        if bomb_triggered:
            if bomb_countdown is None:
                bomb_countdown = pygame.time.get_ticks() + 2000  # 2 seconds countdown
            elif pygame.time.get_ticks() >= bomb_countdown:
                # Display "GAME OVER" and bomb image
                WINDOW.blit(BOMB_BIG, (0, 0))
                game_over_text = font.render("GAME OVER", True, (255, 0, 0))
                WINDOW.blit(game_over_text, (0, 0))
                display.flip()
                pygame.time.delay(5000)  # Display for 5 seconds
                state = 0  # Return to main menu
                bomb_triggered = False
                bomb_countdown = None
                objects.clear()
                special_objects_easy.clear()
                continue

        # Spawn new objects randomly
        if randint(0, 200) < 2:  # 2% chance to spawn an object each frame
            spawn_corn(WINDOW_HEIGHT, objects)
        # Spawn special_objects_easy randomly
        if randint(0, 400) < 1:  # 0.05% chance to spawn an object each frame
            spawn_specials_easy(WINDOW_HEIGHT, special_objects_easy)
        
        keys = pygame.key.get_pressed()
                
        for obj in objects + special_objects_easy:
            # Check if the key for the ICE object is pressed
            if obj["type"] == "ICE" and keys[pygame.key.key_code(obj["letter"])]:
                freeze_objects(5, objects, special_objects_easy)
            # Check if the key for the BOMB object is pressed
            if obj["type"] == "BOMB" and keys[pygame.key.key_code(obj["letter"])]:
                bomb_triggered = False
                bomb_countdown = None

            if obj["type"] == "BOMB":
                bomb_triggered = True

    display.flip()
    clock.tick(30)  # Limit the frame rate to 30 FPS