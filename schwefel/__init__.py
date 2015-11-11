import math, random, util
"""
Schwefel's function
This file have anything about we need to test the schwefel's function.
"""

FITNESS = 0.1
NUM_BITS = 30

def new_individual():
    ind = []
    for x in xrange(NUM_BITS):
        ind.append(str(random.randint(0,1)))
    return ind

def to_vector(li):
    v = []
    v.append(util.to_int(li[:10]))
    v.append(util.to_int(li[10:20]))
    v.append(util.to_int(li[20:30]))
    print v

def get_fitness(li):
    v = []

    v.append(util.to_int(li[:10]))
    v.append(util.to_int(li[10:20]))
    v.append(util.to_int(li[20:30]))

    alpha = 418.982887
    fitness = 0
    for i in range(len(v)):
        fitness -= v[i]*math.sin(math.sqrt(math.fabs(v[i])))
    return float(fitness) + alpha*len(v)


def is_finished(individual):
    f = get_fitness(individual)
    return f <= FITNESS and f >= -FITNESS



