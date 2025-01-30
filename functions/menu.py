from pygame import *


# Game functions
def draw_main_menu(window, background_main_menu, button_play, button_lang):
    window.blit(background_main_menu, (0, 0))
    button_lang
    button_lang 
    window.blit(button_play, (90, 430))
    window.blit(button_lang, (90, 510))

def draw_level_menu(window, background_main_menu):
    window.blit(background_main_menu, (0, 0))
    font_button = font.SysFont('comicsansms', 36)
    button_easy = font_button.render('Easy', True, (255, 255, 255))
    button_hard = font_button.render('Hard', True, (255, 255, 255))
    window.blit(button_easy, (90, 430))
    window.blit(button_hard, (90, 510))

def draw_language_menu(window, background_main_menu):
    window.blit(background_main_menu, (0, 0))
    font_button = font.SysFont('comicsansms', 26)
    button_english = font_button.render('English', True, (255, 255, 255))
    button_french = font_button.render('French', True, (255, 255, 255))
    button_spanish = font_button.render('Spanish', True, (255, 255, 255))
    window.blit(button_english, (90, 430))
    window.blit(button_french, (90, 480))
    window.blit(button_spanish, (90, 530))