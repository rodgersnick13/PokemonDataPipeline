import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load Pokémon data
df = pd.read_csv("pokemon_cleaned.csv")

# Attributes to compare
stats = ['hp', 'attack', 'defense', 'speed', 'height_m', 'weight_kg']

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pokémon Stat Comparison Dashboard"),

    # Overall Scatter Overview
    dcc.Graph(id='overview-graph'),

    html.Label("Select Pokémon to Compare:"),
    dcc.Dropdown(
        id="pokemon-dropdown",
        options=[{'label': p, 'value': p} for p in df['name']],
        multi=False
    ),

    html.Label("Select Second Pokémon to Compare:"),
    dcc.Dropdown(
        id="opp-dropdown",
        options=[{'label': p, 'value': p} for p in df['name']],
        multi=False
    ),

    dcc.Graph(id='bar-comparison-graph')
])


@app.callback(
    Output('overview-graph', 'figure'),
    Output('bar-comparison-graph', 'figure'),
    Input('pokemon-dropdown', 'value'),
    Input('opp-dropdown', 'value')
)
def compare_pokemon(selected_pokemon, opp_pokemon):
    # ---------- OVERVIEW SCATTER ----------
    overview_scatter_fig = px.scatter(
        df,
        x="attack",
        y="defense",
        color="type1",
        hover_data=['name'],
        title="Pokémon Overview: Attack vs Defense"
    )

    # Highlight selected Pokémon
    if selected_pokemon:
        sel_row = df[df['name'] == selected_pokemon]
        overview_scatter_fig.add_trace(go.Scatter(
            x=sel_row['attack'],
            y=sel_row['defense'],
            mode='markers+text',
            text=[selected_pokemon],
            textposition="top center",
            marker=dict(size=15, color='black', symbol='star'),
            name=selected_pokemon
        ))

    # Highlight opponent Pokémon if selected
    if opp_pokemon:
        opp_row = df[df['name'] == opp_pokemon]
        overview_scatter_fig.add_trace(go.Scatter(
            x=opp_row['attack'],
            y=opp_row['defense'],
            mode='markers+text',
            text=[opp_pokemon],
            textposition="top center",
            marker=dict(size=15, color='red', symbol='diamond'),
            name=opp_pokemon
        ))

    # ---------- BAR CHART ----------
    if not selected_pokemon:
        bar_fig = px.bar(title="Select at least one Pokémon to compare stats")
        return overview_scatter_fig, bar_fig

    sel_stats = df[df['name'] == selected_pokemon][stats].iloc[0]

    if opp_pokemon:
        # Compare against the opponent Pokémon directly
        opp_stats = df[df['name'] == opp_pokemon][stats].iloc[0]
        comparison_df = pd.DataFrame({
            'Attribute': stats,
            selected_pokemon: sel_stats.values,
            opp_pokemon: opp_stats.values
        })
    else:
        # Compare against the mean of all other Pokémon
        others_mean = df[df['name'] != selected_pokemon][stats].mean()
        comparison_df = pd.DataFrame({
            'Attribute': stats,
            selected_pokemon: sel_stats.values,
            'Average Pokémon': others_mean.values
        })

    comparison_df = comparison_df.melt(id_vars='Attribute', var_name='Pokémon', value_name='Stat Value')
    bar_fig = px.bar(
        comparison_df,
        x='Attribute',
        y='Stat Value',
        color='Pokémon',
        barmode='group',
        title=f"{selected_pokemon} vs {opp_pokemon if opp_pokemon else 'Average Pokémon'}"
    )
    bar_fig.update_layout(yaxis_title="Stat Value", showlegend=True)

    return overview_scatter_fig, bar_fig


if __name__ == "__main__":
    app.run(debug=True)
