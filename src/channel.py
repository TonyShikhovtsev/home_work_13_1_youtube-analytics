import requests

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key = "AIzaSyDHgpl7lB3wLwo17yG67V1zkWbZnmm5pWI"

    def fetch_channel_info(self) -> dict:
        """Загрузка информации о канале через API"""
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_data = self.fetch_channel_info()
        if "items" in channel_data and len(channel_data["items"]) > 0:
            snippet = channel_data["items"][0]["snippet"]
            statistics = channel_data["items"][0]["statistics"]

            print("Информация о канале:")
            print(f"Название: {snippet['title']}")
            print(f"Описание: {snippet['description']}")
            print(f"Дата создания: {snippet['publishedAt']}")
            print(f"Количество подписчиков: {statistics['subscriberCount']}")
            print(f"Количество просмотров: {statistics['viewCount']}")
