import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def forecast_load(df, column='CPU_usage', steps=10):
    model = ARIMA(df[column], order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    return forecast

if __name__ == "__main__":
    df = pd.read_csv("data/server_data.csv")
    predictions = forecast_load(df)
    print("Forecasted values:", predictions)
