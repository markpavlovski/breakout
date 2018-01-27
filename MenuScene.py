import pygame
from Scene import *
from GameConstants import *

class MenuScene(Scene):

    def __init__(self,game):
        super(MenuScene,self).__init__(game)

        self.add_text("1 - Start Game", x = 400, y = 300, size = 50)
        self.add_text("2 - High Score", x = 400, y = 350, size = 50)
        self.add_text("3 - Quit", x = 400, y = 400, size = 50)

        self.__menu_sprite = pygame.image.load(GameConstants.SPRITE_MENU)
        self.__start_sound = True

    def render(self):
        self.get_game().screen.blit(self.__menu_sprite,(50,50))
        super(MenuScene,self).render()
        while self.__start_sound:
            self.get_game().play_sound(GameConstants.SOUND_BREAKOUT)
            self.__start_sound = False


    def handle_events(self, events):
        super(MenuScene,self).handle_events(events)
        pressed_keys = pygame.key.get_pressed()

        pad = self.get_game().get_pad()


        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key  == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_1:
                    self.get_game().play_sound(GameConstants.SOUND_NEW_GAME)
                    self.get_game().change_scene(GameConstants.PLAYING_SCENE)
                if event.key == pygame.K_2:
                    self.get_game().play_sound(GameConstants.SOUND_HIGH_SCORES)
                    self.get_game().change_scene(GameConstants.HIGHSCORE_SCENE)
                if event.key == pygame.K_3:
                    exit()
