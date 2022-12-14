import numpy as np

from Games import Traditional_Minority_Game, Network_Minority_Game, Disconnected_Network_Minority_Game_10, Disconnected_Network_Minority_Game_4, Guru_Network_Minority_Game
from Agent import Agent

from typing import List
import random

def vary_brain_size(T: int, N: int, brain_size: int, num_strategies: int, seed: int):
    np.random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

    game = Traditional_Minority_Game(T, N, agents, past_games = past_games, threshold = 0.5, time_limit= None)
    game.start()
    return game
    
def propagate_strategies_network(aggregate_mode: str, T: int, N: int, brain_size: int, num_strategies: int, p: float, seed: int, time_step : List[int], fig_dir = None):
    np.random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies, aggregate_mode= aggregate_mode) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

    game = Network_Minority_Game(T, N, agents, past_games = past_games, 
                                threshold = 0.5, p = p,
                                time_step = time_step,
                                time_limit= None, seed = seed)
    game.network.plot_graph(fig_dir)
    game.start()
    return game

def propagate_strategies_guru_network(T: int, N: int, brain_size: int, num_strategies: int, p: float, seed: int, time_step : List[int], fig_dir = None):
    np.random.seed(seed)
    random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies) for i in range(N)]
    guru_idx = random.sample([i for i in range(N)], N//5)
    for i in guru_idx:
        agents[i].guru = True
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

    game = Guru_Network_Minority_Game(T, N, agents, past_games = past_games, 
                                threshold = 0.5, p = p,
                                time_step = time_step,
                                time_limit= None, seed = seed)
    game.network.plot_graph(fig_dir)
    game.start()
    return game

def propagate_strategies_disconnected_network_10(aggregate_mode: str, T: int, N: int, brain_size: int, num_strategies: int, seed: int, time_step : List[int], fig_dir = None):
    np.random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies, aggregate_mode= aggregate_mode) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

    game = Disconnected_Network_Minority_Game_10(T, N, agents, past_games = past_games, 
                                threshold = 0.5,
                                time_step = time_step,
                                time_limit= None, seed = seed)
    game.network.plot_graph(fig_dir)
    game.start()
    return game

def propagate_strategies_disconnected_network_4(aggregate_mode: str, T: int, N: int, brain_size: int, num_strategies: int, seed: int, time_step : List[int], fig_dir = None):
    np.random.seed(seed)
    agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies, aggregate_mode= aggregate_mode) for i in range(N)]
    past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

    game = Disconnected_Network_Minority_Game_4(T, N, agents, past_games = past_games, 
                                threshold = 0.5,
                                time_step = time_step,
                                time_limit= None, seed = seed)
    game.network.plot_graph(fig_dir)
    game.start()
    return game

def propagate_strategies_network_100_times(aggregate_mode: str, T: int, N: int, brain_size: int, num_strategies: int, p: float, seed: int, time_step : List[int]):
    np.random.seed(seed)

    stats = {
        "solo": [],
        "coop": []
    }

    for t in time_step:
        stats["solo"].append([])
        stats["coop"].append([])

    for i in range(100):
        agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies, aggregate_mode = aggregate_mode) for i in range(N)]
        past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

        game = Network_Minority_Game(T, N, agents, past_games = past_games, 
                                    threshold = 0.5, p = p,
                                    time_step = time_step,
                                    time_limit= None, seed = seed)
        game.start()
        for i in range(len(time_step)):
            stats["solo"][i].append(np.mean(game.arr_num_solo_winner[time_step[i]-5:time_step[i]+5])/game.num_solo_agent)
            stats["coop"][i].append(np.mean(game.arr_num_coop_winner[time_step[i]-5:time_step[i]+5])/game.num_coop_agent)

    return game, stats

def propagate_strategies_disconnected_network_10_100_times(aggregate_mode: str, T: int, N: int, brain_size: int, num_strategies: int, seed: int, time_step : List[int], fig_dir = None):
    np.random.seed(seed)

    stats = {
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

    for t in time_step:
        stats[1].append([])
        stats[10].append([])
        stats[20].append([])
        stats[30].append([])
        stats[40].append([])
        stats[50].append([])
        stats[60].append([])
        stats[70].append([])
        stats[80].append([])
        stats[90].append([])

    for i in range(100):
        agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies, aggregate_mode= aggregate_mode) for i in range(N)]
        past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

        game = Disconnected_Network_Minority_Game_10(T, N, agents, past_games = past_games, 
                                    threshold = 0.5,
                                    time_step = time_step,
                                    time_limit= None, seed = seed)
        game.start()
        for i in range(len(time_step)):
            stats[1][i].append(np.mean(game.num_winner_by_group[1][time_step[i]-5:time_step[i]+5])/1)
            stats[10][i].append(np.mean(game.num_winner_by_group[10][time_step[i]-5:time_step[i]+5])/10)
            stats[20][i].append(np.mean(game.num_winner_by_group[20][time_step[i]-5:time_step[i]+5])/20)
            stats[30][i].append(np.mean(game.num_winner_by_group[30][time_step[i]-5:time_step[i]+5])/30)
            stats[40][i].append(np.mean(game.num_winner_by_group[40][time_step[i]-5:time_step[i]+5])/40)
            stats[50][i].append(np.mean(game.num_winner_by_group[50][time_step[i]-5:time_step[i]+5])/50)
            stats[60][i].append(np.mean(game.num_winner_by_group[60][time_step[i]-5:time_step[i]+5])/60)
            stats[70][i].append(np.mean(game.num_winner_by_group[70][time_step[i]-5:time_step[i]+5])/70)
            stats[80][i].append(np.mean(game.num_winner_by_group[80][time_step[i]-5:time_step[i]+5])/80)
            stats[90][i].append(np.mean(game.num_winner_by_group[90][time_step[i]-5:time_step[i]+5])/90)
    return game, stats

def propagate_strategies_disconnected_network_4_100_times(aggregate_mode: str, T: int, N: int, brain_size: int, num_strategies: int, seed: int, time_step : List[int], fig_dir = None):
    np.random.seed(seed)

    stats = {
        1: [],
        64: [],
        128: [],
        256: []
    }

    for t in time_step:
        stats[1].append([])
        stats[64].append([])
        stats[128].append([])
        stats[256].append([])

    for i in range(100):
        agents = [Agent(i, past_decisions= None, brain_size = brain_size, num_strategies= num_strategies, aggregate_mode= aggregate_mode) for i in range(N)]
        past_games = np.binary_repr(np.random.randint(0, 2**8), width = 8)         # Assume there is already 8 games played in the past

        game = Disconnected_Network_Minority_Game_4(T, N, agents, past_games = past_games, 
                                    threshold = 0.5,
                                    time_step = time_step,
                                    time_limit= None, seed = seed)
        game.start()
        for i in range(len(time_step)):
            stats[1][i].append(np.mean(game.num_winner_by_group[1][time_step[i]-5:time_step[i]+5])/1)
            stats[64][i].append(np.mean(game.num_winner_by_group[64][time_step[i]-5:time_step[i]+5])/64)
            stats[128][i].append(np.mean(game.num_winner_by_group[128][time_step[i]-5:time_step[i]+5])/128)
            stats[256][i].append(np.mean(game.num_winner_by_group[256][time_step[i]-5:time_step[i]+5])/256)
    return game, stats