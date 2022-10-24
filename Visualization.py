# Import netowrkx to visualize our graphs. 
import networkx as nx

from Games import Single_Stage_Game
from Agent import Agent

data = Single_Stage_Game(0, N, agents, past_games= None, threshold = 0.5, time_limit= None)
nx.draw_spring(data)
