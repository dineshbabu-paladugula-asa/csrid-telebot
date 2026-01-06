class SimpleStorage:
    def __init__(self):
        self._data = {}

    def save_response(self, chat_id: int, data: dict):
        self._data[chat_id] = data

    def get_response(self, chat_id: int) -> dict:
        return self._data.get(chat_id)

    def update_response(self, chat_id: int, key: str, value):
        if chat_id not in self._data:
            self._data[chat_id] = {}
        self._data[chat_id][key] = value

    def get_all_data(self):
        return self._data

# Global instance
storage = SimpleStorage()
