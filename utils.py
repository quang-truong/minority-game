import numpy as np
import matplotlib.pyplot as plt

from Games import Single_Stage_Game

def plot_games_result(games, xlim, ylim_lower, ylim_upper):
    game_index = []
    num_bar = [] 
    for game in games:
        game_index.append(game.index)
        num_bar.append(game.final_result[1])
    
    plt.plot(game_index, num_bar)
    plt.xlim(0, xlim)
    plt.ylim(ylim_lower, ylim_upper)
    plt.show()