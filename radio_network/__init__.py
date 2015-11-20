import math, random, util


class RadioNetwork():# (x,y)(x,y)
    """ToDo"""
    NUM_BITS = 5 # 11
    limit_area = 2 ** NUM_BITS # 2048
    fitness = 0.2 # 80% ?
    covered_area = 0.8 # 80%
    covered_bs = 2
    amount_bs = int(math.ceil(((limit_area**2) * covered_area) / (math.pi * (covered_bs**2))))

    def num_bits(self):
        return int(self.amount_bs * self.NUM_BITS * 2)

    def new_individual(self):
        """Generats a new individual for population"""
        while True:
            individual = []
            for x in xrange(self.amount_bs * self.NUM_BITS * 2):
                individual.append(str(random.randint(0,1)))
            var1, var2 = self.validate_individual(individual)
            if var1:
                break
        return individual


    def get_fitness(self, individual):
        """Checks how close to this result"""
        v = []
        for i in xrange(self.amount_bs * 2):
            number = int(''.join(individual[i*self.NUM_BITS:(i+1)*self.NUM_BITS]), 2)
            v.append(number - self.limit_area/2)

        area_intersection = 0.0
        area_coverage = self.amount_bs * (math.pi * (self.covered_bs**2))

        for i in xrange(self.amount_bs):
            for j in xrange(self.amount_bs):
                if i < j:
                    d = math.sqrt(((v[j*2] - v[i*2])**2) + ((v[j*2+1] - v[i*2+1])**2))
                    d = math.fabs(d)##
                    if d < self.covered_bs*2:##
                        if d > 0:
                            
                            part1 = self.covered_bs*self.covered_bs*math.acos((d*d + self.covered_bs*self.covered_bs - self.covered_bs*self.covered_bs)/(2*d*self.covered_bs))
                            part2 = self.covered_bs*self.covered_bs*math.acos((d*d + self.covered_bs*self.covered_bs - self.covered_bs*self.covered_bs)/(2*d*self.covered_bs))
                            part3 = 0.5*math.sqrt((-d+self.covered_bs+self.covered_bs)*(d+self.covered_bs-self.covered_bs)*(d-self.covered_bs+self.covered_bs)*(d+self.covered_bs+self.covered_bs))
                            area_intersection += (part1 + part2 + part3)

                        else:
                            area_intersection += math.pi * (self.covered_bs ** 2)
                        """
                        part1 = self.covered_bs*self.covered_bs*math.acos((d*d)/(2*d*self.covered_bs))
                        part2 = self.covered_bs*self.covered_bs*math.acos((d*d)/(2*d*self.covered_bs))
                        part3 = 0.5*math.sqrt((-d+self.covered_bs+self.covered_bs)*(d)*(d)*(d+self.covered_bs+self.covered_bs))
                        area_intersection += (part1 + part2 + part3)

                        A = ((2*(self.covered_bs**2)) * (math.acos(d/(2*self.covered_bs))) - (0.5*d) * (math.sqrt((4*(self.covered_bs**2)) - (d**2))))
                        area_intersection += A

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
            number = int(''.join(individual[i*self.NUM_BITS:(i+1)*self.NUM_BITS]), 2)
            if math.fabs(number) > self.limit_area - self.covered_bs or math.fabs(number) < self.covered_bs: #Limita para dentro da area
                return False, individual
        return True, individual


    def show(self, individual):
        string = "[ "
        for i in xrange(self.amount_bs * 2):
            number = int(''.join(individual[i*self.NUM_BITS:(i+1)*self.NUM_BITS]), 2)
            string += str(number - self.limit_area/2)
            string += ", " if i+1 < AMOUNT_NUM else " "

        return string+"]"
