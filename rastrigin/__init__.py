import math, random, util
"""
Rastigin function

"""

LIMIT_VALUE = 500
FITNESS = 0.1
NUM_BITS_IN_NUM = 10
AMOUNT_NUN = 3

# 10 bits to each number: 1 bit = signal and 9 bits = number

#sign bit = 1 --> positive
#sign bit = 0 --> negative

def new_individual():
    ind = []
    condition = True
    while condition:
        ind = []
        pass
        for x in xrange(NUM_BITS_IN_NUM*AMOUNT_NUN):
            ind.append(str(random.randint(0,1)))
        condition = valide_individual(ind)

    return ind

def get_fitness(individual):
    v = []
    for i in xrange(AMOUNT_NUN):
        id_sign = i*NUM_BITS_IN_NUM
        number = int(''.join(individual[id_sign+1:(i+1)*NUM_BITS_IN_NUM]), 2)
        if individual[id_sign] == "1":
            v.append(-number)
        else:
            v.append(number)

    alpha = 10
    fitness = 0
    for i in range(len(v)):
        fitness += v[i]**2 - alpha*math.sin(2*math.pi*v[i])
    return float(fitness) + alpha*len(v)


def is_finished(individual):
    f = get_fitness(individual)
    return f <= FITNESS and f >= -FITNESS


def valide_individual(individual):
    '''
    validation of an individual to find out if it is part of the domain
    '''
    for i in xrange(AMOUNT_NUN):
        number = int(''.join(individual[(i*NUM_BITS_IN_NUM)+1:(i+1)*NUM_BITS_IN_NUM]), 2)
        if LIMIT_VALUE <= math.fabs(number):
            return True

    return False

def number_bits():
    return NUM_BITS_IN_NUM * AMOUNT_NUN

def show(individual):
    string = "[ "
    for i in xrange(AMOUNT_NUN):
        id_sign = i*NUM_BITS_IN_NUM
        sign = "" if individual[id_sign] == "1" else "-"
        number = int(''.join(individual[id_sign+1:(i+1)*NUM_BITS_IN_NUM]), 2)
        string += sign+str(number)
        string += ", " if i+1 < AMOUNT_NUN else " "

    print string+"]"
