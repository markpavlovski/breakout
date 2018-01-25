import pygame
from GameConstants import *
from GameObject import *

class Ball(GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = GameConstants.BALL_SPEED
        self.__increment = GameConstants.MOVEMENT_INCREMENT
        self.__direction = [1,-1]
        self.__in_motion = False

        super(Ball,self).__init__(position, GameConstants.BALL_SIZE, sprite)

    def set_speed(self,new_speed):
        self.__speed = new_speed

    def reset_speed(self):
        self.set_speed(GameConstants.BALL_SPEED)

    def get_speed(self):
        return self.__speed

    def is_in_motion(self):
        return self.__in_motion

    def set_motion(self, is_moving):
        self.__in_motion = is_moving
        self.reset_speed()

    def change_direction(self, game_object):
        position = self.get_position()
        size = self.get_size()
        object_position = game_object.get_position()
        object_size = game_object.get_size()

        # ball hits object below:
        if \
        position[1] > object_position[1] and \
        position[1] < object_position[1] + object_size[1] and \
        position[0] > object_position[0] and \
        position[0] < object_position[0] + object_size[0]:
            self.set_position((position[0], object_position[1]+object_size[1]))
            self.__direction[1] *= -1


        # ball hits object from above:
        elif \
        position[1] + size[1] > object_position[1] and \
        position[1] + size[1] < object_position[1] + object_size[1] and\
        position[0] > object_position[0] and \
        position[0] < object_position[0] + object_size[0]:
            self.set_position((position[0],object_position[1]-size[1]))
            self.__direction[1] *= -1

        # ball hits object from left:
        elif \
        position[0] + size[0] > object_position[0] and\
        position[0] + size[0] < object_position[0] + object_size[0]:
            self.set_position((object_position[0]-size[0],position[1]))
            self.__direction[0] *= -1

        else:
            self.set_position((object_position[0]+size[0],position[1]))
            self.__direction[0] *= -1
            self.__direction[1] *= -1


    def update_position(self):

        if not self.is_in_motion():
            pad_position = self.__game.get_pad().get_position()
            self.set_position((pad_position[0]+GameConstants.PAD_SIZE[0]/2-GameConstants.BALL_SIZE[0]/2,
                                pad_position[1]-GameConstants.BALL_SIZE[1]))
            return

        position = self.get_position()
        size = self.get_size()
        new_position = (position[0] + (self.__increment*self.__speed)*self.__direction[0],
                        position[1] + (self.__increment*self.__speed)*self.__direction[1])

        # Bounce off right wall:
        if new_position[0] + size[0] >= GameConstants.SCREEN_SIZE[0]:
            new_position = (GameConstants.SCREEN_SIZE[0]- size[0], new_position[1])
            self.__direction[0] *= -1
        # Bounce off left wall:
        if new_position[0] <= 0:
            new_position = (0,new_position[1])
            self.__direction[0] *= -1
        # Bounce off top wall:
        if new_position[1] <= 0:
            new_position = (new_position[0], 0)
            self.__direction[1] *= -1
        # Bounce off bottom wall:
        if new_position[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            new_position = (new_position[0], GameConstants.SCREEN_SIZE[1]-size[1])
            self.__direction[1] *= -1

        self.set_position(new_position)


    def is_ball_dead(self):
        pass
