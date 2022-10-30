import numpy as np

from Strategies import random_strategy

class Agent:
    def __init__(self, index: int, past_decisions: str, brain_size = 4, num_strategies = 5):
        self.index = index
        self.past_decisions = past_decisions                        # (True or False, Win or Lose, Strategies used)
        self.brain_size = brain_size                                # Number of Bits in Brain (M)
        self.num_strategies = num_strategies
        self.strategies = random_strategy(self.num_strategies, self.brain_size)
        self.virtual_point = np.zeros(num_strategies)                        # merit point for each strategy
        self.best_strategy = self.strategies[np.argmax(self.virtual_point)]
        self.score = 0

    def filter_signal(self, signal: str):
        return int(signal[-self.brain_size:], 2)
    
    def make_decision(self, signal: str):
        filtered_signal = self.filter_signal(signal)
        decision = int(self.best_strategy[filtered_signal])
        return 'Bar' if decision else 'Home'

    def update(self, result: int, signal: str):
        result = 1 if result == 'Bar' else 0
        filtered_signal = self.filter_signal(signal)
        if self.best_strategy[filtered_signal] == result:                       # Update Score based on Result
            self.score += 1
        else:
            self.score -= 1
        for i in range(self.num_strategies):                                    # Calculate next best Strategy
            if int(self.strategies[i][filtered_signal]) == result:
                self.virtual_point[i] += 1
            else:
                self.virtual_point[i] -= 1
        self.best_strategy = self.strategies[np.argmax(self.virtual_point)]
