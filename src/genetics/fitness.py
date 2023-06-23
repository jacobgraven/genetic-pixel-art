import numpy as np

def mse_fitness(input_img, target_img):
    """ 
    Mean squared error fitness function. 
    """
    # input_np = np.array(input_img)
    # target_np = np.array(target_img)
    # fitness = np.mean((input_img - target_img) ** 2)
    return np.mean((input_img - target_img) ** 2)  

def mae_fitness(input_img, target_img):
    """ 
    Mean absolute error fitness function 
    """
    # input_np = np.array(input_img)
    # target_np = np.array(target_img)
    # fitness = np.mean(np.abs(input_img - target_img))
    return np.mean(np.abs(input_img - target_img))

def rmse_fitness(input_img, target_img):
    """ 
    Root mean squared error fitness function
    """
    return np.sqrt(mse_fitness(input_img, target_img))

def mase_fitness(input_img, target_img):
    """
    Mean absolute squared error fitness function
    """
    # input_np = np.array(input_img)
    # target_np = np.array(target_img)
    # fitness = np.mean(np.abs(input_img - target_img) ** 2)
    return np.mean(np.abs(input_img - target_img) ** 2)