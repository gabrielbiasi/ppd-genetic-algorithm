import math 
"""
Schwefel's function
This file have anything about we need to test the schwefel's function.
"""

def get_fitness(chromosome):
	# TODO
	# for while accepting only integer numbers
	
	alpha = 418.982887
	fitness = 0
	for i in range(len(chromosome)):
		fitness -= chromosome[i]*math.sin(math.sqrt(math.fabs(chromosome[i])))
	return float(fitness) + alpha*len(chromosome)