import pygame 
from pygame import *

"""Constantes du jeu"""""

# Window setup
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

WINDOW = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('Corn Ninja')

# Load images
background_main_menu = image.load('assets/img/background_main_menu.jpg').convert()
background_play = image.load('assets/img/background_play.jpg').convert()
box = image.load('assets/img/box.jpg').convert_alpha()
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
background_main_menu = transform.scale(background_main_menu, (WINDOW_WIDTH, WINDOW_HEIGHT))
background_play = transform.scale(background_play, (WINDOW_WIDTH, WINDOW_HEIGHT))
box = transform.scale(box, (110, 110))
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










# Parabolic motion parameters
GRAVITY = 0.5  # Strength of gravity (affects the curve)