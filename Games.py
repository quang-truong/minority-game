import numpy as np

from Agent import Agent
from Network import Network

from typing import List, Tuple

class Traditional_Minority_Game():
    def __init__(self, T: int, N: int, agents: List[Agent], past_games: str, threshold = 0.6, time_limit = None):
        self.T = T                              # number of games
        self.N = N                              # number of agents
        self.agents = agents
        self.past_games = past_games            # a binary string
        self.threshold = threshold
        self.time_limit = time_limit
        self.final_results = []               

    def start(self):
        for _ in range(self.T):
            res = self.iterate()
            self.final_results.append(res)
            self.update(res)
            self.past_games += '1' if res[0] == 'Bar' else '0'

    def iterate(self):
        res = None
        num_of_attendants = 0
        num_of_stay_home = 0
        for agent in self.agents:
            decision = agent.make_decision(self.past_games)
            if (decision == 'Bar'): num_of_attendants += 1
            else: num_of_stay_home += 1
        if (self.threshold != None):                # El Farol threshold
            res = 'Bar' if num_of_attendants / (num_of_attendants + num_of_stay_home) < self.threshold else 'Home'
        else:
            res = 'Bar' if num_of_attendants < num_of_stay_home else 'Home'
        return (res, num_of_attendants, num_of_stay_home)

    def update(self, result: Tuple[str, int, int]):
        for agent in self.agents:
            agent.update(result[0], self.past_games)

    def get_final_results(self): return self.final_results


class Network_Minority_Game(Traditional_Minority_Game):
    def __init__(self, T: int, N: int, agents: List[Agent], past_games: str, threshold: int, p: float, directed: bool, time_limit = None, seed = 123):
        super().__init__(T, N, agents, past_games, threshold, time_limit)
        self.G = Network(self.agents, p, directed, seed)