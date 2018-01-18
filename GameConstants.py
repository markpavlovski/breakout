import os

class GameConstants:
    SCREEN_SIZE = (800,600)
    BRICK_SIZE = (30,8)
    BRICK_GAP = (2,2)
    BALL_SIZE = (10,10)
    PAD_SIZE = (30,8)
    SPRITE_BALL = os.path.join("Assets", "ball.png")
    SPRITE_BRICK = os.path.join("Assets", "brick.png")
    SPRITE_SPEED_BRICK = os.path.join("Assets", "brick_speed.png")
    SPRITE_LIFE_BRICK = os.path.join("Assets", "brick_life.png")
    FPS = 60
