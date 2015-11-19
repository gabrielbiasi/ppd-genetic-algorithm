import util


def generate_models(pop, best, porcentage):
    models = []
    last_generated = best

    models.append(util.create_model(last_generated))
    for x in xrange(0, len(pop)):
        if util.similarity_of_individuals(pop[x], last_generated) <= porcentage:
            models.append(util.create_model(pop[x]))
            last_generated = pop[x]

    return models
