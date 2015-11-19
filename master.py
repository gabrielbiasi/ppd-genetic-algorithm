import util


def generate_models(pop, porcentage=0.25):
    models = []
    last_generated = pop[0]

    models.append(util.create_model(last_generated))
    for x in xrange(1, len(pop)):
        if util.similarity_of_individuals(pop[x], last_generated) <= porcentage:
            models.append(util.create_model(pop[x]))
            last_generated = pop[x]

    return models
