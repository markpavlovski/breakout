import os

class GameConstants:

    # Game
    SCREEN_SIZE = (1080,800)
    FPS = 40
    ROW_LENGTH = 18
    MOVEMENT_INCREMENT = 2

    # Scenes

    PLAYING_SCENE = 0
    GAMEOVER_SCENE = 1
    HIGHSCORE_SCENE = 2
    MENU_SCENE = 3


    # Bricks
    BRICK_SIZE = (60,25)
    BRICK_GAP = (0,0)
    BRICK_HIT_POINTS = 100
    SPRITE_BRICK_GREEN = os.path.join("assets", "green.png")
    SPRITE_BRICK_RED = os.path.join("assets", "red.png")
    SPRITE_BRICK_ORANGE = os.path.join("assets", "orange.png")
    SPRITE_BRICK_YELLOW = os.path.join("assets", "yellow.png")
    SPRITE_BRICK_BLUE = os.path.join("assets", "blue.png")
    SPRITE_BRICK_SPEED = os.path.join("assets", "grey.png")
    SPRITE_BRICK_LIFE = os.path.join("assets", "white.png")

    # Ball
    BALL_SIZE = (16,16)
    BALL_SPEED = 10
    SPRITE_BALL = os.path.join("assets", "ball.png")

    # Pad
    PAD_SIZE = (150,25)
    PAD_SPEED = 15
    SPRITE_PAD = os.path.join("assets", "pad.png")







    pass
