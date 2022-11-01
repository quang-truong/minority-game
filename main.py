import utils
from experiments import vary_brain_size, vary_network

def main():
    T = 100
    N = 451
    # 1) Varying Brain Size per Minority Games by Yeung and Zhang
    # games = vary_brain_size(T = T, N = N, brain_size = 6, num_strategies = 4, seed = 123)
    # utils.plot_games_result(games, N, xlim = T, ylim_lower = 50, ylim_upper= 350)

    # 2) Varying Network Minority Game
    time_step = [i for i in range(T//5, T, T//5)]
    games = vary_network(T = T, N = N, brain_size = 6, num_strategies = 4, 
                        p = 0.005, seed = 64, directed = False, 
                        time_step = time_step)
    utils.plot_network_games_result(games, N, time_step, xlim = T, ylim_lower = 0, ylim_upper= N)


if __name__ == "__main__":
    main()