from GameConstants import *
from Brick import *

class SpeedBrick(Brick):
    def __init__(self, position, sprite, game):
        super(SpeedBrick, self).__init__(position, sprite, game)

    def hit(self):
        for ball in self.get_game().get_balls():
            ball.set_speed([1.3*ball.get_speed()[0],1.3*ball.get_speed()[0]])
        super(SpeedBrick,self).hit()

    def get_hit_sound(self):
        return GameConstants.SOUND_HIT_BRICK_SPEED
