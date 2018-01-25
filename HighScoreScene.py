import pygame
from Scene import *

class HighScoreScene(Scene):

    def __init__(self,game):
        super(HighScoreScene,self).__init__(game)


    def handle_events(self, events):
        super(HighScoreScene,self).handle_events(events)
        pressed_keys = pygame.key.get_pressed()
        game = self.get_game()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if pressed_keys[pygame.K_w] & pressed_keys[pygame.K_q]:
            exit()
