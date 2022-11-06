# Import netowrkx to visualize our graphs. 

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
  

from turtle import Turtle

# Ball move distance
MOVE_DIST = 1

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('blue')
    self.penup()
    self.x_move_dist = MOVE_DIST
    self.y_move_dist = MOVE_DIST
    self.reset()

  def move(self):
    # Move only 1 step ahead both vertically and horizontally 
    new_y = self.ycor() + self.y_move_dist
    new_x = self.xcor() + self.x_move_dist
    self.goto(x = new_y, y = new_y)

  def bounce(self, x_bounce, y_bounce):
    if x_bounce:
      # Reverse the horizontal direction 
      self.x_move_dist *= -1

    if y_bounce:
      # Reverse the vertical direction 
      self.y_move_dist *= -1
      
  def reset(self) -> None:
      return super().reset()
