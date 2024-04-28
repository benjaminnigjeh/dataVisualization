import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Data Visualization Dashboard"),
    dcc.Graph(id='scatter-plot'),
    dcc.Slider(
        id='slider',
        min=1,
        max=10,
        step=1,
        value=5,
        marks={i: str(i) for i in range(1, 11)}
    )
])

# Define callback to update the scatter plot based on slider value
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('slider', 'value')
)
def update_scatter_plot(selected_value):
    # Update the data based on the selected value
    updated_df = df[df['x'] <= selected_value]
    
    # Create a scatter plot
    fig = px.scatter(updated_df, x='x', y='y', title='Scatter Plot')
    
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
