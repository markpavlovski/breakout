import pygame
from Scene import *
from GameConstants import *
from HighScore import *

class HighScoreScene(Scene):

    def __init__(self,game):
        super(HighScoreScene,self).__init__(game)
        self.__highscore_sprite = pygame.image.load(GameConstants.SPRITE_HIGHSCORE)

    def render(self):
        game = self.get_game()
        game.screen.blit(self.__highscore_sprite,(50,50))
        self.clear_text()
        high_score = HighScore()


        text_width = 200
        text_position = [GameConstants.SCREEN_SIZE[0]/2-text_width/2,GameConstants.SCREEN_SIZE[1]*.35]

        for score in high_score.get_scores():
            self.add_text("{}: {}".format(score[0],score[1]),text_position[0],text_position[1], size = GameConstants.HIGHSCORE_FONT_SIZE)
            text_position[1] += GameConstants.HIGHSCORE_FONT_LINE_OFFSET
        self.add_text("RETURN TO MAIN MENU",300,text_position[1] + 150, size = GameConstants.HIGHSCORE_FONT_SIZE)
        super(HighScoreScene,self).render()

    def handle_events(self, events):
        super(HighScoreScene,self).handle_events(events)
        pressed_keys = pygame.key.get_pressed()
        game = self.get_game()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.play_sound(GameConstants.SOUND_BREAKOUT)
                    game.reset()
                    game.change_scene(GameConstants.MENU_SCENE)

        if pressed_keys[pygame.K_w] & pressed_keys[pygame.K_q]:
            exit()
