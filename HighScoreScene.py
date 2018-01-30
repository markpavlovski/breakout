import pygame
import random
from Scene import *
from GameConstants import *
from HighScore import *
from Level import *
from Ball import *


class HighScoreScene(Scene):

    def __init__(self,game):
        super(HighScoreScene,self).__init__(game)
        self.__level = Level(game)
        self.__level.load_highscores()
        self.__balls = [Ball((GameConstants.SCREEN_SIZE[0]*random.random(),GameConstants.SCREEN_SIZE[1]*random.random()),pygame.image.load(GameConstants.SPRITE_BALL),game),
                        Ball((GameConstants.SCREEN_SIZE[0]*random.random(),GameConstants.SCREEN_SIZE[1]*random.random()),pygame.image.load(GameConstants.SPRITE_BALL),game)]


    def render(self):
        game = self.get_game()
        balls = self.__balls
        self.clear_text()
        high_score = HighScore()

        level = self.__level
        for brick in self.__level.get_bricks():
            if not brick.is_destroyed():
                game.screen.blit(brick.get_sprite(),brick.get_position())


        text_position = [675,197]

        for score in high_score.get_scores():
            self.add_text("{}: {}".format(score[0],score[1]),text_position[0],text_position[1], size = GameConstants.HIGHSCORE_FONT_SIZE)
            text_position[1] += GameConstants.HIGHSCORE_FONT_LINE_OFFSET
        self.add_text("RETURN TO MAIN MENU",275,700, size = 40)
        super(HighScoreScene,self).render()

        for ball in balls:
            ball.set_motion(True)
            for brick in self.__level.get_bricks():
                if not brick.is_destroyed() and ball.intersects(brick):
                    # game.play_sound(brick.get_hit_sound())
                    ball.change_direction(brick)
            for other_ball in balls:
                if ball != other_ball and ball.intersects(other_ball):
                    ball.change_direction(other_ball)

            ball.update_position()
            game.screen.blit(ball.get_sprite(),ball.get_position())



    def handle_events(self, events):
        super(HighScoreScene,self).handle_events(events)
        pressed_keys = pygame.key.get_pressed()
        game = self.get_game()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or
                event.key == pygame.K_ESCAPE or
                event.key == pygame.K_RETURN):
                    game.play_sound(GameConstants.SOUND_BREAKOUT)
                    game.reset()
                    game.change_scene(GameConstants.MENU_SCENE)

        if pressed_keys[pygame.K_w] & pressed_keys[pygame.K_q]:
            exit()
