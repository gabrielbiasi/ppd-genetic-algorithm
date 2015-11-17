import math
import random


class City:
    _id = None
    _x = None
    _y = None


    def __init__(self, _id, _x=None, _y=None):
        random.seed()

        self._id = _id
        self._x = _x if _x else random.random() * 200
        self._y = _y if _y else random.random() * 200


    def __str__(self):
        return '(%d, %d)' % (int(self._x), int(self._y))


    def distance_to(self, city):
        x_distance = abs(self.getX() - city.getX())
        y_distance = abs(self.getY() - city.getY())
        return math.sqrt((x_distance * x_distance) + (y_distance * y_distance))
