import numpy as np

def generate_random_image(n_px):
    """
    Generates a random image object
    
    The object returned is an array with dim=(n_px, n_px, 3). Each inner
    array (consisting of 3 values) encodes the RGB values for a pixel 
    """
    r_values = np.random.randint(0, 256, size=(n_px, n_px))
    g_values = np.random.randint(0, 256, size=(n_px, n_px))
    b_values = np.random.randint(0, 256, size=(n_px, n_px))
    random_img = np.dstack((r_values, g_values, b_values))
    return random_img

def generate_population(pop_size, n_px):
    """
    Generate a set of random images
    """
    population = []
    for _ in range(pop_size):
        population.append(generate_random_image(n_px))
    return population