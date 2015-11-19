# -*- coding: utf-8 -*-

from mpi4py import MPI
import math
import sys

import conf, util
from master import generate_models
from slave  import generate_populations, magic, get_bests, get_bestest

from rastrigin import Rastrigin
from schwefel import Schwefel
from traveling_salesman import TravelingSalesman

comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

if size != 3:
    raise Exception('The algorithm needs 2 workers.')

if rank == 0:
    ## MASTER ##
    print '[MASTER] Starting'

    print '\nChoose the algorithm to be executed:\n'
    print '1. Schwefel\'s Function'
    print '2. Traveling Salesman'
    print '3. Rastrigim Function'
    print '4. Radio Network Optimization'
    print '\n0. Exit\n'

    while True:
        try:
            option = int(raw_input("Enter an option: "))
            if option < 0 or option > 4:
                print "Invalid option"
            else:
                break
        except:
            print "Invalid option"

    if option == 1:
        problem = Schwefel()
    elif option == 2:
        problem = TravelingSalesman()
    elif option == 3:
        problem = Rastrigin()
    elif option == 4:
        print "Radio not implemented"
        sys.exit(0)
    else:
        sys.exit(0)

    pop = util.new_population(problem)

    ## 25% ##
    print '[MASTER] Sending to 25-work... '
    comm.send({'problem': problem, 'models': generate_models(pop, 0.25), 'data': problem.get_data()}, dest=1, tag=0)

    ## 50% ##
    print '[MASTER] Sending to 50-work... '
    comm.send({'problem': problem, 'models': generate_models(pop, 0.50), 'data': problem.get_data()}, dest=2, tag=0)

    ## 75% ##
    #print '[MASTER] Sending to 75-work... '
    #comm.send({'problem': problem, 'models': generate_models(pop, 0.75), 'data': problem.get_data()}, dest=3, tag=0)

    ## 100% ##
    #print '[MASTER] Sending to 100-work... '
    #comm.send({'problem': problem, 'models': generate_models(pop, 1.00), 'data': problem.get_data()}, dest=4, tag=0)

    print '[MASTER] Waiting... '

    v = []
    ind1 = comm.recv(source=1, tag=1)
    ind2 = comm.recv(source=2, tag=2)
    #ind3 = comm.recv(source=3, tag=3)
    #ind4 = comm.recv(source=4, tag=4)

    print '0.25> ', ind1, problem.get_fitness(ind1)
    print '0.50> ', ind2, problem.get_fitness(ind2)
    #print '0.75> ', ind3, problem.get_fitness(ind3)
    #print '1.00> ', ind4, problem.get_fitness(ind4)
    print 'END'


else:
    ## SLAVE ##
    recv_data = comm.recv(source=0, tag=0)
    problem = recv_data['problem']
    models = recv_data['models']
    problem.set_data(recv_data['data'])

    print '[', rank, ']', 'Models: ', len(models)
    last = 999
    while True:
        populations = generate_populations(problem, len(models))

        magic(populations, models, problem)

        bests = get_bests(populations, models, problem)
        b = get_bestest(bests, problem)

        if problem.is_finished(b):
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


    print '[', rank, '] finished.', problem.show(b)
    comm.send(b, dest=0, tag=rank)
