import random

from city import City
from tour import Tour
import util

NUM_BITS_IN_NUM = 7
AMOUNT_NUM = 2
NUM_CITIES = 2 ** NUM_BITS_IN_NUM

class TravelingSalesman:
    data = None
    best_fitness = 9999999
    count_fitness = 0
    total_count_fitness = 10


    def new_individual(self):
        if not self.data:
            self.data = []
            for i in xrange(NUM_CITIES):
                city = City(i)
                self.data.append(city.__dict__)

        origin = random.randint(0, NUM_CITIES - 1)
        step = random.randint(0, NUM_CITIES - 1)
        if NUM_CITIES % 2 == 0:
            while step % 2 == 0:
                step = random.randint(1, NUM_CITIES - 1)

        return list(bin(origin)[2:].zfill(NUM_BITS_IN_NUM) + bin(step)[2:].zfill(NUM_BITS_IN_NUM))

    def funcao(self, origin, step):
        a = []
        a.append(origin)
        for pos in xrange(1, NUM_CITIES):
            s = a[pos - 1] + step
            if s > NUM_CITIES:
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
        print isinstance(self.data[0], dict)
        if len(self.data) and isinstance(self.data[0], dict):
            self.set_data(list(self.data))
        v = []
        origin = int(''.join(individual[0:NUM_BITS_IN_NUM]), 2)
        step = int(''.join(individual[NUM_BITS_IN_NUM:2 * NUM_BITS_IN_NUM]), 2)
        func = self.funcao(origin, step)

        cities = []
        for i in func:
            for j in self.data:
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
        return float(tour_distance)


    def validate_individual(self, individual):
        if individual[-1] == '0':
            individual[-1] = '1'
        return True


    def num_bits(self):
        return NUM_BITS_IN_NUM * AMOUNT_NUM


    def is_finished(self, best):
        f = self.get_fitness(best)
        if f < self.best_fitness:
            self.best_fitness = f
            self.count_fitness = 0
        elif f == self.best_fitness:
            self.count_fitness += 1
            if self.count_fitness == self.total_count_fitness:
                return True
        return False


    def show(self, individual):
        origin = int(''.join(individual[0:NUM_BITS_IN_NUM]), 2)
        step = int(''.join(individual[NUM_BITS_IN_NUM:2 * NUM_BITS_IN_NUM]), 2)
        return '(%d, %d)' % (origin, step)
