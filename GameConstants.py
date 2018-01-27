import os

class GameConstants:

    # Game
    SCREEN_SIZE = (1080,800)
    FPS = 20
    ROW_LENGTH = 18
    MOVEMENT_INCREMENT = 1
    LIVES = 20
    SPRITE_MENU = os.path.join("assets", "main_menu.png")

    # High Scores
    HIGHSCORE_DATA = "highscore.dat"
    HIGHSCORE_KEPT_SIZE = 5
    HIGHSCORE_USER_NAME_LENGTH = 6
    HIGHSCORE_FONT_SIZE = 50
    SPRITE_HIGHSCORE = os.path.join("assets", "high_score.png")

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
    BALL_SPEED = 20
    SPRITE_BALL = os.path.join("assets", "ball.png")

    # Pad
    PAD_SIZE = (150,25)
    PAD_SPEED = 35
    SPRITE_PAD = os.path.join("assets", "pad.png")

    # Sounds
    SOUND_FILE_NEW_GAME = os.path.join("assets","sounds", "new_game.wav")
    SOUND_FILE_GAME_OVER = os.path.join("assets","sounds", "game_over.wav")
    SOUND_FILE_HIT_BRICK = os.path.join("assets", "sounds", "berimbau_high.wav")
    SOUND_FILE_HIT_BRICK_LIFE = os.path.join("assets", "sounds", "bonus_life.wav")
    SOUND_FILE_HIT_BRICK_SPEED = os.path.join("assets", "sounds", "speed.wav")
    SOUND_FILE_HIT_WALL = os.path.join("assets", "sounds", "berimbau_dirty.wav")
    SOUND_FILE_HIT_PAD = os.path.join("assets", "sounds", "berimbau_low.wav")
    SOUND_FILE_NEXT_LEVEL = os.path.join("assets", "sounds", "next_level.wav")
    SOUND_FILE_YOU_DIE = os.path.join("assets", "sounds", "you_die.wav")
    SOUND_FILE_HIGH_SCORES = os.path.join("assets", "sounds", "high_scores.wav")




    SOUND_GAME_OVER = 0
    SOUND_HIT_BRICK = 1
    SOUND_HIT_BRICK_LIFE = 2
    SOUND_HIT_BRICK_SPEED = 3
    SOUND_HIT_WALL = 4
    SOUND_HIT_PAD = 5
    SOUND_NEW_GAME = 6
    SOUND_NEXT_LEVEL = 7
    SOUND_YOU_DIE = 8
    SOUND_HIGH_SCORES = 9




    pass
