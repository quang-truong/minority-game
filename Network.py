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
    
    def plot_graph(self, fig_dir = None):
        options = {"edgecolors": "tab:gray", "node_color": self.colors, "node_size": 150, "alpha": 0.9, "font_size": 8, "font_color": "whitesmoke"}
        nx.draw_networkx(self.G, with_labels = False, **options)
        if fig_dir:
            plt.savefig(fig_dir, dpi = 500)
        else:
            plt.show()
        plt.close()

class Disconnected_Network_10(Network):
    def __init__(self, agents: List[Agent], seed: int):
        super().__init__(agents, 0.5, seed)
        self.G = nx.Graph()
        self.G.add_node(1)
        for i in range(10, 91, 10):
            if (i == 10):   p = 0.225
            elif (i == 20): p = 0.2
            elif (i == 30): p = 0.2
            elif (i == 40): p = 0.2
            elif (i == 50): p = 0.1
            elif (i == 60): p = 0.1
            elif (i == 70): p = 0.1
            elif (i == 80): p = 0.1
            elif (i == 90): p = 0.05
            g = (nx.generators.erdos_renyi_graph(i, p, seed))           # actually p = 0.5 is the minimum bound to guarantee to have a connected graph of N nodes.
            self.G = nx.union(self.G, g, rename=('A', 'B'))                 # If p doesn't work, try to increase p. The trade-off is longer runtime.
        self.G = nx.convert_node_labels_to_integers(self.G)
        self.colors = []
    
    def plot_graph(self, fig_dir = None):
        options = {"edgecolors": "tab:gray", "node_color": self.colors, "node_size": 150, "alpha": 0.9, "font_size": 8, "font_color": "whitesmoke"}
        nx.draw_shell(self.G, with_labels = False, **options)
        if fig_dir:
            plt.savefig(fig_dir, dpi = 500)
        else:
            plt.show()
        plt.close()

class Disconnected_Network_4(Network):
    def __init__(self, agents: List[Agent], seed: int):
        super().__init__(agents, 0.5, seed)
        self.G = nx.Graph()
        self.G.add_node(1)
        for i in [64, 128, 256]:
            if (i == 64): p = 0.1
            elif (i == 128): p = 0.035
            else: p = 0.019
            g = (nx.generators.erdos_renyi_graph(i, p, seed))           # actually p = 0.5 is the minimum bound to guarantee to have a connected graph of N nodes.
            self.G = nx.union(self.G, g, rename=('A', 'B'))             # If p doesn't work, try to increase p. The trade-off is longer runtime.
        self.G = nx.convert_node_labels_to_integers(self.G)
        self.colors = []
    
    def plot_graph(self, fig_dir = None):
        options = {"edgecolors": "tab:gray", "node_color": self.colors, "node_size": 150, "alpha": 0.9, "font_size": 8, "font_color": "whitesmoke"}
        nx.draw_shell(self.G, with_labels = False, **options)
        if fig_dir:
            plt.savefig(fig_dir, dpi = 500)
        else:
            plt.show()
        plt.close()
