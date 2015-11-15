"""
Core Algorithm
"""

import conf, util, random, math
import schwefel
import rastrigin

def run(problem):

    ### MASTER ###

    pop = util.new_population(problem)
    population_size = len(pop)

    models = []
    last_generated = pop[0]

    aux = []
    for i in pop:
        aux.append(math.fabs(problem.get_fitness(i)))
    aux = sorted(aux)
    med = sum(aux[:(len(aux) / 2)]) / (len(aux) / 2)

    models.append(util.create_model(last_generated, med))

    for x in xrange(1, population_size):
        if util.similarity_of_individuals(pop[x], last_generated) <= 0.25:
            models.append(util.create_model(pop[x], med))
            last_generated = pop[x]

    aux = []
    for x in models:
        aux.append(list(x))

    #### SLAVE ###
    print population_size
    print len(models)

    print '[',
    for x in models[0]:
        print '%.2f' % x,
    print ']'
    # Generating the new population for each probabilist model #
    oi = 1
    last = problem.get_fitness(last_generated)
    while True:
    #while oi < 1000:
        print '------init------'
        populations = []
        for model_id in xrange(len(models)):
            populations.append(util.new_population(problem))

        # The magic #
        for model_id in xrange(len(models)):
            for model_item_id in xrange(len(models[model_id])):
                for bit_id in xrange(len(populations[model_id][model_item_id])):
                    if random.random() < models[model_id][model_item_id]:
                        populations[model_id][model_item_id][bit_id] = '1'
                    else:
                        populations[model_id][model_item_id][bit_id] = '0'

        # Calculate the best individual of each probabilist model #
        bests = [None] * len(models)
        for model_id in xrange(len(models)):
            bests[model_id] = populations[model_id][0]
            for model_item_id in xrange(1, len(models[model_id])):
                print math.fabs(problem.get_fitness(bests[model_id]))
                if math.fabs(problem.get_fitness(bests[model_id])) > math.fabs(problem.get_fitness(populations[model_id][model_item_id])):
                    bests[model_id] = populations[model_id][model_item_id]

        # Calculate the bestest #
        b = bests[0]
        for best in bests:
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

        # Learing model
        new = math.fabs(problem.get_fitness(b))
        util.learning(last, new)
        last = new

        print '[',
        for x in models[0]:
            print '%.2f' % x,
        print ']'

        v = []
        v.append(util.to_int(b[:10]))
        v.append(util.to_int(b[10:20]))
        v.append(util.to_int(b[20:30]))
        print b
        print v, '\t\t',problem.get_fitness(b), conf.ALPHA
        print '------end------'
        oi += 1


    for x in xrange(len(models)):
        print '>>', x, '<<'
        for y in xrange(len(models[x])):
            print aux[x][y], " -> ", models[x][y]

if __name__ == '__main__':
    print 'INIT'
    run(rastrigin)
    print 'END'
