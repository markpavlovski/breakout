from Brick import *

class SpeedBrick(Brick):
    def __init__(self, position, sprite, game):
        super(SpeedBrick, self).__init__(position, sprite, game)

    def hit(self):
        for ball in self.get_game().get_balls():
            ball.set_speed(2*ball.get_speed())
        super(SpeedBrick,self).hit()
