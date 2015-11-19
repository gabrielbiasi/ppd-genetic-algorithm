import random, math
import util


def generate_populations(problem, size):
    populations = []
    for model_id in xrange(size):
        pop = util.new_population(problem)
        populations.append(pop)
    return populations


def magic(populations, models, problem):
    for model_id in xrange(len(models)):
        for model_item_id in xrange(len(models[model_id])):
            loop = False
            while not loop:
                for bit_id in xrange(len(populations[model_id][model_item_id])):
                    if random.random() < models[model_id][model_item_id]:
                        populations[model_id][model_item_id][bit_id] = '1'
                    else:
                        populations[model_id][model_item_id][bit_id] = '0'
                loop, populations[model_id][model_item_id] = problem.validate_individual(populations[model_id][model_item_id])


def get_bests(populations, models, problem):
    bests = [None] * len(models)
    for model_id in xrange(len(models)):
        bests[model_id] = populations[model_id][0]
        for model_item_id in xrange(1, len(models[model_id])):
            if math.fabs(problem.get_fitness(bests[model_id])) > math.fabs(problem.get_fitness(populations[model_id][model_item_id])):
                bests[model_id] = populations[model_id][model_item_id]
    return bests


def get_bestest(bests, problem):
    b = bests[0]
    for best in bests:
        if math.fabs(problem.get_fitness(best)) < math.fabs(problem.get_fitness(b)):
            b = best
    return b
