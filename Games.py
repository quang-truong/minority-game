import numpy as np

class Single_Stage_Game:
    def __init__(self, index, N, agents, past_games, threshold = 0.6, time_limit = None):
        self.index = index
        self.N = N
        self.agents = agents
        self.past_games = past_games
        self.threshold = threshold
        self.time_limit = time_limit
        self.final_result = None                # 'Bar' or 'Home'

    def start(self):
        res = None
        num_of_attendants = 0
        num_of_stay_home = 0
        for agent in self.agents:
            decision = agent.make_decision()
            if (decision == 'Bar'): num_of_attendants += 1
            else: num_of_stay_home += 1
        if (self.threshold != None):                # El Farol threshold
            res = 'Bar' if num_of_attendants / (num_of_attendants + num_of_stay_home) < self.threshold else 'Home'
        else:
            res = 'Bar' if num_of_attendants < (num_of_attendants + num_of_stay_home) else 'Home'
        self.final_result = (res, num_of_attendants, num_of_stay_home)

