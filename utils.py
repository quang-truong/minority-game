import numpy as np
import matplotlib.pyplot as plt

def plot_games_result(games, xlim, ylim_lower, ylim_upper):
    game_index = []
    num_bar = [] 
    for i in range(len(games)):
        game_index.append(i)
        num_bar.append(games[i][1])
    
    plt.plot(game_index, num_bar)
    plt.xlim(0, xlim)
    plt.ylim(ylim_lower, ylim_upper)
    plt.show()