from pygame import *
from random import randint


# Parabolic motion parameters
gravity = 0.5  # Strength of gravity (affects the curve)

def draw_game(window, background_play, objects, special_objects_easy, corn_yellow, corn_red, corn_blue, corn_green, bomb, ice, life, window_width, window_height):
    window.blit(background_play, (0, 0))

    # Draw and update objects
    for obj in objects:
        obj["x"] += obj["vx"]  # Update horizontal position
        obj["y"] += obj["vy"]  # Update vertical position
        obj["vy"] += gravity  # Apply gravity

        # Draw the object
        if obj["type"] == "corn_yellow":
            window.blit(corn_yellow, (obj["x"], obj["y"]))
        elif obj["type"] == "corn_red":
            window.blit(corn_red, (obj["x"], obj["y"]))
        elif obj["type"] == "corn_blue":
            window.blit(corn_blue, (obj["x"], obj["y"]))
        elif obj["type"] == "corn_green":
            window.blit(corn_green, (obj["x"], obj["y"]))
        elif obj["type"] == "bomb":
            window.blit(bomb, (obj["x"], obj["y"]))
        elif obj["type"] == "ice":
            window.blit(ice, (obj["x"], obj["y"]))
        elif obj["type"] == "life":
            window.blit(life, (obj["x"], obj["y"]))

        # Remove objects that go off-screen
        if obj["x"] > window_width or obj["y"] > window_height:
            objects.remove(obj)

    # Draw and update special objects [easy mode]
        # Draw and update objects
    for obj in special_objects_easy:
        obj["x"] += obj["vx"]  # Update horizontal position
        obj["y"] += obj["vy"]  # Update vertical position
        obj["vy"] += gravity  # Apply gravity

        # Draw the special object [easy mode]
        if  obj["type"] == "bomb":
            window.blit(bomb, (obj["x"], obj["y"]))
        elif obj["type"] == "ice":
            window.blit(ice, (obj["x"], obj["y"]))
        elif obj["type"] == "life":
            window.blit(life, (obj["x"], obj["y"]))

        # Remove special objects [easy mode] that go off-screen
        if obj["x"] > window_width or obj["y"] > window_height:
            special_objects_easy.remove(obj)

def spawn_corn(window_height, objects):
    """Spawn a new object (butter or popcorn) with random initial velocity."""
    if randint(0, 3) == 0:
        obj_type = "corn_yellow"
    elif randint(0, 3) == 1:
        obj_type = "corn_red"
    elif randint(0, 3) == 2:
        obj_type = "corn_blue"
    else:
        obj_type = "corn_green"
    x = 0  # Start from the left side of the screen
    y = window_height - 100  # Start near the bottom
    vx = randint(5, 10)  # Random horizontal speed
    vy = randint(-20, -10)  # Random vertical speed (upwards)
    objects.append({"type": obj_type, "x": x, "y": y, "vx": vx, "vy": vy})

def spawn_specials_easy(window_height, special_objects_easy):
    """Spawn a new special object (bomb, ice, life) with random initial velocity."""
    if randint(0, 2) == 0:
        obj_type = "bomb"
    elif randint(0, 2) == 1:
        obj_type = "ice"
    else:
        obj_type = "life"
    x = 0  # Start from the left side of the screen
    y = window_height - 100  # Start near the bottom
    vx = randint(8, 12)  # Random horizontal speed
    vy = randint(-22, -12)  # Random vertical speed (upwards)
    special_objects_easy.append({"type": obj_type, "x": x, "y": y, "vx": vx, "vy": vy})