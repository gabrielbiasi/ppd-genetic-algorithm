"""
Core Algorithm
"""

import conf, util, random
import schwefel

def run(problem):

    ### MASTER ###

    # Setting the size of population
    # To dedide what we will use
    population_size = (problem.NUM_BITS ** 2) / 2

    pop = util.new_population(problem)

    models = []
    last_generated = pop[0]
    models.append(util.create_model(last_generated, conf.ALPHA))

    for x in xrange(1, population_size):
        if util.similarity_of_individuals(pop[x], last_generated) <= 0.25:
            models.append(util.create_model(last_generated, conf.ALPHA))
            last_generated = pop[x]

    #### SLAVE ###

    population_size = (problem.NUM_BITS ** 2) / 2

    # Generating the new population for each probabilist model #

    populations = []
    for i in xrange(len(models)):
        pop = []
        for x in xrange(population_size):
            pop.append(problem.new_individual())
        populations.append(pop)


    # The magic #
    for model_id in xrange(len(models)):
        for model_item_id in xrange(len(models[model_id])):
            for bit_id in xrange(len(populations[model_id][model_item_id])):
                condition = random.random() < models[model_id][model_item_id]
                populations[model_id][model_item_id][bit_id] = '1' if condition else '0'


    # Calculate the best individual of each probabilist model #
    bests = []
    for model_id in xrange(len(models)):
        bests[model_id] = populations[model_id][0]
        for model_item_id in xrange(1, len(models[model_id])):
            if problem.get_fitness(bests[model_id]) > problem.get_fitness(populations[model_id][model_item_id]):
                bests[model_id] = populations[model_id][model_item_id]


    # Calculate the bestest #
    b = bests[0]
    for best in bests[1:]:
        if problem.get_fitness(b) > problem.get_fitness(best):
            b = best


    # B is the best #


if __name__ == '__main__':
    print 'INIT'
    run(schwefel)
    print 'END'