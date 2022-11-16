import numpy as np

from Strategies import random_strategy

class Agent():
    def __init__(self, index: int, past_decisions: str, brain_size = 4, num_strategies = 5, aggregate_mode = "all", guru = False):
        self.index = index
        self.past_decisions = past_decisions                        # (True or False, Win or Lose, Strategies used)
        self.brain_size = brain_size                                # Number of Bits in Brain (M)
        self.num_strategies = num_strategies
        self.strategies = random_strategy(self.num_strategies, self.brain_size)
        self.virtual_point = np.zeros(num_strategies)                        # merit point for each strategy
        self.best_strategy = self.strategies[np.argmax(self.virtual_point)]
        self.score = 0

        # network attributes
        self.neighbors = []
        self.aggregated_strategies = None
        self.aggregated_virtual_point = None
        self.aggregate_mode = aggregate_mode

        # guru attribute
        self.guru = guru

    def filter_signal(self, signal: str):
        return int(signal[-self.brain_size:], 2)
    
    def make_decision(self, signal: str):
        filtered_signal = self.filter_signal(signal)
        decision = int(self.best_strategy[filtered_signal])
        return 'Bar' if decision else 'Home'
    
    def make_rp_decision(self, signal: str):
        filtered_signal = self.filter_signal(signal)
        unique, counts = np.unique(self.strategies[:, filtered_signal], return_counts= True)
        tmp = dict(zip(unique, counts))
        decision = None
        if len(tmp) == 1:
            decision = list(tmp.keys())[0]
        else:
            if (tmp[0] <= tmp[1]):
                decision = 0
            else:
                decision = 1
        return 'Bar' if decision else 'Home'

    def update(self, result: int, signal: str):
        is_winner = False
        result = 1 if result == 'Bar' else 0
        filtered_signal = self.filter_signal(signal)
        if (self.guru):
            unique, counts = np.unique(self.strategies[:, filtered_signal], return_counts= True)
            tmp = dict(zip(unique, counts))
            decision = None
            if len(tmp) == 1:
                decision = list(tmp.keys())[0]
            else:
                if (tmp[0] <= tmp[1]):
                    decision = 0
                else:
                    decision = 1
            if (decision == result):
                self.score += 1
                is_winner = True
            else:
                self.score -= 1
        else:
            if self.best_strategy[filtered_signal] == result:                       # Update Score based on Result
                self.score += 1
                is_winner = True
            else:
                self.score -= 1
        for i in range(self.num_strategies):                                    # Calculate next best Strategy
            if int(self.strategies[i][filtered_signal]) == result:
                self.virtual_point[i] += 1
            else:
                self.virtual_point[i] -= 1
        self.best_strategy = self.strategies[np.argmax(self.virtual_point)]
        return is_winner
