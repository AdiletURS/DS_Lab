from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import matplotlib.pyplot as plt

def forecast_with_arima(filepath):
    # Загрузка очищенных данных
    data = pd.read_csv(filepath)
    cpu_usage = data['CPU_usage']

    # Разделение данных на обучающую и тестовую выборки
    train = cpu_usage[:int(0.8 * len(cpu_usage))]
    test = cpu_usage[int(0.8 * len(cpu_usage)):]

    # Обучение модели
    model = ARIMA(train, order=(5, 1, 0))
    model_fit = model.fit()

    # Прогнозирование
    forecast = model_fit.forecast(steps=len(test))

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.plot(test.values, label="Фактические данные", color='blue')
    plt.plot(forecast, label="Прогноз", color='orange')
    plt.legend()
    plt.title("Прогнозирование загрузки CPU (ARIMA)")
    plt.show()

if __name__ == "__main__":
    forecast_with_arima("data/cleaned_server_data.csv")
