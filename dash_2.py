
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd 

from app import server  

app = dash.Dash('dash_2', sharing=True, url_base_pathname='/dash_2', csrf_protect=False, server=server) 

app.config['suppress_callback_exceptions']=True 

df = pd.read_csv('app_2/slice.csv')



app.layout = html.Div(children=[
    html.H1(children='Barstool Sports: '
                     'A Pizza Slice Review '
                     'By El Presidente'),

    html.Div(children='''
        One Bite...Everybody Knows the Rules.
    '''),

    dcc.Graph(
        id='slice.csv',
        figure={
            'data': [
            {'x':df['Slice'], 'y': df['Score'], 'type': 'bar', 'name': 'score'}, 
            ],
            'layout': {
                'title': 'Barstool Sports Pizza Slice Review in NYC' 
            }
        }
    )


])

'''

@app.callback(
    Output('dash-2-display-value', 'children'),
    [Input('dash-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

''' 

