"""
Core Algorithm
"""

import conf, util, random, math
import schwefel

def run(problem):

    ### MASTER ###

    # Setting the size of population
    # To dedide what we will use
    population_size = (problem.NUM_BITS ** 2) / 2

    pop = util.new_population(problem)

    print problem.get_fitness(pop[0])

    models = []
    last_generated = pop[0]
    models.append(util.create_model(last_generated))

    for x in xrange(1, population_size):
        if util.similarity_of_individuals(pop[x], last_generated) <= 0.25:
            models.append(util.create_model(last_generated))
            last_generated = pop[x]

    aux = []
    for x in models:
        aux.append(list(x))

    #### SLAVE ###

    population_size = (problem.NUM_BITS ** 2) / 2
    print population_size
    print len(models)

    # Generating the new population for each probabilist model #
    oi = 1
    while True:
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
        bests = [None] * len(models)
        for model_id in xrange(len(models)):
            bests[model_id] = populations[model_id][0]
            for model_item_id in xrange(1, len(models[model_id])):
                if math.fabs(problem.get_fitness(bests[model_id])) > math.fabs(problem.get_fitness(populations[model_id][model_item_id])):
                    bests[model_id] = populations[model_id][model_item_id]


        # Calculate the bestest #
        b = bests[0]
        for best in bests:
            print best
            print problem.get_fitness(best)
            if math.fabs(problem.get_fitness(b)) > math.fabs(problem.get_fitness(best)):
                b = best

        # B is the best #
        if problem.is_finished(b):
            print 'FINISHED'
            print problem.get_fitness(b)
            v = []
            v.append(util.to_int(b[:10]))
            v.append(util.to_int(b[10:20]))
            v.append(util.to_int(b[20:30]))
            print v
            return

        # Calculate the new probabilist models #
        for model in models:
            util.update_model(model, b)

        # Mutate each probabilist model #
        for model in models:
            util.mutate_model(model)

        print 'melhor: ', problem.get_fitness(b)
        oi += 1


    for x in xrange(len(models)):
        print '>>', x, '<<'
        for y in xrange(len(models[x])):
            print aux[x][y], " -> ", models[x][y]

if __name__ == '__main__':
    print 'INIT'
    run(schwefel)
    print 'END'