"""
File to put some utils functions
"""
import random
import conf

def to_bin(number):
    return list(bin(number))[2:]


def to_int(binary):
    return int(''.join(binary), 2)


def similarity_of_individuals(ind1, ind2):
    if len(ind1) != len(ind2):
        raise Exception('The chromossomes have different sizes!')

    hamming_distance = sum(c1 == c2 for c1, c2 in zip(ind1, ind2))
    return float(hamming_distance) / len(ind1)


def mutate_model(model):
    for i, x in enumerate(model):
        if random.random() <  conf.MUT_POB:
            model[i] = x * (1.0 - conf.MUT_SH + random.randint(0,1) * conf.MUT_SH
    return model
