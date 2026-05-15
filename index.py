python
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load the dataset
data_url = 'https://example.com/Renewable_Energy_Share.csv'
data = pd.read_csv(data_url)

# Initialize the Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Abu Dhabi Renewable Energy Trends Dashboard"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': str(year), 'value': year} for year in data['Year'].unique()],
        multi=True,
        placeholder="Select Year(s)"
    ),
    dcc.Graph(id='trend-graph'),
    html.Div(id='summary-output')
])

# Callbacks for interactivity
@app.callback(
    [Output('trend-graph', 'figure'),
     Output('summary-output', 'children')],
    [Input('year-dropdown', 'value')]
)
def update_graph(selected_years):
    if not selected_years:
        filtered_data = data
        summary = f"Displaying data for all years."
    else:
        filtered_data = data[data['Year'].isin(selected_years)]
        summary = f"Displaying data for years: {', '.join(map(str, selected_years))}"

    fig = px.line(filtered_data, x='Year', y='Renewable Energy Share (%)', 
                  title="Trend of Renewable Energy Share (2013-2024)",
                  labels={'Year': 'Year', 'Renewable Energy Share (%)': 'Renewable Energy Share (%)'})
    
    return fig, summary

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
