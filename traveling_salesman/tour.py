import random

class Tour:
    _alpha = 0.05
    _distance = 0
    _fitness = 0
    _tour = []


    def generate_tour(self, cities_list):
        self._tour = cities_list
        random.shuffle(self._tour)


    def get_tour(self):
        return self._tour


    def get_biggest_id(self):
        biggest = self._tour[0].id
        for city in self._tour:
            if city.id > biggest:
                biggest = city.id

        return biggest


    def get_fitness(self):
        return self._fitness
