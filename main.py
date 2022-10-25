import numpy as np

from Games import Single_Stage_Game
from Agent import Agent

import utils

def main():
    T = 1000
    N = 1001
    brain_size = 6                         # M
    num_strategies = 5                      # S
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past
    games = []
    for i in range(T):
        game = Single_Stage_Game(i, N, agents, past_games= past_games, threshold = 0.5, time_limit= None)
        game.start()
        game.update()                   # let agents update strategy
        past_games += '1' if game.final_result[0] == 'Bar' else '0'
        games.append(game)
    utils.plot_games_result(games)


if __name__ == "__main__":
    main()