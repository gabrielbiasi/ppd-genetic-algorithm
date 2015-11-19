# -*- coding: utf-8 -*-

from mpi4py import MPI
import math

import conf, util
from master import generate_models
from slave  import generate_populations, magic, get_bests, get_bestest

import schwefel
from traveling_salesman import TravelingSalesman

comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

problem = TravelingSalesman()

if size != 3:
    raise Exception('The algorithm needs 4 workers.')

if rank == 0:
    ## MASTER ##
    print '[MASTER] Starting'

    pop = util.new_population(problem)
    population_size = len(pop)

    ## 25% ##
    print '[MASTER] Sending to 25-work... '
    comm.send({'models': generate_models(pop, 0.25), 'data': problem.get_data()}, dest=1, tag=0)

    ## 50% ##
    print '[MASTER] Sending to 50-work... '
    comm.send({'models': generate_models(pop, 0.50), 'data': problem.get_data()}, dest=2, tag=0)

    ## 75% ##
    #print '[MASTER] Sending to 75-work... '
    #comm.send({'models': generate_models(pop, 0.75), 'data': problem.get_data()}, dest=3, tag=0)

    ## 100% ##
    #print '[MASTER] Sending to 100-work... '
    #comm.send({'models': generate_models(pop, 1.00), 'data': problem.get_data()}, dest=4, tag=0)

    print '[MASTER] Waiting... '

    v = []
    core_data = None
    response = comm.recv(core_data, source=1, tag=1)
    ind1, fitness1 = response['ind'], response['fitness']
    response = comm.recv(core_data, source=2, tag=2)
    ind2, fitness2 = response['ind'], response['fitness']
    # response = comm.recv(core_data, source=3, tag=3)
    # ind3, fitness3 = response['ind'], response['fitness']
    # response = comm.recv(core_data, source=4, tag=4)
    # ind4, fitness4 = response['ind'], response['fitness']

    print '\n--- 0.25 ---'
    print 'individual:', ''.join(ind1)
    print 'fitness:', fitness1
    print '\n--- 0.50 ---'
    print 'individual:', ''.join(ind2)
    print 'fitness:', fitness2
    print '\n--- 0.75 ---'
    #print 'individual', ''.join(ind3)
    # print 'fitness', fitness3
    print '\n--- 1.00 ---'
    #print 'individual', ''.join(ind4)
    # print 'fitness', fitness4


else:
    ## SLAVE ##
    recv_data = comm.recv(source=0, tag=0)
    models = recv_data['models']
    problem.set_data(recv_data['data'])
    print '[', str(rank), '] received.'

    last = 999
    while True:
        populations = generate_populations(problem, len(models))

        magic(populations, models, problem)

        bests = get_bests(populations, models, problem)
        b = get_bestest(bests, problem)

        if problem.is_finished(b):
            final_fitness = problem.get_fitness(b)
            break

        # Calculate the new probabilist models #
        for model in models:
            util.update_model(model, b)

        # Mutate each probabilist model #
        for model in models:
            util.mutate_model(model)

        # Learning model
        new = math.fabs(problem.get_fitness(b))
        util.learning(last, new)
        last = new

        print '[', rank, ']', problem.show(b), '\t\t', problem.get_fitness(b),'\t\t', conf.ALPHA


    print '[', rank, '] finished. Sending... ',
    comm.send({'ind': b, 'fitness': final_fitness}, dest=0, tag=rank)
