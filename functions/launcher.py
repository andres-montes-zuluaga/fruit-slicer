from pygame import *
from random import randint


# Parabolic motion parameters
gravity = 0.5  # Strength of gravity (affects the curve)

def draw_game(window, background_play, objects, corn_yellow, corn_red, popcorn, window_width, window_height):
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
        elif obj["type"] == "popcorn":
            window.blit(popcorn, (obj["x"], obj["y"]))

        # Remove objects that go off-screen
        if obj["x"] > window_width or obj["y"] > window_height:
            objects.remove(obj)

def spawn_object(window_height, objects):
    """Spawn a new object (butter or popcorn) with random initial velocity."""
    if randint(0, 2) == 0:
        obj_type = "corn_yellow"
    elif randint(0, 2) == 1:
        obj_type = "corn_red"
    else:
        obj_type = "popcorn"
    #obj_type = "mais" if randint(0, 2) == 0 elif "corn_red" else "popcorn"
    x = 0  # Start from the left side of the screen
    y = window_height - 100  # Start near the bottom
    vx = randint(5, 10)  # Random horizontal speed
    vy = randint(-20, -10)  # Random vertical speed (upwards)
    objects.append({"type": obj_type, "x": x, "y": y, "vx": vx, "vy": vy})