import math, random, util
"""
Schwefel's function
This file have anything about we need to test the schwefel's function.
"""

LIMIT_VALUE = 1000
FITNESS = 0.1
NUM_BITS_IN_NUM = 10
AMOUNT_NUM = 3


# 10 bits to each number: 1 bit = signal and 9 bits = number

def new_individual():
    ind = []
    loop = False
    while not loop:
        ind = []
        for x in xrange(NUM_BITS_IN_NUM*AMOUNT_NUM):
            ind.append(str(random.randint(0,1)))
        loop = valide_individual(ind)
    return ind

def get_fitness(individual):
    v = []
    for i in xrange(AMOUNT_NUM):
        number = int(''.join(individual[i*NUM_BITS_IN_NUM:(i+1)*NUM_BITS_IN_NUM]), 2)
        v.append(number - 500)

    alpha = 418.982887
    fitness = 0
    for i in range(AMOUNT_NUM):
        fitness -= v[i]*math.sin(math.sqrt(math.fabs(v[i])))
    # print "fitness :", float(fitness) + alpha*AMOUNT_NUM
    return float(fitness) + alpha*AMOUNT_NUM


def is_finished(individual):
    f = get_fitness(individual)
    return f <= FITNESS and f >= -FITNESS


def valide_individual(individual):
    '''
    validation of an individual to find out if it is part of the domain
    '''
    for i in xrange(AMOUNT_NUM):
        number = int(''.join(individual[i*NUM_BITS_IN_NUM:(i+1)*NUM_BITS_IN_NUM]), 2)
        if LIMIT_VALUE < number:
            return False
    return True

def num_bits():
    return NUM_BITS_IN_NUM * AMOUNT_NUM


def show(individual):
    string = "[ "
    for i in xrange(AMOUNT_NUM):
        number = int(''.join(individual[i*NUM_BITS_IN_NUM:(i+1)*NUM_BITS_IN_NUM]), 2)
        string += str(number - 500)
        string += ", " if i+1 < AMOUNT_NUM else " "

    return string+"]"