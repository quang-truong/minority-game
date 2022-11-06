from Agent import Agent

import networkx as nx
import matplotlib.pyplot as plt
from typing import List

class Network():
    def __init__(self, agents: List[Agent], p: float, seed: int):
        self.agents = agents
        self.p = p
        self.seed = seed
        self.G = nx.generators.erdos_renyi_graph(len(self.agents), p, seed)
        self.colors = []
    
    def plot_graph(self):
        options = {"edgecolors": "tab:gray", "node_color": self.colors, "node_size": 150, "alpha": 0.9, "font_size": 8, "font_color": "whitesmoke"}
        nx.draw_networkx(self.G, with_labels = False, **options)
        plt.show()

class Disconnected_Network(Network):
    def __init__(self, agents: List[Agent], seed: int):
        super().__init__(agents, 0.5, seed)
        self.G = nx.Graph()
        self.G.add_node(1)
        for i in range(10, 91, 10):
            g = (nx.generators.erdos_renyi_graph(i, 0.5, seed))
            self.G = nx.union(self.G, g, rename=('A', 'B'))
        self.G = nx.convert_node_labels_to_integers(self.G)
        self.colors = []
    
    def plot_graph(self):
        options = {"edgecolors": "tab:gray", "node_color": self.colors, "node_size": 150, "alpha": 0.9, "font_size": 8, "font_color": "whitesmoke"}
        nx.draw_shell(self.G, with_labels = False, **options)
        plt.show()
    
