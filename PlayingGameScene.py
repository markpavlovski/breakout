import pygame
from Scene import *

class PlayingGameScene(Scene):

    def __init__(self,game):
        super(PlayingGameScene,self).__init__(game)

    def render(self):
        super(PlayingGameScene,self).render()

        game = self.get_game()
        balls = game.get_balls()
        pad = game.get_pad()

        for ball in game.get_balls():
            for other_ball in balls:
                if ball != other_ball and ball.intersects(other_ball):
                    ball.change_direction(other_ball)

            for brick in game.get_level().get_bricks():
                if not brick.is_destroyed() and ball.intersects(brick):
                    brick.hit()
                    ball.change_direction(brick)
                    break

            if ball.intersects(pad):
                ball.change_direction(pad)

            ball.update_position()
            game.screen.blit(ball.get_sprite(),ball.get_position())

        for brick in game.get_level().get_bricks():
            if not brick.is_destroyed():
                game.screen.blit(brick.get_sprite(),brick.get_position())


        pad.set_position((pygame.mouse.get_pos()[0], pad.get_position()[1]))
        game.screen.blit(pad.get_sprite(), pad.get_position())

    def handle_events(self, events):
        super(PlayingGameScene,self).handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
