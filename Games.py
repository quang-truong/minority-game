import numpy as np

from Agent import Agent
from Network import Network

from typing import List

class Single_Stage_Game:
    def __init__(self, index: int, N: int, agents: List[Agent], past_games: str, threshold = 0.6, time_limit = None):
        self.index = index
        self.N = N
        self.agents = agents
        self.past_games = past_games            # a binary string
        self.threshold = threshold
        self.time_limit = time_limit
        self.final_result = None                # 'Bar' or 'Home'

    def start(self):
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
        self.final_result = (res, num_of_attendants, num_of_stay_home)

    def update(self):
        for agent in self.agents:
            agent.update(self.final_result[0], self.past_games)


class Single_Stage_Network_Game:
    def __init__(self,  index: int, N: int, agents: List[Agent], past_games: str, threshold: int, p: float, directed: bool, time_limit = None, seed = 123):
        self.index = index
        self.N = N
        self.agents = agents
        self.past_games = past_games            # a binary string
        self.threshold = threshold
        self.time_limit = time_limit
        self.final_result = None                # 'Bar' or 'Home'
        self.G = Network(self.agents, p, directed, seed)

    def start(self):
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
        self.final_result = (res, num_of_attendants, num_of_stay_home)

    def update(self):
        for agent in self.agents:
            agent.update(self.final_result[0], self.past_games)