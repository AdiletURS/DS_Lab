# Прогнозирование пиковых нагрузок на серверную инфраструктуру

## Описание

Этот проект нацелен на прогнозирование пиковых нагрузок на серверную инфраструктуру. Он использует данные о загрузке серверов, такие как CPU, RAM, и сетевой трафик, и применяет модели временных рядов для предсказания нагрузки на 10-15 минут вперед.

## Структура проекта

- `data/server_data.csv` — данные о серверной нагрузке.
- `src/generate_data.py` — генерация данных.
- `src/model_training.py` — обучение моделей.
- `src/forecast.py` — прогнозирование нагрузки.
- `src/alerts.py` — система уведомлений.
- `src/dashboard.py` — дашборд для визуализации.
- `requirements.txt` — зависимости.

## Запуск проекта

1. Установите зависимости:

Давайте подробно рассмотрим, что делает каждый файл в вашем проекте и какие требования они выполняют.

### **1. Структура проекта**

```
server_load_forecasting/
├── data/
│   ├── server_data.csv         # Исходные данные сервера
│   ├── cleaned_server_data.csv # Очищенные данные сервера
├── src/
│   ├── generate_data.py        # Генерация данных
│   ├── preprocess.py           # Основная предобработка данных
│   ├── data_preprocessing.py   # Расширенная предобработка данных
│   ├── analyze.py              # Анализ данных
│   ├── forecast.py             # Управление прогнозированием
│   ├── forecast_arima.py       # Прогнозирование с использованием модели ARIMA
│   ├── forecast_lstm.py        # Прогнозирование с использованием модели LSTM
│   ├── dashboard.py            # Визуализация и управление дашбордом
│   ├── alerts.py               # Уведомления (например, через Telegram)
│   └── __pycache__/            # Кэшированные файлы Python
├── app.py                      # Главный файл для запуска системы
├── requirements.txt            # Список зависимостей проекта
└── README.md                   # Документация проекта
```

---

### **2. Описание файлов**

#### **`data/`**

- **`server_data.csv`** — Исходные данные о серверной нагрузке. Этот файл содержит сырые данные, такие как CPU, RAM, использование сети и другие метрики. Эти данные могут быть собраны с серверов или сгенерированы.
  - **Требование:** Содержит данные для анализа и прогнозирования нагрузки серверов.
- **`cleaned_server_data.csv`** — Очищенные и предварительно обработанные данные. Этот файл создается после обработки и очищения данных, включая удаление пропусков, исправление выбросов, нормализацию и другие преобразования.
  - **Требование:** Содержит подготовленные для обучения и анализа данные.

---

#### **`src/`**

- **`generate_data.py`** — Скрипт для генерации исходных данных, если они не предоставлены. Этот файл может использовать случайные данные или получать их с сервера.
  - **Требование:** Генерация исходных данных для анализа и прогнозирования нагрузки.
- **`preprocess.py`** — Скрипт для выполнения базовой предобработки данных. Включает обработку пропусков, удаление ненужных столбцов, нормализацию и стандартизацию.
  - **Требование:** Подготовка данных для последующего анализа и использования в моделях.
- **`data_preprocessing.py`** — Расширенная предобработка данных. Может включать более сложные трансформации, такие как агрегирование, создание новых признаков, обработка категориальных переменных, детектирование аномалий и др.
  - **Требование:** Углубленная предобработка данных для улучшения точности моделей и улучшения качества прогноза.
- **`analyze.py`** — Скрипт для выполнения анализа данных. Этот файл включает в себя статистические методы для изучения распределений, корреляций, трендов и других важных характеристик данных.
  - **Требование:** Проведение анализа для выявления закономерностей и подготовки данных для прогнозирования.
- **`forecast.py`** — Управление прогнозированием нагрузки на сервер. Этот файл отвечает за настройку и запуск моделей прогнозирования.
  - **Требование:** Объединение и управление процессом прогнозирования на основе данных и выбранных моделей.
