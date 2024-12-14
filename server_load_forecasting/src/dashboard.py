from dash import Dash, dcc, html
import pandas as pd
import plotly.graph_objs as go

def create_dashboard():  # Функция для создания дашборда
    app = Dash(__name__)

    data = pd.read_csv("data/cleaned_server_data.csv")

    app.layout = html.Div([
        html.H1("Server Load Dashboard"),
        dcc.Graph(
            id="cpu-usage",
            figure={
                "data": [
                    go.Scatter(
                        x=data['timestamp'],
                        y=data['CPU_usage'],
                        mode="lines",
                        name="CPU Usage"
                    ),
                ],
                "layout": {
                    "title": "CPU Usage Over Time"
                }
            }
        )
    ])
    return app  # Возвращаем объект приложения

# В app.py теперь можно будет импортировать и использовать create_dashboard
