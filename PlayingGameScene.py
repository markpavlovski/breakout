import pygame
from Scene import *
from GameConstants import *

class PlayingGameScene(Scene):

    def __init__(self,game):
        super(PlayingGameScene,self).__init__(game)

    def render(self):
        super(PlayingGameScene,self).render()

        game = self.get_game()
        level = game.get_level()
        balls = game.get_balls()
        pad = game.get_pad()

        if level.get_amount_of_bricks_left() <= 0:
            for ball in balls:
                ball.set_motion(False)
            game.play_sound(GameConstants.SOUND_NEXT_LEVEL)
            level.load_next_level()



        if game.get_lives() <= 0:
            game.play_sound(GameConstants.SOUND_GAME_OVER)
            game.change_scene(GameConstants.GAMEOVER_SCENE)



        for ball in game.get_balls():
            for other_ball in balls:
                if ball != other_ball and ball.intersects(other_ball):
                    ball.change_direction(other_ball)

            for brick in game.get_level().get_bricks():
                if not brick.is_destroyed() and ball.intersects(brick):
                    game.play_sound(brick.get_hit_sound())
                    brick.hit()
                    level.brick_hit()
                    game.increase_score(brick.get_hit_points())
                    ball.change_direction(brick)
                    break

            if ball.intersects(pad):
                game.play_sound(GameConstants.SOUND_HIT_PAD)
                ball.change_direction(pad)

            ball.update_position()

            if ball.is_ball_dead():
                ball.set_motion(False)
                game.reduce_lives()
                if game.get_lives() > 0:
                    game.play_sound(GameConstants.SOUND_YOU_DIE)




            game.screen.blit(ball.get_sprite(),ball.get_position())

        for brick in game.get_level().get_bricks():
            if not brick.is_destroyed():
                game.screen.blit(brick.get_sprite(),brick.get_position())

        game.screen.blit(pad.get_sprite(), pad.get_position())

        self.clear_text()
        self.add_text(
            "SCORE: {}".format(game.get_score()),
            x = 20,
            y = 25,
            size = 30
        )
        self.add_text(
            "LIVES: {}".format(game.get_lives()),
            x = 20,
            y = 65,
            size = 30
        )


    def handle_events(self, events):
        super(PlayingGameScene,self).handle_events(events)
        pressed_keys = pygame.key.get_pressed()

        game = self.get_game()
        pad = self.get_game().get_pad()


        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key  == pygame.K_SPACE or event.key == pygame.K_UP:
                    for ball in self.get_game().get_balls():
                        ball.set_motion(True)

        if pressed_keys[pygame.K_RIGHT]:
            pad.move_right()
        if pressed_keys[pygame.K_LEFT]:
            pad.move_left()

        if pressed_keys[pygame.K_w] & pressed_keys[pygame.K_q]:
            exit()
