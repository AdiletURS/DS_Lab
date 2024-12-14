import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def forecast_with_lstm(filepath):
    # Загрузка очищенных данных
    data = pd.read_csv(filepath)
    cpu_usage = data['CPU_usage'].values.reshape(-1, 1)

    # Нормализация данных
    scaler = MinMaxScaler()
    cpu_usage_scaled = scaler.fit_transform(cpu_usage)

    # Создание временных рядов
    def create_sequences(data, seq_length):
        X, y = [], []
        for i in range(len(data) - seq_length):
            X.append(data[i:i+seq_length])
            y.append(data[i+seq_length])
        return np.array(X), np.array(y)

    seq_length = 20  # Длина последовательности
    X, y = create_sequences(cpu_usage_scaled, seq_length)

    # Разделение на обучающую и тестовую выборки
    split = int(0.8 * len(X))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    # Построение модели
    model = Sequential([
        LSTM(50, activation='relu', input_shape=(seq_length, 1)),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')

    # Обучение модели
    model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1)

    # Прогнозирование
    predictions = model.predict(X_test)
    predictions = scaler.inverse_transform(predictions)

    # Построение графика
    plt.figure(figsize=(10, 5))
    plt.plot(cpu_usage[-len(predictions):], label="Фактические данные", color='blue')
    plt.plot(predictions, label="Прогноз", color='orange')
    plt.legend()
    plt.title("Прогнозирование загрузки CPU (LSTM)")
    plt.show()

if __name__ == "__main__":
    forecast_with_lstm("data/cleaned_server_data.csv")
