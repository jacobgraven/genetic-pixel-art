import numpy as np
from uuid import uuid4 as id
from pathlib import Path

from objects.image import ImagePixelator, ImageBuilder
from genetics.population import generate_population
from genetics.evolution import *


# FILEPATH = None
N_POPULATION = 10
N_PIXELS = 32

# FIX PATH HERE
# image_data = ImagePixelator(r"..\images\input-examples\cats/cleo.jpg", 32)


target_arr = image_data.pixel_array
# pop_arr = generate_population(10, 16)
# pop_example = pop_arr[0]

ImageBuilder(target_arr)

# breed_test_arr = [[[2, 2, 2], [3, 3, 3]], [[4, 4, 4], [5, 5, 5]]]
# print(np.array(breed_test_arr[0][0] + breed_test_arr[0][0]) /  2)
# built_image = ImageBuilder(target_arr)

# print(image_fitness(pop_example, target_arr))
# print(mutate_image(pop_example))
# print(blender_crossover(pop_arr[0], pop_arr[1]))

# Grayscale tests

# gray_pop = generate_gray_population(10, 16)
# gray_example = gray_pop[0]
# ImageBuilder(gray_example)

current_generation = generate_population(10, 32)
best_img, best_fitness = select_routlette(current_generation, target_arr, proportion=5)
# best_score = best_fitness[0]
    
probability_values = []
total_fitness = np.sum(best_fitness)
for val in best_fitness:
    probability_values.append(val / total_fitness)
print(probability_values)
