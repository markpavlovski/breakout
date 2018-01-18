import pygame

from GameConstants import *
from GameObject import *

from Scene import *
from Brick import *

from Ball import *
from Pad import *

from Level import *
from HighScore import *

from PlayingGameScene import *
from GameOverScene import *
from HighScoreScene import *
from MenuScene import *

class Breakout:
    def __init__(self):
        self.__lives = 5
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)

        self.__pad = Pad((0,0),0)
        self.__balls = [Ball((0,0),0,self)]

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Breakout!")

        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32) #pygame.DOUBLEBUF | pygame.FULLSCREEN for full screen
        pygame.mouse.set_visible(False)

        self.__scenes = [
            PlayingGameScene(self),
            GameOverScene(self),
            HighScoreScene(self),
            MenuScene(self)
            ]

        self.__current_scene = 0
        self.__sounds = ()

        print(GameConstants.SCREEN_SIZE)
        pass


    def start(self):
        while True:
            self.__clock.tick(GameConstants.FPS)
            self.__screen.fill((0,0,0))
            current_scene = self.__scenes[self.__current_scene]
            current_scene.handle_events(pygame.event.get())
            current_scene.render()

            pygame.display.update()

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
