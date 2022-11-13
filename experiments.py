import numpy as np

from Games import Traditional_Minority_Game, Network_Minority_Game, Disconnected_Network_Minority_Game_10, Disconnected_Network_Minority_Game_5
from Agent import Agent

from typing import List

def vary_brain_size(T: int, N: int, brain_size: int, num_strategies: int, seed: int):
    np.random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

    game = Traditional_Minority_Game(T, N, agents, past_games = past_games, threshold = 0.5, time_limit= None)
    game.start()
    return game
    
def vary_network(T: int, N: int, brain_size: int, num_strategies: int, p: float, seed: int, time_step : List[int]):
    np.random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

    game = Network_Minority_Game(T, N, agents, past_games = past_games, 
                                threshold = 0.5, p = p,
                                time_step = time_step,
                                time_limit= None, seed = seed)
    game.network.plot_graph()
    game.start()
    return game

def vary_disconnected_network_10(T: int, N: int, brain_size: int, num_strategies: int, seed: int, time_step : List[int]):
    np.random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

    game = Disconnected_Network_Minority_Game_10(T, N, agents, past_games = past_games, 
                                threshold = 0.5,
                                time_step = time_step,
                                time_limit= None, seed = seed)
    game.network.plot_graph()
    game.start()
    return game

def vary_disconnected_network_5(T: int, N: int, brain_size: int, num_strategies: int, seed: int, time_step : List[int]):
    np.random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

    game = Disconnected_Network_Minority_Game_5(T, N, agents, past_games = past_games, 
                                threshold = 0.5,
                                time_step = time_step,
                                time_limit= None, seed = seed)
    game.network.plot_graph()
    game.start()
    return game