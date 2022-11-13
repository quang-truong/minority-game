import numpy as np

from Agent import Agent

def aggregate_all_neighbor_strategies(agent: Agent, neighbor: Agent):
    mask_row_index = [i for i in range(neighbor.num_strategies)]
    for i in range(neighbor.strategies.shape[0]):
        if ((neighbor.strategies[i] == agent.strategies).all(axis = 1).any()):      # Duplicate Strategies
            mask_row_index.remove(i)
    masked_strategies = neighbor.strategies[mask_row_index]
    masked_virtual_point = neighbor.virtual_point[mask_row_index]
    return masked_strategies, masked_virtual_point

def aggregate_best_neighbor_strategies(agent: Agent, neighbor: Agent):
    neighbor_best_strategy = neighbor.best_strategy
    neighbor_best_virtual_point = np.max(neighbor.virtual_point)
    if ((neighbor_best_strategy == agent.strategies).all(axis = 1).any()):          # Duplicate strategies
        return None, None
    return neighbor_best_strategy, neighbor_best_virtual_point