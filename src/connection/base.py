import requests

class APIConnection:
    def __init__(self, API_url):
        self.url = API_url

    def get_item(self, item_id):
        try:
            response = requests.get(f"{self.url}/item/{item_id}")
            response.raise_for_status()
            print('success')
            return response.json()
        except requests.exceptions.HTTPError as err:
            if response.status_code == 404:
                print('id error')
            else:
                print(f"HTTP error occurred: {err}")

    def create_item(self, data):
        try:
            response = requests.post(f"{self.url}/item", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")

    def update_item(self, item_id, data):
        try:
            response = requests.put(f"{self.url}/item/{item_id}", json=data)
            response.raise_for_status()
            print('success')
            return response.json()
        except requests.exceptions.HTTPError as err:
            if response.status_code == 404:
                print('id error')
            else:
                print(f"HTTP error occurred: {err}")
