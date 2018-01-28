import pygame
from Scene import *
from GameConstants import *
from Brick import *

class MenuScene(Scene):

    def __init__(self,game):
        super(MenuScene,self).__init__(game)

        self.add_text("START GAME", x = 663, y = 458, size = 40)
        self.add_text("HIGH SCORE", x = 663, y = 508, size = 40)
        self.add_text("QUIT", x = 663, y = 558, size = 40)

        self.__menu_sprite = pygame.image.load(GameConstants.SPRITE_MENU)
        self.__start_sound = True

        self.__brick_current_location = 0

    def render(self):
        game = self.get_game()
        self.get_game().screen.blit(self.__menu_sprite,(0,0))
        super(MenuScene,self).render()
        while self.__start_sound:
            self.get_game().play_sound(GameConstants.SOUND_BREAKOUT)
            self.__start_sound = False

        start_x = 586
        start_y = 468
        linebreak = 50
        brick_locations = [(start_x,start_y),(start_x,start_y + linebreak),(start_x,start_y+2*linebreak)]
        brick = Brick(brick_locations[self.__brick_current_location], pygame.image.load(GameConstants.SPRITE_BRICK_RED), game)
        game.screen.blit(Brick.get_sprite(brick),brick.get_position())




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
                if event.key == pygame.K_SPACE:
                    if self.__brick_current_location == 0:
                        self.get_game().play_sound(GameConstants.SOUND_NEW_GAME)
                        self.get_game().change_scene(GameConstants.PLAYING_SCENE)
                    elif self.__brick_current_location == 1:
                        self.get_game().play_sound(GameConstants.SOUND_HIGH_SCORES)
                        self.get_game().change_scene(GameConstants.HIGHSCORE_SCENE)
                    elif self.__brick_current_location == 2:
                        exit()

                if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                    self.get_game().play_sound(GameConstants.SOUND_MENU)
                    self.__brick_current_location += 1
                    self.__brick_current_location %= 3
                if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                    self.get_game().play_sound(GameConstants.SOUND_MENU)
                    self.__brick_current_location -= 1
                    self.__brick_current_location %= 3
