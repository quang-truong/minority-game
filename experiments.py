import numpy as np

from Games import Single_Stage_Game, Single_Stage_Network_Game
from Agent import Agent

def vary_brain_size(T: int, N: int, brain_size: int, num_strategies: int, seed: int):
    np.random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past
    games = []
    for i in range(T):
        game = Single_Stage_Game(i, N, agents, past_games= past_games, threshold = 0.5, time_limit= None)
        game.start()
        game.update()                   # let agents update strategy
        past_games += '1' if game.final_result[0] == 'Bar' else '0'
        games.append(game)
    return games
    
def vary_network(T: int, N: int, brain_size: int, num_strategies: int, p: float, seed: int, directed: bool):
    np.random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past
    games = []
    for i in range(T):
        game = Single_Stage_Network_Game(i, N, agents, past_games= past_games, threshold = 0.5, p = p, directed = directed, time_limit= None, seed = seed)
        game.start()
        game.update()                   # let agents update strategy
        past_games += '1' if game.final_result[0] == 'Bar' else '0'
        games.append(game)
    return games