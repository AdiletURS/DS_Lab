import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['CPU_usage'], label='CPU Usage')
    plt.plot(df['timestamp'], df['RAM_usage'], label='RAM Usage')
    plt.legend()
    plt.xlabel('Timestamp')
    plt.ylabel('Usage')
    plt.title('Server Load Metrics Over Time')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data/server_data.csv")
    analyze_data(df)
