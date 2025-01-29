class Element:
    def __init__(self, spece, name, letter, size, speed, position, reaction):
        self.spece = spece # 0 = fruit, 1 = special
        self.name = name
        self.letter = letter # A letter for fruits, A sequence numerique for Bombs & Ices
        self.size = size # (,) Two numbers tuple
        self.speed = speed # Number
        self.position = position # (,) Two numbers tuple
        self.reaction = reaction # S = slice, E = explosion, D = desactivate F = freeze, R = restore
    
    def movement(self):
        print("This is a " + self.name + " movement!")

    def slice(self):
        print("This is a " + self.name + " sliced! la pouvre fruit!")

    def turn_off_bomb(self):
        print("You have deactivated a bomb!")

    def explosion(self):
        print("The bomb exploded... sorry")

    def turn_on_frezzer(self):
        print("You froze the time! Enjoy and cut the corn!")

    def restore_heart(self):
        print("Super! You got a heart back!")




fruit1 = Element(0, "Banana", "B", (50,50), 5, (0, 0), "S")

fruit1.movement()
fruit1.slice()


bomb1 = Element(1, "Bomb", "1243", (50,50), 8, (0, 0), "E")

bomb1.turn_off_bomb()
bomb1.explosion()


ice1 = Element(1, "Ice", "asdf", (50,50), 8, (0, 0), "F")

ice1.turn_on_frezzer()


heart1 = Element(1, "Heart", "heart", (50,50), 5, (0, 0), "R")

heart1.restore_heart()