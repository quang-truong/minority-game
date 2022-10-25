import numpy as np

def random_strategy(num_strategy, brain_size):
    bin_strings =  np.random.randint(0, 2, size = (num_strategy, 2**brain_size))
    return bin_strings