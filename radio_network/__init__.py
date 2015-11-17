import math, random, util
"""
Radio network optimization module 
"""

PRECISION_COORD = 1
X = 1 
Y = 3
DATA = None

# 10 bits to each number: 1 bit = signal and 9 bits = number

#sign bit = 1 --> positive
#sign bit = 0 --> negative


def monitor_coords(y,x):
    # for i in y*2:
    pass




def id_in_coords(id):
    
    l = X * 2 + 1
    c = Y * 2 + 1
    x = id % c 
    y = int(id/c)
    coord_x = x - int(c/2)
    coord_y = int(l/2) - y 
    print x , y
    print coord_x, coord_y





































def new_individual():
    ind = []
    loop = False
    while not loop:
        ind = []
        for x in xrange(NUM_BITS_IN_NUM*AMOUNT_NUM):
            ind.append(str(random.randint(0,1)))
        loop = validate_individual(ind)
    return ind

def get_fitness(individual):
    v = []
    for i in xrange(AMOUNT_NUM):
        number = int(''.join(individual[i*NUM_BITS_IN_NUM:(i+1)*NUM_BITS_IN_NUM]), 2)##----
        v.append((number - 512))##---

    alpha = 10
    fitness = 0
    for i in range(AMOUNT_NUM):
        fitness += v[i]**2 - alpha*math.cos(2*math.pi*v[i])
    return float(fitness) + alpha*AMOUNT_NUM


def is_finished(individual):
    f = get_fitness(individual)
    return f <= FITNESS and f >= -FITNESS


def validate_individual(individual):
    '''
    validation of an individual to find out if it is part of the domain
    '''
    for i in xrange(AMOUNT_NUM):
        number = int(''.join(individual[i*NUM_BITS_IN_NUM:(i+1)*NUM_BITS_IN_NUM]), 2)###---
        if LIMIT_VALUE < math.fabs(number):
            return False

    return True

def num_bits():
    return NUM_BITS_IN_NUM * AMOUNT_NUM

def show(individual):
    string = "[ "
    for i in xrange(AMOUNT_NUM):
        number = int(''.join(individual[i*NUM_BITS_IN_NUM:(i+1)*NUM_BITS_IN_NUM]), 2)
        string += str(number - 512)
        string += ", " if i+1 < AMOUNT_NUM else " "

    print string+"]"

def set_data(data):
    DATA = data

def get_data():
    return data