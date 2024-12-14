import pandas as pd
import numpy as np

def preprocess_data(filepath):
    # Загрузка данных
    data = pd.read_csv(filepath)

    # Удаление пропусков
    data = data.dropna()

    # Удаление аномалий
    for column in ['CPU_usage', 'RAM_usage', 'network_traffic']:
        mean = data[column].mean()
        std_dev = data[column].std()
        upper_limit = mean + 3 * std_dev
        lower_limit = mean - 3 * std_dev
        data = data[(data[column] >= lower_limit) & (data[column] <= upper_limit)]

    return data

if __name__ == "__main__":
    cleaned_data = preprocess_data("data/server_data.csv")
    cleaned_data.to_csv("data/cleaned_server_data.csv", index=False)
