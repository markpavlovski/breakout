from GameConstants import *
from GameObject import *

class Ball(GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = 3
        self.__increment = (2,2)
        self.__direction = (1,1)
        self.__in_motion = False

        super(Ball,self).__init__(position, GameConstants.BALL_SIZE, sprite)

    def set_speed(self,new_speed):
        self.__speed = new_speed

    def reset_speed(self):
        self.set_speed(3)

    def get_speed(self):
        return self.__speed

    def is_in_motion(self):
        return self.__in_motion

    def set_motion(self, is_moving):
        self.__in_motion = is_moving
        self.reset_speed()

    def change_direction(self, game_object):
        pass

    def update_position(self):
        pass

    def is_ball_dead(self):
        pass
