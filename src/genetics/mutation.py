# NOTE: random/regular gauss mutations are very slow

import numpy as np

def random_mutation(img, max_px=25):
    """
    Random pixel mutation
    """
    mutated = np.copy(img)
    for _ in range(np.random.randint(0, max_px)):
        row = np.random.randint(0, len(img))
        col = np.random.randint(0, len(img))
        mutated[row][col] = (np.random.randint(0, 256), 
                             np.random.randint(0, 256), 
                             np.random.randint(0, 256))
    
    return mutated

def fast_gauss_mutation(img, px_rate=.25, std=25, mean=0):
    """
    Row (Fast) Gaussian mutation (single-row mutation)
    """
    n_dim = len(img)
    mutated = np.copy(img)
    row = np.random.randint(0, n_dim)
    for i in range(n_dim):
        if(np.random.rand() < px_rate):
            dR, dG, dB = np.random.normal(mean, std, 3) # (mean, std, samples)
                
            mutated[row][i][0] += dR
            mutated[row][i][1] += dG
            mutated[row][i][2] += dB
                
            mutated[row][i] = np.clip(mutated[row][i], 0, 255)

    return mutated

def gaussian_mutation(img, px_rate=0.4, std=25, mean=0):
    """
    Gaussian mutation (slow)
    """
    n_dim = len(img)
    mutated = np.copy(img) # mutated = img
    for i in range(n_dim):
        for j in range(n_dim):
            rmut = np.random.rand()
            if(rmut < px_rate):
                            
                dR, dG, dB = np.random.normal(mean, std, 3) # (mean, std, samples)
                
                mutated[i][j][0] += dR
                mutated[i][j][1] += dG
                mutated[i][j][2] += dB

                # mutated[i][j][:] += [dR, dG, dB]

                mutated[i][j] = np.clip(mutated[i][j], 0, 255)

    return mutated
