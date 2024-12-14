import threading
from src.generate_data import generate_data
from src.preprocess import preprocess_data
from src.analyze import analyze_data
from src.forecast import forecast_load
from src.dashboard import create_dashboard

def run_dashboard():
    app = create_dashboard()
    app.run_server(debug=True)

if __name__ == "__main__":
    # 1. Генерация данных
    generate_data()

    # 2. Предобработка
    df = preprocess_data()

    # 3. Анализ
    analyze_data(df)

    # 4. Прогнозирование
    forecast = forecast_load(df)
    print("Forecast:", forecast)

    # 5. Запуск дашборда в отдельном потоке
    threading.Thread(target=run_dashboard).start()
