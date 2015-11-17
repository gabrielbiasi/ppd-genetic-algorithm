import random

from city import City
from tour import Tour


NUM_BITS_IN_NUM = 10
AMOUNT_NUM = len(bin(NUM_BITS_IN_NUM)[2:])

class TravelingSalesman:
    data = None

    def new_individual(self):
        cities_list = []
        if self.data:
            for city in self.data:
                cities_list.append(City(**city))
        else:
            for i in xrange(NUM_BITS_IN_NUM):
                cities_list.append(City(i))

        tour = Tour()
        tour.set_tour(cities_list)
        origin = random.randint(0, NUM_BITS_IN_NUM)
        step = random.randint(0, NUM_BITS_IN_NUM)
        if NUM_BITS_IN_NUM % 2:
            while not step % 2:
                step = random.randint(0, NUM_BITS_IN_NUM)

        self.data = tour.get_tour()
        return tour.get_binary_tour(origin, step)


    def set_data(self, data):
        self.data = data


    def get_data(self):
        return data


    def get_fitness(self, individual):
        #TODO: converter individual de binario para IDs
        return 1
        # tour = []
        # if self._distance == 0:
        #     tour_distance = 0
        #     for i in xrange(len(self._tour)):
        #         from_city = self.get_city(i)
        #         destination_city = None
        #         if i + 1 < self.tour_size():
        #             destination_city = self.get_city(i + 1)
        #         else:
        #             destination_city = self.get_city(0)
        #         tour_distance += from_city.distance_to(destination_city)
        #     self._distance = tour_distance
        # return self._distance



    def validate_individual(self):
        return True


    def num_bits(self):
        return NUM_BITS_IN_NUM * AMOUNT_NUM


    def is_finished(self, best):
        return False


    def show(self):
        return 'blastoise'
