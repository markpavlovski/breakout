import os

class GameConstants:

    # Game
    SCREEN_SIZE = (1080,800)
    FPS = 60
    ROW_LENGTH = 18

    # Bricks
    BRICK_SIZE = (60,25)
    BRICK_GAP = (0,0)
    SPRITE_BRICK_GREEN = os.path.join("assets", "green.png")
    SPRITE_BRICK_RED = os.path.join("assets", "red.png")
    SPRITE_BRICK_ORANGE = os.path.join("assets", "orange.png")
    SPRITE_BRICK_YELLOW = os.path.join("assets", "yellow.png")
    SPRITE_BRICK_BLUE = os.path.join("assets", "blue.png")
    SPRITE_SPEED_BRICK = os.path.join("assets", "yellow.png")
    SPRITE_LIFE_BRICK = os.path.join("assets", "yellow.png")

    # Ball
    BALL_SIZE = (16,16)
    BALL_SPEED = 10
    SPRITE_BALL = os.path.join("assets", "ball.png")

    # Pad
    PAD_SIZE = (150,25)
    SPRITE_PAD = os.path.join("assets", "pad.png")







    pass
