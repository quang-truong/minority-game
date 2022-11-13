import numpy as np
import networkx as nx

from Agent import Agent
from Network import Network, Disconnected_Network_10, Disconnected_Network_5
from Aggregation import aggregate_all_neighbor_strategies, aggregate_best_neighbor_strategies

from typing import List, Tuple

class Traditional_Minority_Game():
    def __init__(self, T: int, N: int, agents: List[Agent], past_games: str, threshold = 0.6, time_limit = None):
        self.T = T                              # number of games
        self.N = N                              # number of agents
        self.agents = agents
        self.past_games = past_games            # a binary string
        self.threshold = threshold
        self.time_limit = time_limit
        self.final_results = []                 # ('Bar' or 'Home', number of ppl go to Bar, number of ppl go to Home)

    def start(self):
        for t in range(self.T):
            res = self.iterate(t)
            self.final_results.append(res)
            self.update(res, t)
            self.past_games += '1' if res[0] == 'Bar' else '0'

    def iterate(self, t: int):
        print("Iteration ", t)
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

    def update(self, result: Tuple[str, int, int], t: int):
        for agent in self.agents:
            _ = agent.update(result[0], self.past_games)

    def get_final_results(self): return self.final_results


class Network_Minority_Game(Traditional_Minority_Game):
    def __init__(self, T: int, N: int, agents: List[Agent], past_games: str, threshold: int, p: float, time_step: List[int], time_limit = None, seed = 123):
        super().__init__(T, N, agents, past_games, threshold, time_limit)
        self.network = Network(self.agents, p, seed)
        self.num_solo_agent = 0
        self.num_coop_agent = 0
        self.arr_num_solo_winner = []
        self.arr_num_coop_winner = []
        self.time_step = time_step
        self.update_network()
    
    def update_network(self):
        for agent in self.agents:
            self.network.G.nodes[agent.index]['object'] = agent
            agent.neighbors = [self.agents[i] for i in list(self.network.G[agent.index])]
            if (agent.neighbors):
                self.num_coop_agent += 1
                self.network.colors.append("tab:orange")
            else:
                self.num_solo_agent += 1
                self.network.colors.append("tab:blue")
    
    def update(self, result: Tuple[str, int, int], t: int):         
        # Similar to update() of parent, but need to keep track coop and solo
        # as well as propagate strategies
        num_solo_winner = 0
        num_coop_winner = 0
        for agent in self.agents:
            is_winner = agent.update(result[0], self.past_games)
            if (agent.neighbors):
                if (is_winner):
                    num_coop_winner += 1
            else:
                if (is_winner):
                    num_solo_winner += 1
        self.arr_num_solo_winner.append(num_solo_winner)
        self.arr_num_coop_winner.append(num_coop_winner)
        if (t in self.time_step):           # propagate strategies at pre-defined time steps
            self.propagate()

    
    def propagate(self):
        # Temporary Aggregate Strategies for each player
        for agent in self.agents:
            if (agent.neighbors):
                aggregated_strategies = []
                aggregated_virtual_point = []
                for neighbor in agent.neighbors:
                    if (agent.aggregate_mode == "all"):
                        s, vp = aggregate_all_neighbor_strategies(agent, neighbor)
                    elif (agent.aggregate_mode == "best"):
                        s, vp = aggregate_best_neighbor_strategies(agent, neighbor)
                        if s is None:
                            continue
                    aggregated_strategies.append(s)
                    aggregated_virtual_point.append(vp)
                if not aggregated_strategies:       # aggregate nothing
                    continue
                agent.aggregated_strategies = np.concatenate(aggregated_strategies, axis=0)
                agent.aggregated_virtual_point = np.concatenate(aggregated_virtual_point, axis = 0)
        
        # Update Strategy for each player (strategies as well as virtual point of neighbors)
        for agent in self.agents:
            if (agent.neighbors):
                agent.strategies = np.concatenate((agent.strategies, agent.aggregated_strategies), axis = 0)
                agent.virtual_point = np.concatenate((agent.virtual_point, agent.aggregated_virtual_point), axis = 0)
                agent.num_strategies = agent.virtual_point.shape[0]
                agent.aggregated_strategies = None
                agent.aggregated_virtual_point = None

