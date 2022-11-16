from time import time
import numpy as np
import matplotlib.pyplot as plt

from Games import Traditional_Minority_Game, Network_Minority_Game, Disconnected_Network_Minority_Game_10, Disconnected_Network_Minority_Game_4, Guru_Network_Minority_Game

def plot_games_result(game: Traditional_Minority_Game, ylim_lower: int, ylim_upper: int, fig_dir = None):
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
    if fig_dir:
        fig.savefig(fig_dir, dpi = 500)
    else:
        plt.show()
    plt.close(fig)

def plot_network_games_result(game: Network_Minority_Game or Disconnected_Network_Minority_Game_10 or Disconnected_Network_Minority_Game_4 or Guru_Network_Minority_Game, ylim_lower: int, ylim_upper: int, fig_dir = None):
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
    if fig_dir:
        fig.savefig(fig_dir, dpi = 500)
    else:
        plt.show()
    plt.close(fig)

def plot_coop_solo(game: Network_Minority_Game, fig_dir = None):
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
    if fig_dir:
        fig.savefig(fig_dir, dpi = 500)
    else:
        plt.show()
    plt.close(fig)

def plot_guru_solo(game: Guru_Network_Minority_Game, fig_dir = None):
    solo_winner_ratio = []
    guru_winner_ratio = []
    game_index = []

    fig, ax = plt.subplots()
    for i in range(game.T):
        solo_winner_ratio.append(game.arr_num_solo_winner[i]/game.num_solo_agent)
        guru_winner_ratio.append(game.arr_num_guru_winner[i]/game.num_guru_agent)
        game_index.append(i)

    solo_winner_ratio = np.array(solo_winner_ratio)
    guru_winner_ratio = np.array(guru_winner_ratio)
    game_index = np.array(game_index)
    
    solo_windows = rolling_window(solo_winner_ratio, 10)
    solo_rolling_avg = np.average(solo_windows, 1)
    solo_rolling_std = np.std(solo_windows, 1)

    guru_windows = rolling_window(guru_winner_ratio, 10)
    guru_rolling_avg = np.average(guru_windows, 1)
    guru_rolling_std = np.std(guru_windows, 1)

        
    ax.plot(game_index[:-9], solo_rolling_avg, color = "tab:blue", label = "solo")
    ax.fill_between(game_index[:-9], solo_rolling_avg - solo_rolling_std, solo_rolling_avg + solo_rolling_std, color = "tab:blue", alpha = 0.2)
    ax.plot(game_index[:-9], guru_rolling_avg, color = "tab:red", label = "guru")
    ax.fill_between(game_index[:-9], guru_rolling_avg - guru_rolling_std, guru_rolling_avg + guru_rolling_std, color = "tab:red", alpha = 0.2)
    ax.set_xlabel("Game")
    ax.set_ylabel("Winning Ratio (# winners / # ppl in that category)")
    for t in game.time_step:
        ax.axvline(t, linestyle='--', color='tab:grey')
    plt.legend()
    if fig_dir:
        fig.savefig(fig_dir, dpi = 500)
    else:
        plt.show()
    plt.close(fig)

def plot_disconnected_groups_10(game: Disconnected_Network_Minority_Game_10, fig_dir = None):
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
    if fig_dir:
        fig.savefig(fig_dir, dpi = 500)
    else:
        plt.show()
    plt.close(fig)

def plot_disconnected_groups_5(game: Disconnected_Network_Minority_Game_4, fig_dir = None):
    game_index = []

    winner_ratio = {
        1: [],
        64: [],
        128: [],
        256: [],
    }

    windows = {
        1: [],
        64: [],
        128: [],
        256: [],
    }

    rolling_avg = {
        1: [],
        64: [],
        128: [],
        256: [],
    }

    rolling_std = {
        1: [],
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
    if fig_dir:
        fig.savefig(fig_dir, dpi = 500)
    else:
        plt.show()
    plt.close(fig)

def compute_statistics(stats, time_step, colors, width_a = 1, width_b = 0.1, fig_dir = None):
    '''
        https://stackoverflow.com/questions/23461713/obtaining-values-used-in-boxplot-using-python-and-matplotlib
        https://stackoverflow.com/questions/16592222/matplotlib-group-boxplots
    '''
    fig, ax = plt.subplots()
    for key, _ in stats.items():
        for i in range(len(stats[key])):
            data = np.array(stats[key][i])

            avg = np.mean(data)
            median = np.median(data)
            upper_quartile = np.percentile(data, 75)
            lower_quartile = np.percentile(data, 25)

            iqr = upper_quartile - lower_quartile
            upper_whisker = data[data<=upper_quartile+1.5*iqr].max()
            lower_whisker = data[data>=lower_quartile-1.5*iqr].min()
            print("Group {0} - Time Step {1} - Statistics: \t Avg = {2:.2%} \t Min = {3:.2%} \t Q1 = {4:.2%} \t Median = {5:.2%} \t Q3 = {6:.2%} \t Max = {7:.2%} \t IQR = {8:.2%}".format(
                key, time_step[i], avg, lower_whisker, lower_quartile, median, upper_quartile, upper_whisker, iqr
            ))
    
    num_categories = len(stats)
    left_offsets = [-i/10 for i in range(width_a*(len(stats)//2), 0, -width_a)]
    right_offsets = [i/10 for i in range(width_a, width_a*(len(stats)//2 + 1), width_a)]
    if num_categories % 2 == 0:
        offsets = left_offsets + right_offsets
    else:
        offsets = left_offsets + [0] + right_offsets
    
    offsets = np.array(offsets)

    i = 0
    for key, _ in stats.items():
        bp_tmp = ax.boxplot(stats[key], positions=np.array(range(len(stats[key])))*num_categories + offsets[i], sym='', widths=width_b)
        set_box_color(bp_tmp, colors[key])
        i += 1

    # draw temporary lines and use them to create a legend
    for key, val in colors.items():
        plt.plot([], c=val, label=key)
    plt.legend()

    plt.xticks(range(0, len(time_step) * num_categories, num_categories), time_step)
    plt.xlim(-num_categories, len(time_step)*num_categories)
    ax.set_xlabel("Game")
    ax.set_ylabel("Winning Ratio")

    if fig_dir:
        fig.tight_layout()
        fig.set_size_inches(19.20, 10.80)
        fig.savefig(fig_dir, dpi = 500)
    else:
        plt.show()

def set_box_color(bp, color):
    '''
        https://stackoverflow.com/questions/16592222/matplotlib-group-boxplots
    '''
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

def rolling_window(a, window):
    '''
        https://rigtorp.se/2011/01/01/rolling-statistics-numpy.html
    '''
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
