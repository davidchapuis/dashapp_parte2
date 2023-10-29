from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "Fruta": ["Abacaxi", "Jaca", "Banana", "Abacaxi", "Jaca", "Banana"],
    "Quantidade": [4, 1, 2, 2, 4, 5],
    "Cidade": ["São Paulo", "São Paulo", "São Paulo", "Rio", "Rio", "Rio"]
})

fig = px.bar(df, x="Fruta", y="Quantidade", color="Cidade", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Bom dia Dash'),

    html.Div(children='''
        Dash: Um framework web para os seus dados.
    '''),

    dcc.Graph(
        id='examplo-graf',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)