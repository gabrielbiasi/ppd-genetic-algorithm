"""
Traveling Selesman problem
"""

from tour import Tour
from city import City
import util


def new_individual(num):
    cities = []
    for i in xrange(num):
        cities.append(City(i))
    tour = Tour()
    tour.generate_tour(cities)

    ind = []
    fill = len(bin(tour.get_biggest_id())[2:])
    for city in tour.get_tour():
        num = list(bin(city.get_id())[2:].zfill(fill))
        ind += num
    return ind


def get_fittest(li):
    to_cut = 4
    v = []

    for i in xrange(len(li) / to_cut):
        v.append(util.to_int(li[to_cut * i:to_cut * (i + 1)]))

    print v
