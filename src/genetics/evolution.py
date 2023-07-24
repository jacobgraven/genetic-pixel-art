import numpy as np
from .fitness import *
from .crossover import *
from .mutation import *

def image_fitness(img, target_img):
    # return rmse_fitness(img, target_img)
    # return mae_fitness(img, target_img)
    # return mase_fitness(img, target_img)
    return mse_fitness(img, target_img)

def mutate_image(image, bias=25):
    # return random_mutation(image, bias)
    # return gaussian_mutation(image)
    return fast_gauss_mutation(image)

def breed_images(image_a, image_b):
    # return biased_crossover(image_a, image_b)
    # return coinflip_crossover(image_a, image_b)
    # return blend_crossover(image_a, image_b)
    return row_crossover(image_a, image_b)
    # return col_crossover(image_a, image_b)

def population_fitness(current_pop, target_img):
    pop_fitness = []
    for arr in current_pop:
        pop_fitness.append((image_fitness(arr, target_img), arr))

    pop_fitness.sort(key = lambda x : x[0])
    return pop_fitness

def select_best(current_pop, target_img, proportion=20):
    fitness_data = population_fitness(current_pop, target_img)
    selection_pool = []
    for i in range(proportion):
        selection_pool.append(fitness_data[i][1])
    return selection_pool

def mutate_population(ranked_pop, mutation_rate, mutation_px_rate=0.5):
    mutated_pop = []
    for img in ranked_pop:
        if(np.random.rand() < mutation_rate):
            mutated_pop.append(mutate_image(img))
        else:
            mutated_pop.append(img)
    return mutated_pop

def select_best(current_pop, target_img, proportion=20):
    fitness_data = population_fitness(current_pop, target_img)
    selection_pool = []
    for i in range(proportion):
        selection_pool.append(fitness_data[i][1])
    return selection_pool

# TODO / CURRENTLY UNUSED
def breed_group(current_pop, target):
    breed_pool = select_best(current_pop, target)
    if(len(breed_pool) % 2 != 0):
        breed_pool.append(breed_pool[0])
    
    offspring_pool = []
    for _ in range(int(len(breed_pool) / 2)):
        offspring = breed_images(breed_pool.pop(), breed_pool.pop())
        offspring_pool.append(offspring)
    return offspring_pool

# TODO / CURRENTLY UNUSED
def select_routlette(current_pop, target_img, proportion=20):
    fitness_data = population_fitness(current_pop, target_img)
    selection_pool = []
    fitness_pool = []
    for i in range(proportion):
        selection_pool.append(fitness_data[i][1])
        fitness_pool.append(fitness_data[i][0])
    return selection_pool, fitness_pool