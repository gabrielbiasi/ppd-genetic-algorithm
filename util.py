"""
File to put some utils functions
"""
import random
import conf

def to_bin(number):
    return list(bin(number))[2:]


def to_int(binary):
    signal = -1 if binary[0] == '1' else 1
    number = int(''.join(binary[1:]), 2)
    return signal*number


def similarity_of_individuals(ind1, ind2):
    if len(ind1) != len(ind2):
        raise Exception('The chromossomes have different sizes!')

    hamming_distance = sum(c1 == c2 for c1, c2 in zip(ind1, ind2))
    return float(hamming_distance) / len(ind1)


def create_model(individual):
    model = []
    for x in individual:
        model.append((0.5 - conf.ALPHA) * int(x)  + conf.ALPHA * 1)
    return model

def update_model(model, individual):
    for i in xrange(len(model)):
        model[i] = model[i] * (1.0 - conf.ALPHA) + int(individual[i]) * conf.ALPHA


def mutate_model(model):
    for i, x in enumerate(model):
        if random.random() < conf.MUT_PROB:
            model[i] = x * (1.0 - conf.MUT_SH) + random.randint(0,1) * conf.MUT_SH

def learning(previous, new):
    if new < previous:
        conf.ALPHA = conf.ALPHA * (1 + conf.Q)
    else:
        conf.ALPHA = conf.ALPHA_INIT

def new_population(problem):
    population_size = (problem.num_bits() ** 2)
    pop = []
    for x in xrange(population_size):
        ind = problem.new_individual()
        pop.append(ind)
    return pop
