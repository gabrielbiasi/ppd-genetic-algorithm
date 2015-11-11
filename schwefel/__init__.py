import math, random, util
"""
Schwefel's function
This file have anything about we need to test the schwefel's function.
"""

NUM_BITS = 30

def new_individual():
    ind = []
    for x in xrange(NUM_BITS):
        ind.append(str(random.randint(0,1)))
    return ind

def get_fitness(chromosome):
    v = []
    v.append(util.to_int(chromosome[:10]))
    v.append(util.to_int(chromosome[10:20]))
    v.append(util.to_int(chromosome[20:30]))

    print v

    alpha = 418.982887
    fitness = 0
    for i in range(len(v)):
        fitness -= v[i]*math.sin(math.sqrt(math.fabs(v[i])))
    return float(fitness) + alpha*len(v)
