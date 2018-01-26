import pygame
import os
import fileinput
import random
from GameConstants import *
from Brick import *
from SpeedBrick import *
from LifeBrick import *

class Level:
    def __init__(self,game):
        self.__game = game
        self.__bricks = []
        self.__amount_of_bricks_left = 0
        self.__current_level = 0

    def get_bricks(self):
        return self.__bricks

    def get_amount_of_bricks_left(self):
        return self.__amount_of_bricks_left

    def brick_hit(self):
        self.__amount_of_bricks_left -= 1

    def load_nex_level(self):
        pass

    def load(self, level):
        self.__current_level = level
        self.__bricks = []
        x,y = 0,0

        for line in fileinput.input(os.path.join("assets","levels","level{}.dat".format(level))):
            for item in line:
                if item == "1":
                    brick = Brick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_RED), self.__game)
                    self.__bricks.append(brick)
                    self.__amount_of_bricks_left += 1

                elif item == "2":
                    brick = Brick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_ORANGE), self.__game)
                    self.__bricks.append(brick)
                    self.__amount_of_bricks_left += 1

                elif item == "3":
                    brick = Brick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_YELLOW), self.__game)
                    self.__bricks.append(brick)
                    self.__amount_of_bricks_left += 1

                elif item == "4":
                    brick = Brick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_GREEN), self.__game)
                    self.__bricks.append(brick)
                    self.__amount_of_bricks_left += 1

                elif item == "5":
                    brick = Brick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_BLUE), self.__game)
                    self.__bricks.append(brick)
                    self.__amount_of_bricks_left += 1

                elif item == "S":
                    brick = SpeedBrick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_SPEED), self.__game)
                    self.__bricks.append(brick)
                    self.__amount_of_bricks_left += 1

                elif item == "L":
                    brick = LifeBrick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_LIFE), self.__game)
                    self.__bricks.append(brick)
                    self.__amount_of_bricks_left += 1

                x += GameConstants.BRICK_SIZE[0] + GameConstants.BRICK_GAP[0]
            x = 0
            y += GameConstants.BRICK_SIZE[1] + GameConstants.BRICK_GAP[1]

    def load_random(self):
        self.__bricks = []
        x,y = 0,0

        new_bricks = int(GameConstants.SCREEN_SIZE[0]/GameConstants.BRICK_SIZE[0])
        rows = random.randint(1,10)

        for row in range(rows+5):
            for brick in range(new_bricks):
                if row > 4:
                    item = str(random.randint(0,5))
                    if item == "1":
                        brick = Brick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_RED), self.__game)
                        self.__bricks.append(brick)
                        self.__amount_of_bricks_left += 1

                    elif item == "2":
                        brick = Brick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_ORANGE), self.__game)
                        self.__bricks.append(brick)
                        self.__amount_of_bricks_left += 1

                    elif item == "3":
                        brick = Brick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_YELLOW), self.__game)
                        self.__bricks.append(brick)
                        self.__amount_of_bricks_left += 1

                    elif item == "4":
                        brick = Brick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_GREEN), self.__game)
                        self.__bricks.append(brick)
                        self.__amount_of_bricks_left += 1

                    elif item == "5":
                        brick = Brick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_BLUE), self.__game)
                        self.__bricks.append(brick)
                        self.__amount_of_bricks_left += 1

                    elif item == "S":
                        brick = SpeedBrick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_SPEED), self.__game)
                        self.__bricks.append(brick)
                        self.__amount_of_bricks_left += 1

                    elif item == "L":
                        brick = LifeBrick([x,y], pygame.image.load(GameConstants.SPRITE_BRICK_LIFE), self.__game)
                        self.__bricks.append(brick)
                        self.__amount_of_bricks_left += 1

                x += GameConstants.BRICK_SIZE[0] + GameConstants.BRICK_GAP[0]
            x = 0
            y += GameConstants.BRICK_SIZE[1] + GameConstants.BRICK_GAP[1]
