class Population:
    _tours = []


    def generate_population(self, population_size):
        for i in xrange(population_size):
            new_tour = Tour()
            self.save_individual(i, new_tour)


    def set_tour(self, index, tour):
        self._tours[index] = tour


    def get_tour(self, index):
        return self._tours[index]


    def get_fittest(self):
        fittest = self._tours[0]
        for i in xrange(self.population_size()):
            if fittest.get_fitness() < self.get_tour(i).get_fitness():
                fittest = self.get_tour(i)

        return fittest.get_fitness()


    def population_size(self):
        return len(self._tours)
