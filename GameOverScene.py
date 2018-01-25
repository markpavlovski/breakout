import pygame
from Scene import *

class GameOverScene(Scene):

    def __init__(self,game):
        super(GameOverScene,self).__init__(game)

    def handle_events(self, events):
        super(GameOverScene,self).handle_events(events)
        pressed_keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key  == pygame.K_SPACE or event.key == pygame.K_UP:
                    for ball in self.get_game().get_balls():
                        ball.set_motion(True)

        if pressed_keys[pygame.K_w] & pressed_keys[pygame.K_q]:
            exit()
