import utils
from experiments import *

def main():
    T = 500
    # 1) Varying Brain Size per Minority Games by Yeung and Zhang
    print("Experiment 1:")
    game = vary_brain_size(T = T, N = 449, brain_size = 8, num_strategies = 4, seed = 123)
    utils.plot_games_result(game, ylim_lower = 0, ylim_upper= 449, fig_dir= 'figures/exp1_game_result (M=8).png')

    # 2) Propagate All Strategies - Network Minority Game
    print("Experiment 2:")
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_strategies_network(aggregate_mode = "all", T = T, N = 449, brain_size = 8, num_strategies = 4, 
                        p = 0.0025, seed = 64, time_step = time_step, fig_dir= 'figures/exp2_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= 449, fig_dir= 'figures/exp2_game_result.png')
    utils.plot_coop_solo(game, fig_dir='figures/exp2_winning_ratio.png')

    # 3) Propagate All Strategies - Disconnected Minority Game (10 Groups)
    # If the below code doesn't work, probability to create edges in Erdos-Renyi graph is low. 
    # p = 0.5 guarantees to create a connected sub-graph, but the trade-off is runtime.
    # Try to change seed, or increase p in Network.py
    print("Experiment 3:")
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_strategies_disconnected_network_10(aggregate_mode = "all", T = T, N = 451, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step, fig_dir= 'figures/exp3_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= 451, fig_dir= 'figures/exp3_game_result.png')
    utils.plot_disconnected_groups_10(game, fig_dir='figures/exp3_winning_ratio.png')

    # 4) Propagate All Strategies - Disconnected Minority Game (4 Groups)
    # If the below code doesn't work, probability to create edges in Erdos-Renyi graph is low. 
    # p = 0.5 guarantees to create a connected sub-graph, but the trade-off is runtime.
    # Try to change seed, or increase p in Network.py
    print("Experiment 4:")
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_strategies_disconnected_network_4(aggregate_mode = "all", T = T, N = 449, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step, fig_dir= 'figures/exp4_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= 449, fig_dir= 'figures/exp4_game_result.png')
    utils.plot_disconnected_groups_5(game, fig_dir='figures/exp4_winning_ratio.png')

    # 5) Propagate Best Strategies - Network Minority Game
    print("Experiment 5:")
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_strategies_network(aggregate_mode = "best", T = T, N = 449, brain_size = 8, num_strategies = 4, 
                        p = 0.0025, seed = 64, time_step = time_step, fig_dir= 'figures/exp5_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= 449, fig_dir= 'figures/exp5_game_result.png')
    utils.plot_coop_solo(game, fig_dir='figures/exp5_winning_ratio.png')

    # 6) Propagate Best Strategies - Disconnected Minority Game (10 Groups)
    # If the below code doesn't work, probability to create edges in Erdos-Renyi graph is low. 
    # p = 0.5 guarantees to create a connected sub-graph, but the trade-off is runtime.
    # Try to change seed, or increase p in Network.py
    print("Experiment 6:")
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_strategies_disconnected_network_10(aggregate_mode = "best", T = T, N = 451, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step, fig_dir= 'figures/exp6_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= 451, fig_dir= 'figures/exp6_game_result.png')
    utils.plot_disconnected_groups_10(game, fig_dir= 'figures/exp6_winning_ratio.png')

    # 7) Propagate Best Strategies - Disconnected Minority Game (4 Groups)
    # If the below code doesn't work, probability to create edges in Erdos-Renyi graph is low. 
    # p = 0.5 guarantees to create a connected sub-graph, but the trade-off is runtime.
    # Try to change seed, or increase p in Network.py
    print("Experiment 7:")
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_strategies_disconnected_network_4(aggregate_mode = "best", T = T, N = 449, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step, fig_dir= 'figures/exp7_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= 449, fig_dir= 'figures/exp7_game_result.png')
    utils.plot_disconnected_groups_5(game, fig_dir= 'figures/exp7_winning_ratio.png')

    # 8) Propagate All Strategies 100 times - Network Minority Game     (**Take long time**)
    print("Experiment 8:")
    time_step = [i for i in range(T//5, T, T//5)]
    game, stats = propagate_strategies_network_100_times(aggregate_mode = "all", T = T, N = 449, brain_size = 8, num_strategies = 4, 
                        p = 0.0025, seed = 64, time_step = time_step)
    utils.compute_statistics(stats, game.time_step, colors = {'solo': 'tab:blue', 'coop':'tab:orange'}, width_a = 4, width_b = 0.6, fig_dir= 'figures/exp8_boxplot.png')

    # 9) Propagate Best Strategies 100 times - Network Minority Game    (**Take long time**)
    print("Experiment 9:")
    time_step = [i for i in range(T//5, T, T//5)]
    game, stats = propagate_strategies_network_100_times(aggregate_mode = "best", T = T, N = 449, brain_size = 8, num_strategies = 4, 
                        p = 0.0025, seed = 64, time_step = time_step)
    utils.compute_statistics(stats, game.time_step, colors = {'solo': 'tab:blue', 'coop':'tab:orange'}, width_a = 4, width_b = 0.6, fig_dir= 'figures/exp9_boxplot.png')

    # 10) Propagate All Strategies 100 times - Disconnected Minority Game (10 Groups)   (**Take long time**)
    print("Experiment 10:")
    time_step = [i for i in range(T//5, T, T//5)]
    game, stats = propagate_strategies_disconnected_network_10_100_times(aggregate_mode = "all", T = T, N = 451, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step)
    utils.compute_statistics(stats, game.time_step, colors = game.colors, width_a = 6, width_b = 0.5, fig_dir= 'figures/exp10_boxplot.png')

    # 11) Propagate Best Strategies 100 times - Disconnected Minority Game (10 Groups)  (**Take long time**)
    print("Experiment 11:")
    time_step = [i for i in range(T//5, T, T//5)]
    game, stats = propagate_strategies_disconnected_network_10_100_times(aggregate_mode = "best", T = T, N = 451, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step)
    utils.compute_statistics(stats, game.time_step, colors = game.colors, width_a = 6, width_b = 0.5, fig_dir= 'figures/exp11_boxplot.png')

    # 12) Propagate All Strategies 100 times - Disconnected Minority Game (4 Groups)   (**Take long time**)
    print("Experiment 12:")
    time_step = [i for i in range(T//5, T, T//5)]
    game, stats = propagate_strategies_disconnected_network_4_100_times(aggregate_mode = "all", T = T, N = 449, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step)
    utils.compute_statistics(stats, game.time_step, colors = game.colors, width_a = 6, width_b = 0.5, fig_dir= 'figures/exp12_boxplot.png')

    # 13) Propagate Best Strategies 100 times - Disconnected Minority Game (4 Groups)  (**Take long time**)
    print("Experiment 13:")
    time_step = [i for i in range(T//5, T, T//5)]
    game, stats = propagate_strategies_disconnected_network_4_100_times(aggregate_mode = "best", T = T, N = 449, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step)
    utils.compute_statistics(stats, game.time_step, colors = game.colors, width_a = 6, width_b = 0.5, fig_dir= 'figures/exp13_boxplot.png')

    # 14) Propagate Guru Network        (Not included in the report)
    print("Experiment 14:")
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_strategies_guru_network(T = T, N = 449, brain_size = 8, num_strategies = 4, 
                        p = 0.0025, seed = 64, time_step = time_step, fig_dir= 'figures/exp14_network_plot (p=0.0025).png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= 449, fig_dir= 'figures/exp14_game_result (p=0.0025).png')
    utils.plot_guru_solo(game, fig_dir='figures/exp14_winning_ratio (p=0.0025).png')
if __name__ == "__main__":
    main()