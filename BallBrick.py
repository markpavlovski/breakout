from GameConstants import *
from Brick import *

class LifeBrick(Brick):

    def __init__(self, position, sprite, game):
        super(BallBrick, self).__init__(position, sprite, game)

    def hit(self):
        self.get_game().increase_lives()
        super(BallBrick, self).hit()

    def get_hit_sound(self):
        return GameConstants.SOUND_HIT_BRICK_LIFE
