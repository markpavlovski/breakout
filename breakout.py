import pygame

from GameConstants import *
from GameObject import *

from Scene import *
from Brick import *

from Ball import *
from Pad import *

from Level import *
from HighScore import *



class Breakout:
    def __init__(self):
        self.__lives = 5
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)

        self.__pad = Pad((0,0),0)
        self.__balls = [Ball((0,0),0,self)]

        print(GameConstants.SCREEN_SIZE)
        pass

    def start(self):
        pass

    def change_scene(self, scene):
        pass

    def get_level(self):
        pass

    def get_score(self):
        pass

    def increase_score(self,score):
        pass

    def get_lives(self):
        pass

    def get_balls(self):
        pass

    def get_pad(self):
        pass

    def play_sound(self, sound_clip):
        pass

    def reduce_lives(self):
        pass

    def increase_lives(self):
        pass

    def reset(self):
        pass

Breakout().start()
