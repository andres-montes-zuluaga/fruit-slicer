import pygame 
from pygame import *

"""Constantes du jeu"""""

# Window setup
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('Corn Ninja')


# Load images
BACKGROUND_MAIN_MENU = image.load('assets/img/background_main_menu.jpg').convert()
BACKGROUND_PLAY = image.load('assets/img/background_play.jpg').convert()
BOX = image.load('assets/img/box.jpg').convert_alpha()
CORN_YELLOW = image.load('assets/img/corn_yellow.jpg').convert()
CORN_RED = image.load('assets/img/corn_red.jpg').convert()
CORN_BLUE = image.load('assets/img/corn_blue.jpg').convert()
CORN_GREEN = image.load('assets/img/corn_green.jpg').convert()
BOMB = image.load('assets/img/bomb.png').convert()
ICE = image.load('assets/img/ice.png').convert_alpha()
LIFE = image.load('assets/img/life.png').convert_alpha()
BUTTON_PLAY = image.load('assets/img/button_play.jpg').convert()
BUTTON_LANG = image.load('assets/img/button_lang.png').convert()

# Resize images if necessary
BACKGROUND_MAIN_MENU = transform.scale(BACKGROUND_MAIN_MENU, (WINDOW_WIDTH, WINDOW_HEIGHT))
BACKGROUND_PLAY = transform.scale(BACKGROUND_PLAY, (WINDOW_WIDTH, WINDOW_HEIGHT))
BOX = transform.scale(BOX, (110, 110))
CORN_YELLOW = transform.scale(CORN_YELLOW, (50, 50))
CORN_RED = transform.scale(CORN_RED, (50, 50))
CORN_BLUE = transform.scale(CORN_BLUE, (50, 50))
CORN_GREEN = transform.scale(CORN_GREEN, (50, 50))
BOMB = transform.scale(BOMB, (50, 50))
ICE = transform.scale(ICE, (50, 50))
LIFE = transform.scale(LIFE, (50, 50))
BUTTON_PLAY = transform.scale(BUTTON_PLAY, (70, 70))
BUTTON_LANG = transform.scale(BUTTON_LANG, (70, 70))


# Parabolic motion parameters
GRAVITY = 0.3  # Strength of gravity (affects the curve)