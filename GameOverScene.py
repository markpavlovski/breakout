import pygame
from Scene import *
from GameConstants import *

class GameOverScene(Scene):

    def __init__(self,game):
        super(GameOverScene,self).__init__(game)

    def render(self):
        super(GameOverScene,self).render()
        self.clear_text()
        self.add_text("Press SPACE to restart the game",400,400, size = 30)

    def handle_events(self, events):
        super(GameOverScene,self).handle_events(events)
        pressed_keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.get_game().reset()
                    self.get_game().change_scene(GameConstants.PLAYING_SCENE)

        if pressed_keys[pygame.K_w] & pressed_keys[pygame.K_q]:
            exit()
