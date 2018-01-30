from GameConstants import *
from Brick import *
from Ball import *

class BallBrick(Brick):

    def __init__(self, position, sprite, game):
        super(BallBrick, self).__init__(position, sprite, game)

    def hit(self):
        game = self.get_game()
        super(BallBrick, self).hit()
        ball = Ball((GameConstants.SCREEN_SIZE[0]/2,GameConstants.SCREEN_SIZE[1]*2/3),pygame.image.load(GameConstants.SPRITE_BALL),game)
        game.add_a_ball(ball)
        ball.set_motion(True)


    def get_hit_sound(self):
        return GameConstants.SOUND_HIT_BRICK_BALL
