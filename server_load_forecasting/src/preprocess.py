import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(input_path="data/server_data.csv"):
    df = pd.read_csv(input_path)
    # Удаление пропусков
    df.fillna(method='ffill', inplace=True)
    # Нормализация данных
    scaler = MinMaxScaler()
    df[['CPU_usage', 'RAM_usage', 'network_traffic']] = scaler.fit_transform(
        df[['CPU_usage', 'RAM_usage', 'network_traffic']]
    )
    return df

if __name__ == "__main__":
    df = preprocess_data()
    print(df.head())
