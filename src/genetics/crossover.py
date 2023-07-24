## NOTE: blend/bias/coinflip are very slow 

import numpy as np

def row_crossover(img_a, img_b, bias=0.5):
    n_dim = len(img_a)
    offspring = np.zeros((n_dim, n_dim, 3))

    for i in range(n_dim):
        if np.random.rand() < bias:
            offspring[i] = img_a[i]
        else:
            offspring[i] = img_b[i]

    return offspring

def col_crossover(img_a, img_b, bias=0.5):
    n_dim = len(img_a)
    offspring = np.zeros((n_dim, n_dim, 3))
    
    for i in range(n_dim):
        if np.random.rand() < bias:
            offspring[:, i] = img_a[:, i]
        else:
            offspring[:, i] = img_b[:, i]
    
    return offspring

def blend_crossover(img_a, img_b):
    n_dim = len(img_a)
    offspring = np.zeros((n_dim, n_dim, 3))
    for i in range(n_dim):
        for j in range(n_dim):
            offspring[i][j][0] = (img_a[i][j][0] + img_b[i][j][0]) /  2
            offspring[i][j][1] = (img_a[i][j][1] + img_b[i][j][1]) /  2
            offspring[i][j][2] = (img_a[i][j][2] + img_b[i][j][2]) /  2

    return offspring

def coinflip_crossover(img_a, img_b):
    n_dim = len(img_a)
    offspring = np.zeros((n_dim, n_dim, 3))
    for i in range(n_dim):
        for j in range(n_dim):
            if np.random.rand() < 0.5:
                offspring[i][j] = img_a[i][j]
            else:
                offspring[i][j] = img_b[i][j]

    return offspring

def biased_crossover(img_a, img_b, bias=0.5):
    n_dim = len(img_a)
    offspring = np.zeros((n_dim, n_dim, 3))

    for i in range(n_dim):
        for j in range(n_dim):
            if np.random.rand() < bias:
                offspring[i][j] = img_a[i][j]
            else:
                offspring[i][j] = img_b[i][j]

    return offspring
