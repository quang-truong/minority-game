from Games import Single_Stage_Game
from Agent import Agent

def main():
    N = 100
    agents = [Agent(i, past_decisions= None, past_games= None) for i in range(N)]
    game = Single_Stage_Game(0, N, agents, past_games= None, threshold = 0.5, time_limit= None)
    game.start()
    print(game.final_result)


if __name__ == "__main__":
    main()