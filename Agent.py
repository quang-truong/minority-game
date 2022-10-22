from Strategies import random_strategy

class Agent:
    def __init__(self, index, past_decisions, past_games):
        self.index = index
        self.past_decisions = past_decisions                # (True or False, Win or Lose, Strategies used)
        self.past_games = past_games                        # Past history of games

    
    def make_decision(self):
        decision = random_strategy()
        return 'Bar' if decision else 'Home'