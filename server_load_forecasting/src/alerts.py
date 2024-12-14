import requests

def send_alert(message):
    url = f"https://api.telegram.org/bot7524338613:AAEx_t2ko4gWBdFleME8fmlDBDmP6La8f_E/sendMessage"
    params = {"chat_id": "824151875", "text": message}
    response = requests.get(url, params=params)
    print(response.json())

if __name__ == "__main__":
    # Пример уведомления
    send_alert("Внимание: нагрузка на сервер достигла пикового уровня!")
