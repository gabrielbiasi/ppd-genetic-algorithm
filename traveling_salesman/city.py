import math
import random


class City:
    _id = None
    _x = None
    _y = None

    def __init__(self, id, x=None, y=None):
        random.seed()
        self._id = id
        self._x = x
        self._y = y
        if not x:
            self._x = random.random() * 200
        if not y:
            self._y = random.random() * 200


    def __str__(self):
        return '(%d, %d)' % (int(self._x), int(self._y))


    def get_id(self):
        return self._id


    def get_x(self):
        return self._x


    def get_y(self):
        return self._y


    def distance_to(self, city):
        x_distance = abs(self.getX() - city.getX())
        y_distance = abs(self.getY() - city.getY())
        return math.sqrt((x_distance * x_distance) + (y_distance * y_distance))
