import math, random, util


class RadioNetwork():
    """ToDo"""
    limit_area = 2048
    num_bits = 11
    fitness = 0.2 # 80% ?
    covered_area = 0.8 # 80%
    covered_bs = 5
    amount_bs = math.ceil(((limit_area**2) * covered_area) / (math.pi * (covered_bs**2)))

    def new_individual(self):
        """Generats a new individual for population"""
        while True:
            individual = []
            for x in xrange(self.amount_bs * self.num_bits * 2):
                individual.append(str(random.randint(0,1)))
            var1, var2 = self.validate_individual(ind)
            if var1:
                break
        return individual


    def get_fitness(self, individual):
        """Checks how close to this result"""
        v = []
        for i in xrange(self.amount_bs * 2):
            number = int(''.join(individual[i*self.num_bits:(i+1)*self.num_bits]), 2)
            v.append(number - self.limit_area/2)

        area_intersection = 0.0
        area_coverage = self.amount_bs * (math.pi * (self.covered_bs**2))

        for i in xrange(self.amount_bs):
            for j in xrange(self.amount_bs):
                if i < j:
                    d = math.sqrt(((v[j*2] - v[i*2])**2) + ((v[j*2+1] - v[i*2+1])**2))

                    part1 = self.covered_bs*self.covered_bs*math.acos((d*d + self.covered_bs*self.covered_bs - self.covered_bs*self.covered_bs)/(2*d*self.covered_bs))
                    part2 = self.covered_bs*self.covered_bs*math.acos((d*d + self.covered_bs*self.covered_bs - self.covered_bs*self.covered_bs)/(2*d*self.covered_bs))
                    part3 = 0.5*math.sqrt((-d+self.covered_bs+self.covered_bs)*(d+self.covered_bs-self.covered_bs)*(d-self.covered_bs+self.covered_bs)*(d+self.covered_bs+self.covered_bs))
                    area_intersection += (part1 + part2 + part3)
                    """
                    part1 = self.covered_bs*self.covered_bs*math.acos((d*d)/(2*d*self.covered_bs))
                    part2 = self.covered_bs*self.covered_bs*math.acos((d*d)/(2*d*self.covered_bs))
                    part3 = 0.5*math.sqrt((-d+self.covered_bs+self.covered_bs)*(d)*(d)*(d+self.covered_bs+self.covered_bs))
                    area_intersection += (part1 + part2 + part3)

                    """
        area_coverage = area_coverage - area_intersection
        return (1.0 - (area_coverage/(self.limit_area**2)))




    def is_finished(self, individual):
        """ToDO"""
        f = self.get_fitness()
        return f <= math.fabs(self.fitness)

    def validate_individual(self, individual):
        """Validation of an individual to find out if it is part of the domain"""
        for i in xrange(self.amount_bs * 2):
            number = int(''.join(individual[i*self.num_bits:(i+1)*self.num_bits]), 2)
            if math.fabs(number) > self.limit_area - covered_bs or math.fabs(number) < covered_bs: #Limita para dentro da area
                return False, individual
        return True, individual


    def show(self, individual):
        string = "[ "
        for i in xrange(self.amount_bs * 2):
            number = int(''.join(individual[i*self.num_bits:(i+1)*self.num_bits]), 2)
            string += str(number - self.limit_area/2)
            string += ", " if i+1 < AMOUNT_NUM else " "

        return string+"]"
