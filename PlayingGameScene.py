import pygame
from Scene import *

class PlayingGameScene(Scene):

    def __init__(self,game):
        super(PlayingGameScene,self).__init__(game)

    def render(self):
        super(PlayingGameScene,self).render()
        game = self.get_game()
        for ball in game.get_balls():
            ball.update_position()
            game.screen.blit(ball.get_sprite(),ball.get_position())
        for brick in game.get_level().get_bricks():
            game.screen.blit(brick.get_sprite(),brick.get_position())

    def handle_events(self, events):
        super(PlayingGameScene,self).handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