class Disconnected_Network_Minority_Game_10(Traditional_Minority_Game):
    def __init__(self, T: int, N: int, agents: List[Agent], past_games: str, threshold: int, time_step: List[int], time_limit = None, seed = 123):
        super().__init__(T, N, agents, past_games, threshold, time_limit)
        self.network = Disconnected_Network_10(self.agents, seed)
        self.num_winner_by_group = {
            1: [],
            10: [],
            20: [],
            30: [],
            40: [],
            50: [],
            60: [],
            70: [],
            80: [],
            90: []
        }
        self.time_step = time_step

        self.colors = {
            1: "tab:blue",
            10: "tab:orange",
            20: "tab:green",
            30: "tab:red",
            40: "tab:purple",
            50: "tab:brown",
            60: "tab:pink",
            70: "tab:gray",
            80: "tab:olive",
            90: "tab:cyan",
        }

        self.update_network()
        
    
    def update_network(self):
        for agent in self.agents:
            self.network.G.nodes[agent.index]['object'] = agent
            agent.neighbors = [self.agents[i] for i in list(self.network.G[agent.index])]
            self.network.colors.append(self.colors[len(nx.shortest_path(self.network.G, agent.index))])
    
    def update(self, result: Tuple[str, int, int], t: int):         
        # Similar to update() of parent
        # as well as propagate strategies
        num_winner_by_group = {
            1: 0,
            10: 0,
            20: 0,
            30: 0,
            40: 0,
            50: 0,
            60: 0,
            70: 0,
            80: 0,
            90: 0
        }
        for agent in self.agents:
            is_winner = agent.update(result[0], self.past_games)
            if is_winner:
                group_id = len(nx.shortest_path(self.network.G, agent.index))
                num_winner_by_group[group_id] += 1
        for key, value in num_winner_by_group.items():
            self.num_winner_by_group[key].append(value)
        if (t in self.time_step):           # propagate strategies at pre-defined time steps
            self.propagate()

    
    def propagate(self):
        # Temporary Aggregate Strategies for each player
        for agent in self.agents:
            if (agent.neighbors):
                aggregated_strategies = []
                aggregated_virtual_point = []
                for neighbor in agent.neighbors:
                    s, vp = aggregate_all_neighbor_strategies(agent, neighbor)
                    aggregated_strategies.append(s)
                    aggregated_virtual_point.append(vp)
                agent.aggregated_strategies = np.concatenate(aggregated_strategies, axis=0)
                agent.aggregated_virtual_point = np.concatenate(aggregated_virtual_point, axis = 0)
        
        # Update Strategy for each player (strategies as well as virtual point of neighbors)
        for agent in self.agents:
            if (agent.neighbors):
                agent.strategies = np.concatenate((agent.strategies, agent.aggregated_strategies), axis = 0)
                agent.virtual_point = np.concatenate((agent.virtual_point, agent.aggregated_virtual_point), axis = 0)
                agent.num_strategies = agent.virtual_point.shape[0]
                agent.aggregated_strategies = None
                agent.aggregated_virtual_point = None


class Disconnected_Network_Minority_Game_5(Traditional_Minority_Game):
    def __init__(self, T: int, N: int, agents: List[Agent], past_games: str, threshold: int, time_step: List[int], time_limit = None, seed = 123):
        super().__init__(T, N, agents, past_games, threshold, time_limit)
        self.network = Disconnected_Network_5(self.agents, seed)
        self.num_winner_by_group = {
            1: [],
            32: [],
            64: [],
            128: [],
            256: [],
        }
        self.time_step = time_step

        self.colors = {
            1: "tab:blue",
            32: "tab:orange",
            64: "tab:green",
            128: "tab:red",
            256: "tab:purple",
        }

        self.update_network()
        
    
    def update_network(self):
        for agent in self.agents:
            self.network.G.nodes[agent.index]['object'] = agent
            agent.neighbors = [self.agents[i] for i in list(self.network.G[agent.index])]
            self.network.colors.append(self.colors[len(nx.shortest_path(self.network.G, agent.index))])
    
    def update(self, result: Tuple[str, int, int], t: int):         
        # Similar to update() of parent
        # as well as propagate strategies
        num_winner_by_group = {
            1: 0,
            32: 0,
            64: 0,
            128: 0,
            256: 0,
        }
        for agent in self.agents:
            is_winner = agent.update(result[0], self.past_games)
            if is_winner:
                group_id = len(nx.shortest_path(self.network.G, agent.index))
                num_winner_by_group[group_id] += 1
        for key, value in num_winner_by_group.items():
            self.num_winner_by_group[key].append(value)
        if (t in self.time_step):           # propagate strategies at pre-defined time steps
            self.propagate()

    
    def propagate(self):
        # Temporary Aggregate Strategies for each player
        for agent in self.agents:
            if (agent.neighbors):
                aggregated_strategies = []
                aggregated_virtual_point = []
                for neighbor in agent.neighbors:
                    s, vp = aggregate_all_neighbor_strategies(agent, neighbor)
                    aggregated_strategies.append(s)
                    aggregated_virtual_point.append(vp)
                agent.aggregated_strategies = np.concatenate(aggregated_strategies, axis=0)
                agent.aggregated_virtual_point = np.concatenate(aggregated_virtual_point, axis = 0)
        
        # Update Strategy for each player (strategies as well as virtual point of neighbors)
        for agent in self.agents:
            if (agent.neighbors):
                agent.strategies = np.concatenate((agent.strategies, agent.aggregated_strategies), axis = 0)
                agent.virtual_point = np.concatenate((agent.virtual_point, agent.aggregated_virtual_point), axis = 0)
                agent.num_strategies = agent.virtual_point.shape[0]
                agent.aggregated_strategies = None
                agent.aggregated_virtual_point = None