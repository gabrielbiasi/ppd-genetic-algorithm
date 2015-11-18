import random

from city import City
from tour import Tour
import util

NUM_BITS_IN_NUM = 10
AMOUNT_NUM = len(bin(NUM_BITS_IN_NUM)[2:])
NUM_CITIES = 100

class TravelingSalesman:
    data = None
    best_fitness = 1000
    count_fitness = 0


    def new_individual(self):
        cities_list = []
        if not self.data:
            self.data = []
            for i in xrange(NUM_CITIES):
                city = City(i)
                cities_list.append(City(city))
                self.data.append(city.__dict__)

        origin = random.randint(0, NUM_BITS_IN_NUM - 1)
        step = random.randint(0, NUM_BITS_IN_NUM - 1)
        if NUM_BITS_IN_NUM % 2 == 0:
            while step % 2 == 0:
                step = random.randint(0, NUM_BITS_IN_NUM - 1)
        cities_list = self.funcao(origin, step)
        tour = Tour()
        tour.set_tour(cities_list)
        return list(bin(origin)[2:].zfill(10)) + list(bin(step)[2:].zfill(10))

    def funcao(self, origin, step):
        a = []
        a.append(origin)
        for pos in xrange(NUM_CITIES):
            s = a[pos] + step
            if s >= NUM_CITIES:
                s -= NUM_CITIES
            a.append(s)
        return a


    def set_data(self, data):
        self.data = []
        for i in data:
            self.data.append(City(**i))


    def get_data(self):
        return self.data


    def get_fitness(self, individual):
        v = []
        for i in xrange(2):
            v.append(int(''.join(individual[i * NUM_BITS_IN_NUM:(i + 1) * NUM_BITS_IN_NUM]), 2))

        print v
        a = self.funcao(v[0], v[1])

        cities = []
        for i in a:
            for j in self.data:
                # print j._id, i
                if j._id == i:
                    cities.append(j)
        tour_distance = 0
        for i, from_city in enumerate(cities):
            destination_city = None
            if i + 1 < len(cities):
                destination_city = cities[i + 1]
            else:
                destination_city = cities[0]
            tour_distance += from_city.distance_to(destination_city)
        return 1 / float(tour_distance)


    def distance_to(self, city):
        x_distance = abs(self.getX() - city.getX())
        y_distance = abs(self.getY() - city.getY())
        return math.sqrt((x_distance * x_distance) + (y_distance * y_distance))


    def validate_individual(self, item):
        return True


    def num_bits(self):
        return NUM_BITS_IN_NUM * AMOUNT_NUM


    def is_finished(self, best):
        return False


    def show(self, b):
        return 'blastoise'
