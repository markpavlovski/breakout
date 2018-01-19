import os

class GameConstants:
    SCREEN_SIZE = (472,600)
    BRICK_SIZE = (30,8)
    BRICK_GAP = (4,4)
    BALL_SIZE = (10,10)
    PAD_SIZE = (30,8)
    FPS = 60
    SPRITE_BALL = os.path.join("assets", "ball.png")
    SPRITE_BRICK = os.path.join("assets", "brick.png")
    SPRITE_BRICK_GREEN = os.path.join("assets", "brick_green.png")
    SPRITE_BRICK_PINK = os.path.join("assets", "brick_pink.png")
    SPRITE_BRICK_PURPLE = os.path.join("assets", "brick_purple.png")
    SPRITE_BRICK_YELLOW = os.path.join("assets", "brick_yellow.png")


    SPRITE_SPEED_BRICK = os.path.join("assets", "brick_speed.png")
    SPRITE_LIFE_BRICK = os.path.join("assets", "brick_life.png")
