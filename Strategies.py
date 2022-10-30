import numpy as np

def random_strategy(num_strategy: int, brain_size: int):
    bin_strings =  np.random.randint(0, 2, size = (num_strategy, 2**brain_size))
    return bin_strings