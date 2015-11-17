import random

class Tour:
    _distance = 0
    _fitness = 0
    _tour = []


    def generate_tour(self, cities_list):
        self._tour = list(cities_list)
        random.shuffle(self._tour)


    def get_tour(self):
        return self._tour


    def get_biggest_id(self):
        biggest = self._tour[0].get_id()
        for city in self._tour:
            if city.get_id() > biggest:
                biggest = city.get_id()

        return biggest


    def get_fitness(self):
        return self._fitness
