from Agent import Agent

import networkx as nx
import matplotlib.pyplot as plt
from typing import List

class Network():
    def __init__(self, agents: List[Agent], p: float, directed: bool, seed: int):
        self.agents = agents
        self.p = p
        self.directed = directed
        self.seed = seed
        self.G = nx.generators.erdos_renyi_graph(len(self.agents), p, seed, directed)
        self.colors = []
    
    def plot_graph(self):
        options = {"edgecolors": "tab:gray", "node_color": self.colors, "node_size": 150, "alpha": 0.9, "font_size": 8, "font_color": "whitesmoke"}
        nx.draw_networkx(self.G, with_labels = False, **options)
        plt.show()
