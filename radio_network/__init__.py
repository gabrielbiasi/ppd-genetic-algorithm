import math, random, util
"""
Radio network optimization module 
"""

PRECISION_COORD = 1
X = 1 
Y = 3
BSS = 20

# 10 bits to each number: 1 bit = signal and 9 bits = number

#sign bit = 1 --> positive
#sign bit = 0 --> negative

class Radio():

    data = None
    FITNESS = 0
    def monitor_coords(self, y, x):
        # for i in y*2:
        pass




    def id_in_coords(self, id):
        
        l = get_line
        c = get_column
        x = id % c 
        y = int(id/c)
        coord_x = x - int(c/2)
        coord_y = int(l/2) - y 
        print x , y
        print coord_x, coord_y
        return coord_x, coord_y


    def get_line(self):
        return X * 2 + 1


    def get_column(self):
        return Y * 2 + 1

    def get_area_matriz(self):
        return get_line() * get_column()


    def new_individual(self):
        ind = []
        loop = False
        area_matriz = get_area_matriz()
        while not loop:
            ind = []
            for x in xrange(BSS*(len(bin(area_matriz)[2:]))):
                ind.append(str(random.randint(0,1)))
            loop = validate_individual(ind, len(bin(area_matriz)[2:]), area_matriz)
        return ind



    def validate_individual(self, individual, n_bits, area_matriz):
        '''
        validation of an individual to find out if it is part of the domain
        '''
        for i in xrange(BSS):
            number = int(''.join(individual[i*n_bits:(i+1)*n_bits]), 2)
            if area_matriz <= math.fabs(number):
                return False

        return True

    def get_fitness(self, individual):
        v = []
        for i in xrange(BSS):
            number = int(''.join(individual[i*NUM_BITS_IN_NUM:(i+1)*NUM_BITS_IN_NUM]), 2)
            v.append((number - 512))

        alpha = 10
        fitness = 0
        for i in range(AMOUNT_NUM):
            fitness += v[i]**2 - alpha*math.cos(2*math.pi*v[i])
        return float(fitness) + alpha*AMOUNT_NUM







    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
























"""

    def is_finished(individual):
        f = get_fitness(individual)
        return f <= FITNESS and f >= -FITNESS




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
"""