- **`forecast_arima.py`** — Скрипт для прогнозирования с использованием модели ARIMA. Включает в себя создание, обучение и прогнозирование с использованием модели ARIMA для временных рядов.
  - **Требование:** Прогнозирование будущей нагрузки на сервер с использованием традиционной модели ARIMA.
- **`forecast_lstm.py`** — Скрипт для прогнозирования с использованием модели LSTM (Long Short-Term Memory). Используется для более сложных данных, таких как временные ряды с долгосрочной зависимостью.
  - **Требование:** Прогнозирование серверной нагрузки с использованием нейронных сетей для обработки более сложных данных.
- **`dashboard.py`** — Скрипт для создания дашборда. Этот файл визуализирует данные и прогнозы, предоставляет возможность для анализа текущего состояния и будущих прогнозов.
  - **Требование:** Визуализация результатов анализа и прогнозов для удобства мониторинга.
- **`alerts.py`** — Скрипт для отправки уведомлений, например, через Telegram, если серверная нагрузка превышает пороговые значения. Уведомления могут быть отправлены при достижении критических уровней.

  - **Требование:** Оповещение пользователей о потенциальных проблемах на сервере (например, чрезмерная нагрузка).

- **`__pycache__/`** — Папка, содержащая кэшированные файлы Python (.pyc). Эти файлы автоматически генерируются при запуске скриптов и ускоряют выполнение программ.
  - **Требование:** Повышение производительности при выполнении программы.

---

#### **`app.py`**

Главный файл для запуска системы. Этот файл инициализирует и запускает все компоненты проекта, соединяя обработку данных, прогнозирование, визуализацию и уведомления в единую систему. Через этот файл можно запускать приложение для мониторинга и получения прогнозов.

- **Требование:** Объединение всех частей системы и управление их взаимодействием.

---

#### **`requirements.txt`**

Файл, в котором перечислены все зависимости для проекта (например, `pandas`, `numpy`, `matplotlib`, `statsmodels`, `tensorflow`, `dash`, `requests` и т.д.). Это позволяет легко устанавливать все необходимые библиотеки с помощью команды:

```bash
pip install -r requirements.txt
```

- **Требование:** Указание всех внешних зависимостей, необходимых для работы проекта.

---

#### **`README.md`**

Документация проекта, которая объясняет, что делает проект, как его настроить, как запустить и как использовать. Она может содержать информацию о целях проекта, структуре, установке зависимостей и запуске отдельных компонентов.

- **Требование:** Предоставление документации для понимания работы системы и ее развертывания.

---

### **Как каждый файл отвечает требованиям:**

- **Генерация данных (`generate_data.py`)** — Отвечает на требование о наличии исходных данных для анализа.
- **Предобработка данных (`preprocess.py` и `data_preprocessing.py`)** — Эти файлы отвечают на требования о подготовке данных для анализа и прогнозирования.
- **Анализ данных (`analyze.py`)** — Отвечает на требование проведения анализа данных для выявления закономерностей.
- **Прогнозирование (`forecast.py`, `forecast_arima.py`, `forecast_lstm.py`)** — Эти файлы отвечают на требования прогнозирования серверной нагрузки с использованием различных моделей (ARIMA и LSTM).
- **Визуализация (`dashboard.py`)** — Отвечает на требование о визуализации данных и прогнозов для мониторинга состояния серверной инфраструктуры.
- **Уведомления (`alerts.py`)** — Отвечает на требование об уведомлениях о критической нагрузке на сервер.
- **Главный файл (`app.py`)** — Объединяет все части системы и управляет запуском и взаимодействием компонентов.
- **Зависимости (`requirements.txt`)** — Обеспечивает установку всех необходимых библиотек для работы с проектом.
- **Документация (`README.md`)** — Обеспечивает описание и инструкции по использованию проекта.

В результате, каждый файл отвечает на определенные требования, которые связаны с обработкой данных, прогнозированием, визуализацией и уведомлениями, создавая систему, способную мониторить и прогнозировать нагрузку на серверы.
