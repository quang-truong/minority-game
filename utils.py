import numpy as np
import matplotlib.pyplot as plt

from Games import Single_Stage_Game

def plot_games_result(games):
    game_index = []
    num_bar = [] 
    for game in games:
        game_index.append(game.index)
        num_bar.append(game.final_result[1])
    
    plt.plot(game_index, num_bar)
    plt.show()