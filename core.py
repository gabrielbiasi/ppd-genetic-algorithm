"""
Core Algorithm
"""

import conf, util
import schwefel

def run(problem):

    # Setting the size of population
    # To dedide what we will use
    population_size = (problem.NUM_BITS ** 2) / 2

    # Create the first population, to create the probabilist models
    pop = []
    for x in xrange(population_size):
        pop.append(problem.new_individual())

    models = []
    last_generated = pop[0]
    for x in xrange(1, population_size):
        if util.similarity_of_individuals(pop[x], last_generated) <= 0.25:
            pass



if __name__ == '__main__':
    print 'INIT'
    run(schwefel)
    print 'END'