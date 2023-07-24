import numpy as np
from time import time
from genetics.population import generate_population
from genetics.evolution import *
from objects.image import ImageBuilder, ImagePixelator

TARGET_FILEPATH = r"../images/input-examples/test3.jpg"

NUM_PIXELS = 45
NUM_POPULATION = 250
NUM_GENERATIONS = 1000
NUM_ELITES = 50
RATE_MUTATION = 0.15

# Not yet implemented for use
MUTATION_BIAS = 20
STATS_FREQUENCY = 100
MUTATION_FUNCTION = "fast_gauss_mutation"
CROSSOVER_FUNCTION = "row_crossover"


target_object = ImagePixelator(TARGET_FILEPATH, NUM_PIXELS)
target = target_object.pixel_array
init_population = generate_population(NUM_POPULATION, NUM_PIXELS)
current_generation = init_population

# Simulation Implementation (1) - Basic elitist gene propagation

start_time = time()
for _ in range(NUM_GENERATIONS):
    next_generation = []
    # best = select_best(current_generation, target, proportion=NUM_ELITES)
    # best_score = image_fitness(best[0], target)

    best, best_fitness = select_routlette(current_generation, target, proportion=NUM_ELITES)
    best_score = best_fitness[0]
    print("generation: %d | best fitness: %d" %(_, best_score))
    # print(len(current_generation))
    probability_values = []
    total_fitness = np.sum(best_fitness)
    for val in best_fitness:
        probability_values.append(val / total_fitness)

    cumulative_probabilities = [sum(probability_values[:i+1]) for i in range(len(probability_values))]

    for img in best:
        next_generation.append(img)

    breeding_selection = np.random.choice(NUM_ELITES, 2*(NUM_POPULATION-NUM_ELITES), cumulative_probabilities)
    
    if(len(breeding_selection) % 2 != 0):
        breeding_selection.append(0)
    for i in range(NUM_POPULATION-NUM_ELITES):
        parent_a = best[int(breeding_selection[2*i])]
        parent_b = best[int(breeding_selection[(2*i) + 1])]
        next_generation.append(breed_images(parent_a, parent_b))

    current_generation = mutate_population(next_generation, mutation_rate=RATE_MUTATION)
    

best_score = population_fitness(current_generation, target)[0][0]
execution_time = time() - start_time
print("%d generations finished in %d seconds" %(NUM_GENERATIONS, execution_time))
print("%f was the best finess score" %(best_score))
result = ImageBuilder(np.array(current_generation[0]))
print("Result saved to /images/results/%s" %(result.filename))