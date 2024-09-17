import requests

class APIConnection:
    def __init__(self, api_url="http://127.0.0.1"):
        self.url = api_url

    def get_item(self, item_id):
        """Получение элемента по ID через запрос GET"""
        try:
            response = requests.get(f"{self.url}/item/{item_id}")
            response.raise_for_status()  # Проверка на успешный ответ
            return response.json()  # Вернуть данные в формате JSON
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None

    def create_item(self, data):
        """Создание нового элемента через запрос POST"""
        try:
            response = requests.post(f"{self.url}/item", json=data)
            response.raise_for_status()  # Проверка на успешный ответ
            return response.json()  # Вернуть данные в формате JSON
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None

    def update_item(self, item_id, data):
        """Обновление элемента по ID через запрос PUT"""
        try:
            response = requests.put(f"{self.url}/item/{item_id}", json=data)
            response.raise_for_status()  # Проверка на успешный ответ
            return response.json()  # Вернуть обновленные данные
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return None
