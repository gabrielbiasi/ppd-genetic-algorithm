from math, random, util


class RadioNetwork():
    """ToDo"""
    limit_area = 2048
    num_bits = 11
    data = None
    fitness = 0
    covered_area = 0.8
    covered_bs = 5
    amount_bs = math.ceil(((limit_area**2) * covered_area) / (math.pi * (covered_bs**2)))

    def new_individual(self):
        """Generats a new individual for population"""
        while True:
            individual = []
            for x in xrange(amount_bs * num_bits * 2):
                individual.append(str(random.randint(0,1)))
            if self.validate_individual(ind):
                break
        return individual


    def get_fitness(self, individual):
        """Checks how close to this result"""

    def is_finished(self, individual):
        """ToDO"""
        f = sel.get_fitness()
        return f <= math.fabs(self.fitness)

    def validate_individual(self, individual):
        """Validation of an individual to find out if it is part of the domain"""
        for i in xrange(amount_bs * 2):
            number = int(''.join(individual[i*num_bits:(i+1)*num_bits]), 2)
            if math.fabs(number) > limit_area:
                return False
        return True


    def show(self, individual):
        print "GG"

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
        