from time import time
import numpy as np
import matplotlib.pyplot as plt

from Games import Traditional_Minority_Game, Network_Minority_Game, Disconnected_Network_Minority_Game_10, Disconnected_Network_Minority_Game_5

def plot_games_result(game: Traditional_Minority_Game, ylim_lower: int, ylim_upper: int):
    final_results = game.final_results
    total_agents = game.N

    game_index = []
    num_bar = [] 
    for i in range(game.T):
        game_index.append(i)
        num_bar.append(final_results[i][1])
    
    game_index = np.array(game_index)
    num_bar = np.array(num_bar)

    fig, ax = plt.subplots()
    ax.plot(game_index, num_bar)
    ax.set_xlabel("Game")
    ax.set_ylabel("# of Attendees")
    ax.set_xlim(0, game.T)
    ax.set_ylim(ylim_lower, ylim_upper)
    ax.axhline(total_agents//2, linestyle='--', color='tab:orange')
    plt.show()

def plot_network_games_result(game: Network_Minority_Game or Disconnected_Network_Minority_Game_10 or Disconnected_Network_Minority_Game_5, ylim_lower: int, ylim_upper: int):
    final_results = game.final_results
    total_agent = game.N

    game_index = []
    num_bar = [] 
    for i in range(game.T):
        game_index.append(i)
        num_bar.append(final_results[i][1])

    game_index = np.array(game_index)
    num_bar = np.array(num_bar)

    fig, ax = plt.subplots()
    ax.plot(game_index, num_bar)
    ax.set_xlabel("Game")
    ax.set_ylabel("# of Attendees")
    ax.set_xlim(0, game.T)
    ax.set_ylim(ylim_lower, ylim_upper)
    ax.axhline(total_agent*game.threshold, linestyle='--', color='tab:orange')
    for t in game.time_step:
        ax.axvline(t, linestyle='--', color='tab:grey')
    plt.show()

def plot_coop_solo(game: Network_Minority_Game):
    solo_winner_ratio = []
    coop_winner_ratio = []
    game_index = []

    fig, ax = plt.subplots()
    for i in range(game.T):
        solo_winner_ratio.append(game.arr_num_solo_winner[i]/game.num_solo_agent)
        coop_winner_ratio.append(game.arr_num_coop_winner[i]/game.num_coop_agent)
        game_index.append(i)
    
    solo_winner_ratio = np.array(solo_winner_ratio)
    coop_winner_ratio = np.array(coop_winner_ratio)
    game_index = np.array(game_index)
    
    solo_windows = rolling_window(solo_winner_ratio, 10)
    solo_rolling_avg = np.average(solo_windows, 1)
    solo_rolling_std = np.std(solo_windows, 1)

    coop_windows = rolling_window(coop_winner_ratio, 10)
    coop_rolling_avg = np.average(coop_windows, 1)
    coop_rolling_std = np.std(coop_windows, 1)

        
    ax.plot(game_index[:-9], solo_rolling_avg, color = "tab:blue", label = "solo")
    ax.fill_between(game_index[:-9], solo_rolling_avg - solo_rolling_std, solo_rolling_avg + solo_rolling_std, color = "tab:blue", alpha = 0.2)
    ax.plot(game_index[:-9], coop_rolling_avg, color = "tab:orange", label = "coop")
    ax.fill_between(game_index[:-9], coop_rolling_avg - coop_rolling_std, coop_rolling_avg + coop_rolling_std, color = "tab:orange", alpha = 0.2)
    ax.set_xlabel("Game")
    ax.set_ylabel("Winning Ratio (# winners / # ppl in that category)")
    for t in game.time_step:
        ax.axvline(t, linestyle='--', color='tab:grey')
    plt.legend()
    plt.show()

def plot_disconnected_groups_10(game: Disconnected_Network_Minority_Game_10):
    game_index = []

    winner_ratio = {
        1: [],
        10: [],
        20: [],
        30: [],
        40: [],
        50: [],
        60: [],
        70: [],
        80: [],
        90: []
    }

    windows = {
        1: [],
        10: [],
        20: [],
        30: [],
        40: [],
        50: [],
        60: [],
        70: [],
        80: [],
        90: []
    }

    rolling_avg = {
        1: [],
        10: [],
        20: [],
        30: [],
        40: [],
        50: [],
        60: [],
        70: [],
        80: [],
        90: []
    }

    rolling_std = {
        1: [],
        10: [],
        20: [],
        30: [],
        40: [],
        50: [],
        60: [],
        70: [],
        80: [],
        90: []
    }

    fig, ax = plt.subplots()
    for k in winner_ratio.keys():
        for t in range(game.T):
            winner_ratio[k].append(game.num_winner_by_group[k][t]/k)
    
    for i in range(game.T):
        game_index.append(i)
    
    game_index = np.array(game_index)
    for k in winner_ratio.keys():
        winner_ratio[k] = np.array(winner_ratio[k])
        windows[k] = rolling_window(winner_ratio[k], 10)
        rolling_avg[k] = np.average(windows[k], 1)
        rolling_std[k] = np.std(windows[k], 1)
    
    for k in winner_ratio.keys():
        ax.plot(game_index[:-9], rolling_avg[k], color = game.colors[k], label = str(k))
        ax.fill_between(game_index[:-9], rolling_avg[k] - rolling_std[k], rolling_avg[k] + rolling_std[k], color = game.colors[k], alpha = 0.2)
    
    ax.set_xlabel("Game")
    ax.set_ylabel("Winning Ratio (# winners / # ppl in that category)")
    for t in game.time_step:
        ax.axvline(t, linestyle='--', color='tab:grey')
    plt.legend()
    plt.show()

def plot_disconnected_groups_5(game: Disconnected_Network_Minority_Game_5):
    game_index = []

    winner_ratio = {
        1: [],
        32: [],
        64: [],
        128: [],
        256: [],
    }

    windows = {
        1: [],
        32: [],
        64: [],
        128: [],
        256: [],
    }

    rolling_avg = {
        1: [],
        32: [],
        64: [],
        128: [],
        256: [],
    }

    rolling_std = {
        1: [],
        32: [],
        64: [],
        128: [],
        256: [],
    }

    fig, ax = plt.subplots()
    for k in winner_ratio.keys():
        for t in range(game.T):
            winner_ratio[k].append(game.num_winner_by_group[k][t]/k)
    
    for i in range(game.T):
        game_index.append(i)
    
    game_index = np.array(game_index)
    for k in winner_ratio.keys():
        winner_ratio[k] = np.array(winner_ratio[k])
        windows[k] = rolling_window(winner_ratio[k], 10)
        rolling_avg[k] = np.average(windows[k], 1)
        rolling_std[k] = np.std(windows[k], 1)
    
    for k in winner_ratio.keys():
        ax.plot(game_index[:-9], rolling_avg[k], color = game.colors[k], label = str(k))
        ax.fill_between(game_index[:-9], rolling_avg[k] - rolling_std[k], rolling_avg[k] + rolling_std[k], color = game.colors[k], alpha = 0.2)
    
    ax.set_xlabel("Game")
    ax.set_ylabel("Winning Ratio (# winners / # ppl in that category)")
    for t in game.time_step:
        ax.axvline(t, linestyle='--', color='tab:grey')
    plt.legend()
    plt.show()

def rolling_window(a, window):
    '''
        https://rigtorp.se/2011/01/01/rolling-statistics-numpy.html
    '''
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
