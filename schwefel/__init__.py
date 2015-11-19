import math, random, util
"""
Schwefel's function
This file have anything about we need to test the schwefel's function.
"""

LIMIT_VALUE = 1000
NUM_BITS_IN_NUM = 10
AMOUNT_NUM = 3

class Schwefel():
    data = None
    FITNESS = 0.1
    def new_individual(self):
        ind = []
        loop = False
        while not loop:
            ind = []
            for x in xrange(NUM_BITS_IN_NUM*AMOUNT_NUM):
                ind.append(str(random.randint(0,1)))
            loop = self.validate_individual(ind)
        return ind

    def get_fitness(self, individual):
        v = []
        for i in xrange(AMOUNT_NUM):
            number = int(''.join(individual[i*NUM_BITS_IN_NUM:(i+1)*NUM_BITS_IN_NUM]), 2)
            v.append(number - 500)

        alpha = 418.982887
        fitness = 0.0
        for i in range(AMOUNT_NUM):
            fitness += v[i]*math.sin(math.sqrt(math.fabs(v[i])))
        return alpha*AMOUNT_NUM - float(fitness)


    def is_finished(self, individual):
        f = self.get_fitness(individual)
        return f <= self.FITNESS and f >= -self.FITNESS


    def validate_individual(self, individual):
        '''
        validation of an individual to find out if it is part of the domain
        '''
        for i in xrange(AMOUNT_NUM):
            number = int(''.join(individual[i*NUM_BITS_IN_NUM:(i+1)*NUM_BITS_IN_NUM]), 2)
            if number > LIMIT_VALUE:
                return False
        return True

    def num_bits(self):
        return NUM_BITS_IN_NUM * AMOUNT_NUM


    def show(self, individual):
        string = "[ "
        for i in xrange(AMOUNT_NUM):
            number = int(''.join(individual[i*NUM_BITS_IN_NUM:(i+1)*NUM_BITS_IN_NUM]), 2)
            string += str(number - 500)
            string += ", " if i+1 < AMOUNT_NUM else " "

        return string+"]"
