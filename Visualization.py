# Import netowrkx to visualize our graphs. 

import imp
from random import random
from numpy import void
import utils
import Games


from Games import past_games
from Agent import Agent

"""
The dash and visdcc were not loading on visual studio code. 
import dash
import visdcc
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Create app
app = dash.Dash()

# Load data
data = games


# Define layout 
app.layout = html.Div([ 
  visdcc.Network(id = 'net', 
                 data = {'nodes': nodes, 'edges': edges},
                 options = dict(height = '600px', width = '100%')),
  dcc.RadioItems(id = 'color',
                 options = [{'label': 'Red', 'value': '#FF0000'},
                            {'label': 'Blue', 'value': '#0000FF'}],
                 value = 'Red')])
  
  # Define callback 
app.callback(
  Output('net', 'options'),
  [Input('color', 'value')])
  
def myfun(x):
  return {'nodes': {'color': x}}
  
# Define the main calling 
if __name__ == "__main__":
  app.run_server(debug = True)
"""

import networkx as nx 
# Load pandas df as networkx graph 
data = nx.from_pandas_edgelist(Games, Agent, past_games)
  


