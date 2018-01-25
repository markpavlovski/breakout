from Brick import *

class LifeBrick(Brick):

    def __init__(self, position, sprite, game):
        super(LifeBrick, self).__init__(position, sprite, game)

    def hit(self):
        self.get_game().increase_lives()
        super(LifeBrick, self).hit()
