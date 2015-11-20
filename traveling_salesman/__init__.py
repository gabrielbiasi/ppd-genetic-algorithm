import random, math
import util

NUM_BITS_IN_NUM = 3
CITIES_NUM = 2 ** NUM_BITS_IN_NUM

class TravelingSalesman:
    data = None
    best_fitness = 9999999
    count_fitness = 0
    total_count_fitness = 10

    def new_individual(self):
        if not self.data:
            self.data = []
            for num in range(CITIES_NUM):
                self.data.append({'id': num, 'x': random.randint(0, 200), 'y': random.randint(0, 200)})

        v = range(CITIES_NUM)
        random.shuffle(v)

        ind = []
        for x in v:
            ind += self.int_to_bin(x)
        return ind


    def get_fitness(self, individual):
        v = []
        for i in xrange(CITIES_NUM):
            number = int(''.join(individual[i * NUM_BITS_IN_NUM:(i + 1) * NUM_BITS_IN_NUM]), 2)
            v.append(number)

        tour_distance = 0
        for j, i in enumerate(v):
            from_city = self.data[i]
            destination_city = None
            if j + 1 < len(v):
                destination_city = self.data[j + 1]
            else:
                destination_city = self.data[v[0]]
            tour_distance += math.sqrt((math.fabs(destination_city['x'] - from_city['x'])) ** 2 + (math.fabs(destination_city['y'] - from_city['y'])) ** 2)
        return float(tour_distance)


    def int_to_bin(self, number):
        return list(bin(number)[2:].zfill(NUM_BITS_IN_NUM))


    def validate_individual(self, individual):
        v = []
        for i in xrange(CITIES_NUM):
            number = int(''.join(individual[i * NUM_BITS_IN_NUM:(i + 1) * NUM_BITS_IN_NUM]), 2)
            if number not in v:
                v.append(number)

        for i in self.data:
            if i['id'] not in v:
                v.append(i['id'])

        ind = []
        for x in v:
            ind += self.int_to_bin(x)

        return True, ind


    def num_bits(self):
        return NUM_BITS_IN_NUM * CITIES_NUM


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
        return 'caminho de deus'
