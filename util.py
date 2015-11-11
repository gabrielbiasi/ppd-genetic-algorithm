"""
File to put some utils functions
"""

def to_bin(number):
    return list(bin(number))[2:]

def to_int(binary):
    return int(''.join(binary), 2)

def similarity_of_individuals(ind1, ind2):
    if len(ind1) != len(ind2):
        raise Exception('The chromossomes have different sizes!')

    hamming_distance = sum(c1 == c2 for c1, c2 in zip(ind1, ind2))
    return float(hamming_distance) / len(ind1)

def update_model(model, individual, alpha):
    for i in xrange(len(model)):
        model[i] = model[i] * (1.0 - alpha) + individual[i] * alpha
    return model
