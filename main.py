import utils
from experiments import vary_brain_size, propagate_all_strategies_network, propagate_all_strategies_disconnected_network_10, \
        propagate_all_strategies_disconnected_network_5, propagate_best_strategies_network, propagate_best_strategies_disconnected_network_10, \
        propagate_best_strategies_disconnected_network_5

def main():
    T = 500
    N = 481
    # 1) Varying Brain Size per Minority Games by Yeung and Zhang
    game = vary_brain_size(T = T, N = N, brain_size = 8, num_strategies = 4, seed = 123)
    utils.plot_games_result(game, ylim_lower = 0, ylim_upper= N, fig_dir= 'figures/exp_1_game_result.png')

    # 2) Propagate All Strategies - Network Minority Game
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_all_strategies_network(T = T, N = N, brain_size = 8, num_strategies = 4, 
                        p = 0.005, seed = 64, time_step = time_step, fig_dir= 'figures/exp2_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= N, fig_dir= 'figures/exp2_game_result.png')
    utils.plot_coop_solo(game, fig_dir='figures/exp2_winning_ratio.png')

    # 3) Propagate All Strategies - Disconnected Minority Game (10 Groups)
    # If the below code doesn't work, probability to create edges in Erdos-Renyi graph is low. 
    # p = 0.5 guarantees to create a connected sub-graph, but the trade-off is runtime.
    # Try to change seed, or increase p in Network.py
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_all_strategies_disconnected_network_10(T = T, N = 451, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step, fig_dir= 'figures/exp3_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= N, fig_dir= 'figures/exp3_game_result.png')
    utils.plot_disconnected_groups_10(game, fig_dir='figures/exp3_winning_ratio.png')

    # 4) Propagate All Strategies - Disconnected Minority Game (5 Groups)
    # If the below code doesn't work, probability to create edges in Erdos-Renyi graph is low. 
    # p = 0.5 guarantees to create a connected sub-graph, but the trade-off is runtime.
    # Try to change seed, or increase p in Network.py
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_all_strategies_disconnected_network_5(T = T, N = 481, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step, fig_dir= 'figures/exp4_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= N, fig_dir= 'figures/exp4_game_result.png')
    utils.plot_disconnected_groups_5(game, fig_dir='figures/exp4_winning_ratio.png')

    # 5) Propagate Best Strategies - Network Minority Game
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_best_strategies_network(T = T, N = N, brain_size = 8, num_strategies = 4, 
                        p = 0.005, seed = 64, time_step = time_step, fig_dir= 'figures/exp5_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= N, fig_dir= 'figures/exp5_game_result.png')
    utils.plot_coop_solo(game, fig_dir='figures/exp5_winning_ratio.png')

    # 6) Propagate Best Strategies - Disconnected Minority Game (10 Groups)
    # If the below code doesn't work, probability to create edges in Erdos-Renyi graph is low. 
    # p = 0.5 guarantees to create a connected sub-graph, but the trade-off is runtime.
    # Try to change seed, or increase p in Network.py
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_best_strategies_disconnected_network_10(T = T, N = 451, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step, fig_dir= 'figures/exp6_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= N, fig_dir= 'figures/exp6_game_result.png')
    utils.plot_disconnected_groups_10(game, fig_dir= 'figures/exp6_winning_ratio.png')

    # 7) Propagate Best Strategies - Disconnected Minority Game (5 Groups)
    # If the below code doesn't work, probability to create edges in Erdos-Renyi graph is low. 
    # p = 0.5 guarantees to create a connected sub-graph, but the trade-off is runtime.
    # Try to change seed, or increase p in Network.py
    time_step = [i for i in range(T//5, T, T//5)]
    game = propagate_best_strategies_disconnected_network_5(T = T, N = 481, brain_size = 8, num_strategies = 4, 
                        seed = 64, time_step = time_step, fig_dir= 'figures/exp7_network_plot.png')
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= N, fig_dir= 'figures/exp7_game_result.png')
    utils.plot_disconnected_groups_5(game, fig_dir= 'figures/exp7_winning_ratio.png')

if __name__ == "__main__":
    main()