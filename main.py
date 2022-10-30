import utils
from experiments import vary_brain_size, vary_network

def main():
    # 1) Varying Brain Size per Minority Games by Yeung and Zhang
    # games = vary_brain_size(T = 1000, N = 1001, brain_size = 8, num_strategies = 4, seed = 123)
    # utils.plot_games_result(games, xlim = 1001, ylim_lower = 100, ylim_upper= 900)

    # 2) Varying Network
    games = vary_network(T = 1, N = 31, brain_size = 6, num_strategies = 4, p = 0.05, seed = 123, directed = False)
    games[0].G.plot_graph()


if __name__ == "__main__":
    main()