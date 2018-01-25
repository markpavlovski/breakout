import pygame
from Scene import *
from GameConstants import *

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

        game.screen.blit(pad.get_sprite(), pad.get_position())

        self.clear_text()
        self.add_text(
            "Your Score: {}".format(game.get_score()),
            x = 20,
            y = GameConstants.SCREEN_SIZE[1]-120,
            size = 60
        )
        self.add_text(
            "Lives: {}".format(game.get_score()),
            x = 20,
            y = GameConstants.SCREEN_SIZE[1]-60,
            size = 60
        )


    def handle_events(self, events):
        super(PlayingGameScene,self).handle_events(events)
        pressed_keys = pygame.key.get_pressed()

        pad = self.get_game().get_pad()


        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key  == pygame.K_SPACE or event.key == pygame.K_UP:
                    for ball in self.get_game().get_balls():
                        ball.set_motion(True)

        if pressed_keys[pygame.K_RIGHT]:
            pad.move_right()
        if pressed_keys[pygame.K_LEFT]:
            pad.move_left()

        if pressed_keys[pygame.K_w] & pressed_keys[pygame.K_q]:
            exit()
