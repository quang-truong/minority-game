import utils
from experiments import vary_brain_size, vary_network

def main():
    T = 500
    N = 465
    # 1) Varying Brain Size per Minority Games by Yeung and Zhang
    game = vary_brain_size(T = T, N = N, brain_size = 8, num_strategies = 4, seed = 123)
    utils.plot_games_result(game, ylim_lower = 0, ylim_upper= N)

    # 2) Varying Network Minority Game
    time_step = [i for i in range(T//5, T, T//5)]
    game = vary_network(T = T, N = N, brain_size = 8, num_strategies = 4, 
                        p = 0.005, seed = 64, directed = False, 
                        time_step = time_step)
    utils.plot_network_games_result(game, ylim_lower = 0, ylim_upper= N)
    utils.plot_coop_solo(game)

if __name__ == "__main__":
    main()