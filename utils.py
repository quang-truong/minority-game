from time import time
import numpy as np
import matplotlib.pyplot as plt

def plot_games_result(games, total_agents, xlim, ylim_lower, ylim_upper):
    game_index = []
    num_bar = [] 
    for i in range(len(games)):
        game_index.append(i)
        num_bar.append(games[i][1])
    
    fig, ax = plt.subplots()
    ax.plot(game_index, num_bar)
    ax.set_xlabel("Game")
    ax.set_ylabel("# of Attendees")
    ax.set_xlim(0, xlim)
    ax.set_ylim(ylim_lower, ylim_upper)
    ax.axhline(total_agents//2, linestyle='--', color='tab:orange')
    plt.show()

def plot_network_games_result(games, total_agents, time_step, xlim, ylim_lower, ylim_upper):
    game_index = []
    num_bar = [] 
    for i in range(len(games)):
        game_index.append(i)
        num_bar.append(games[i][1])
    fig, ax = plt.subplots()
    ax.plot(game_index, num_bar)
    ax.set_xlabel("Game")
    ax.set_ylabel("# of Attendees")
    ax.set_xlim(0, xlim)
    ax.set_ylim(ylim_lower, ylim_upper)
    ax.axhline(total_agents//2, linestyle='--', color='tab:orange')
    for t in time_step:
        ax.axvline(t, linestyle='--', color='tab:grey')
    plt.show()