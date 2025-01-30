from pygame import *
from random import randint 

# Parabolic motion parameters
gravity = 0.5  # Strength of gravity (affects the curve)

# Available letters for objects
availabe_letters =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def draw_game(window, background_play, objects, corn_yellow, popcorn, window_width, window_height):
    """Draw the game window, including objects and their associated letters."""
    window.blit(background_play, (0, 0))

    # Draw and update objects
    for obj in objects:
        obj["x"] += obj["vx"]  # Update horizontal position
        obj["y"] += obj["vy"]  # Update vertical position
        obj["vy"] += gravity  # Apply gravity

        # Draw the object
        if obj["type"] == "corn_yellow":
            window.blit(corn_yellow, (obj["x"], obj["y"]))
        elif obj["type"] == "popcorn":
            window.blit(popcorn, (obj["x"], obj["y"]))

        # Draw the letter associated with the object
        text = font.render(obj["letter"], True, (255, 0,0))
        window.blit(text, (obj["x"] + 20, obj["y"] + 20))
        # Remove objects that go off-screen
        if obj["x"] > window_width or obj["y"] > window_height:
            objects.remove(obj)

def spawn_object(window_height, objects):
    """Spawn a new object (corn or popcorn) with random initial velocity and a random letter."""
    obj_type = "corn_yellow" if randint(0, 1) == 0 else "popcorn"
    x = 0  # Start from the left side of the screen
    y = window_height - 100  # Start near the bottom
    vx = randint(5, 10)  # Random horizontal speed
    vy = randint(-20, -10)  # Random vertical speed (upwards)
    letter = choice(available_letters)  # Assign a random letter
    objects.append({"type": obj_type, "x": x, "y": y, "vx": vx, "vy": vy, "letter": letter})

def check_key_press(obj, key_pressed):
    """Check if the pressed key matches the object's letter."""
    return obj["letter"] == key_pressed.upper()  # Compare letters (uppercase)

def handle_events(objects, lives, score):
    """Handle keyboard events and update game state."""
    for event in event.get():
        if event.type == QUIT:  # Quit the game if the window is closed
            return False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:  # Quit the game with the Escape key
                return False
            else:
                # Convert the pressed key to a letter
                key_pressed = key.name(event.key).upper()
                for obj in objects:
                    if check_key_press(obj, key_pressed):
                        objects.remove(obj)  # Remove the object if the letter is correct
                        score += 1  # Increase the score
                        break
                else:
                    lives -= 1  # Lose a life if the key is incorrect
    return True

