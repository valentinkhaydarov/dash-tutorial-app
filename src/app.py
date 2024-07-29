from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src.business_logic.preprocessing import prepare_plot_data, get_country_list

app = Dash()

app.layout = [
    html.H1(children='Population by country',
            style={'textAlign':'center'}),
    dcc.Dropdown(options=get_country_list(),
                 value='germany',
                 id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value: str):
    plot_data = prepare_plot_data(country=value)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=plot_data['year'],
                         y=plot_data['pop_change'],
                         name = "Change",
                         opacity=0.5),
                         secondary_y=True)
    fig.add_trace(go.Scatter(x=plot_data['year'],
                             y=plot_data['pop'],
                             mode='lines+markers',
                             name = "Value"),
                             secondary_y=False)
    fig.update_yaxes(title_text="Absolute Population", secondary_y=False)
    fig.update_yaxes(title_text="Population Change", secondary_y=True)
    
    return fig                         

if __name__ == '__main__':
    app.run()
