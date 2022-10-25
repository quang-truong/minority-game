# Import netowrkx to visualize our graphs. 
import dash 
import visdcc
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from Games import Single_Stage_Game
from Agent import Agent


# Create app
app = dash.Dash()

# Load data
data = Single_Stage_Game(0, N, agents, past_games= None, threshold = 0.5, time_limit= None)

# Define layout 
app.layout = html.Div([ 
  visdcc.Network(id = 'net', 
                 data = {'nodes': nodes, 'edges': edges},
                 options = dict(height = '600px', width = '100%')),
  dcc.RadioItems(id = 'color',
                 options = [{'label': 'Red', 'value': '#ff0000'},
                            {'label': 'Green', 'value': '#00ff00'},
                            {'label': 'Blue', 'value': '#0000ff'}],
                 value = 'Red')
  
  # Define callback 
  app.callback(
    Output('net', 'options'),
    [Input('color', 'value')])
  
  def myfun(x):
    return {'nodes': {'color': x}}
  
 # Define the main calling 
  if __name__. = '__main__':
    app.run_server(debug = True)
  
                             
