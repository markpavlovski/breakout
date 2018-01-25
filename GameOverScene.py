import pygame
from Scene import *
from GameConstants import *
from HighScore import *

class GameOverScene(Scene):

    def __init__(self,game):
        super(GameOverScene,self).__init__(game)

        self.__player_name = ""
        self.__highscore_sprite = pygame.image.load(GameConstants.SPRITE_HIGHSCORE)

    def render(self):
        game = self.get_game()
        game.screen.blit(self.__highscore_sprite,(50,50))

        self.clear_text()
        self.add_text("Your Name: {}".format(self.__player_name),400,400, size = 30)
        super(GameOverScene,self).render()

    def handle_events(self, events):
        super(GameOverScene,self).handle_events(events)
        pressed_keys = pygame.key.get_pressed()
        game = self.get_game()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.reset()
                    game.change_scene(GameConstants.PLAYING_SCENE)
                if event.key == pygame.K_RETURN:
                    HighScore().add(self.__player_name,game.get_score())
                    game.reset()
                    game.change_scene(GameConstants.HIGHSCORE_SCENE)
                elif event.key >= 65 and event.key <= 122:
                    self.__player_name += chr(event.key).upper()

        if pressed_keys[pygame.K_w] & pressed_keys[pygame.K_q]:
            exit()
