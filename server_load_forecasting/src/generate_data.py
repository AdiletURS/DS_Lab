import pandas as pd
import numpy as np

def generate_data(output_path="data/server_data.csv"):
    timestamps = pd.date_range(start="2024-01-01", periods=1000, freq="T")
    cpu_usage = np.random.normal(loc=50, scale=10, size=len(timestamps))
    ram_usage = np.random.normal(loc=60, scale=15, size=len(timestamps))
    network_traffic = np.random.normal(loc=100, scale=25, size=len(timestamps))

    data = pd.DataFrame({
        "timestamp": timestamps,
        "CPU_usage": cpu_usage,
        "RAM_usage": ram_usage,
        "network_traffic": network_traffic
    })
    data.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    generate_data()
