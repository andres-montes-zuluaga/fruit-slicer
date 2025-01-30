from pygame import *


# Game functions
def draw_menu(window, background_main_menu, play_button, lang_button):
    window.blit(background_main_menu, (0, 0))
    play_button
    lang_button 
    window.blit(play_button, (90, 450))
    window.blit(lang_button, (90, 530))

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