from pygame import *
from random import randint

# Game functions
def draw_menu(window):
    window.fill((255, 0, 0))  # Red background
    font_title = font.SysFont('comicsansms', 72)
    title = font_title.render('Corn Ninja', True, (255, 255, 255))
    window.blit(title, (250, 100))

    font_button = font.SysFont('comicsansms', 36)
    play_button = font_button.render('Play', True, (255, 255, 255))
    language_button = font_button.render('Languages', True, (255, 255, 255))
    window.blit(play_button, (400, 300))
    window.blit(language_button, (380, 400))

def draw_level_menu(window):
    window.fill((0, 0, 255))  # Blue background
    font_button = font.SysFont('comicsansms', 36)
    easy_button = font_button.render('Easy', True, (255, 255, 255))
    hard_button = font_button.render('Hard', True, (255, 255, 255))
    window.blit(easy_button, (400, 300))
    window.blit(hard_button, (400, 400))

def draw_language_menu(window):
    window.fill((0, 255, 0))  # Green background
    font_button = font.SysFont('comicsansms', 36)
    english_button = font_button.render('English', True, (255, 255, 255))
    french_button = font_button.render('French', True, (255, 255, 255))
    spanish_button = font_button.render('Spanish', True, (255, 255, 255))
    window.blit(english_button, (400, 300))
    window.blit(french_button, (400, 400))
    window.blit(spanish_button, (400, 500))