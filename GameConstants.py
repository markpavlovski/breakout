import os

class GameConstants:
    SCREEN_SIZE = (472,600)
    BRICK_SIZE = (30,8)
    BRICK_GAP = (4,4)
    BALL_SIZE = (10,10)
    PAD_SIZE = (30,8)
    FPS = 60
    SPRITE_BALL = os.path.join("Assets", "ball.png")
    SPRITE_BRICK = os.path.join("Assets", "brick.png")
    SPRITE_BRICK_GREEN = os.path.join("Assets", "brick_green.png")
    SPRITE_BRICK_PINK = os.path.join("Assets", "brick_pink.png")
    SPRITE_BRICK_PURPLE = os.path.join("Assets", "brick_purple.png")
    SPRITE_BRICK_YELLOW = os.path.join("Assets", "brick_yellow.png")


    SPRITE_SPEED_BRICK = os.path.join("Assets", "brick_speed.png")
    SPRITE_LIFE_BRICK = os.path.join("Assets", "brick_life.png")
