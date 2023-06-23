import numpy as np
from time import time
from genetics.population import generate_population
from genetics.evolution import *
from objects.image import ImageBuilder, ImagePixelator


TARGET_FILEPATH = r"..\images\input-examples\squidward.jpg" # change to valid image/path
NUM_PIXELS = 32
NUM_POPULATION = 100
NUM_GENERATIONS = 15000
NUM_ELITES = 20
RATE_MUTATION = 0.15

# Not yet used
MUTATION_BIAS = 20
STATS_FREQUENCY = 25
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
    best = select_best(current_generation, target, proportion=NUM_ELITES)
    best_score = image_fitness(best[0], target)

    print("generation: %d | best fitness: %d" %(_, best_score))
    # if(_ % STATS_FREQUENCY == 0):
    #     # ImageBuilder(np.array(current_generation[0]), "%d"%(_))
    #     print("gen: %d | best_score: %d" %(_, best_score))
    #     if(_ != 0):
    #          print("%d generations took %s seconds" %(STATS_FREQUENCY, str(time() - gen_compute_time)))
    #     gen_compute_time = time()


    ### Elite-dominant scheme ###
    # Pure Elitism
    for img in best:
        next_generation.append(img)
    
    # Elitist Breeding Version A (Basic, to be updated)
    # for idx in range(NUM_ELITES - 1):
    #     next_generation.append(breed_images(best[idx], best[idx+1]))

    # Version B (Test)
    for idx in range(0, NUM_ELITES):
        next_generation.append(breed_images(best[0], best[idx]))

    # Random Elitist Breeding
    for n in range(NUM_POPULATION - (2*NUM_ELITES)):
        idx1 = np.random.randint(0, len(best))
        idx2 = np.random.randint(0, len(best))
        offspring = breed_images(best[idx1], best[idx2])
        next_generation.append(offspring)

    current_generation = mutate_population(next_generation, mutation_rate=RATE_MUTATION)
    
best_score = population_fitness(current_generation, target)[0][0]
execution_time = time() - start_time
print("%d generations finished in %d seconds" %(NUM_GENERATIONS, execution_time))
print("%f was the best finess score" %(best_score))
result = ImageBuilder(np.array(current_generation[0]))
print("Result saved to /images/results/%s" %(result.filename))
