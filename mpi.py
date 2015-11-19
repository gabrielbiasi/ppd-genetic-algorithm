# -*- coding: utf-8 -*-

from mpi4py import MPI
import math
import sys

import conf, util
from master import generate_models
from slave  import generate_populations, magic, get_bests, get_bestest

from rastrigin import Rastrigin
from radio_network import RadioNetwork
from schwefel import Schwefel
from traveling_salesman import TravelingSalesman

comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

if size != 5:
    raise Exception('The algorithm needs 4 workers.')

if rank == 0:
    ## MASTER ##

    print 'Choose the algorithm to be executed:\n'
    print '1. Schwefel\'s Function'
    print '2. Traveling Salesman'
    print '3. Rastrigim Function'
    print '4. Radio Network Optimization'
    print '\n0. Exit\n'

    while True:
        print 'Enter an option:'
        try:
            option = int(raw_input())
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
        problem = RadioNetwork()

    if option >= 1 and option <= 4:
        print '[MASTER] Starting'

        # Generate the population to create the probabilist models #
        pop = util.new_population(problem)

        # Get the best to use as a model to the others #
        best_boy = get_bestest(pop, problem)

        ## 25% ##
        comm.send({'problem': problem, 'models': generate_models(pop, best_boy, 0.25), 'data': problem.get_data()}, dest=1, tag=0)

        ## 50% ##
        comm.send({'problem': problem, 'models': generate_models(pop, best_boy, 0.50), 'data': problem.get_data()}, dest=2, tag=0)

        ## 75% ##
        comm.send({'problem': problem, 'models': generate_models(pop, best_boy, 0.75), 'data': problem.get_data()}, dest=3, tag=0)

        ## 100% ##
        comm.send({'problem': problem, 'models': generate_models(pop, best_boy, 1.00), 'data': problem.get_data()}, dest=4, tag=0)


        print '[MASTER] Waiting... '

        # Wait for the response #
        v = []
        v.append(comm.recv(source=1, tag=1))
        v.append(comm.recv(source=2, tag=2))
        v.append(comm.recv(source=3, tag=3))
        v.append(comm.recv(source=4, tag=4))

        # Print the best of each worker #

        print '25%  > ', problem.show(v[0]), problem.get_fitness(v[0])
        print '50%  > ', problem.show(v[1]), problem.get_fitness(v[1])
        print '75%  > ', problem.show(v[2]), problem.get_fitness(v[2])
        print '100% > ', problem.show(v[3]), problem.get_fitness(v[3])

        # Print the bestest #
        b = get_bestest(v)
        print 'BEST > ', problem.show(b), problem.get_fitness(b)

        # end! #

    else:
        # Signal for workers shutdown #
        comm.send(None, dest=1, tag=0)
        comm.send(None, dest=2, tag=0)
        comm.send(None, dest=3, tag=0)
        comm.send(None, dest=4, tag=0)

    print 'END'

else:
    ## SLAVE ##
    recv_data = comm.recv(source=0, tag=0)
    if recv_data:
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

        print '[', rank, '] finished! ', problem.show(b)
        comm.send(b, dest=0, tag=rank)
