from collections import deque
from typing import Deque, Dict, List

class ConversationMemory:
    def __init__(self, max_message: int = 12):
        self.memory: Deque[Dict[str,str]] = deque(maxlen=max_message)

    def add_user(self, content: str):
        self.memory.append({"role": "user", "content": content})

    def add_model(self, content: str):
        self.memory.append({"role": "model", "content": content})

    def add_user_message(self, content: str):
        """Alias para add_user para compatibilidad"""
        self.add_user(content)

    def get(self) -> List[Dict[str,str]]:
        return list(self.memory)

    def clear(self):
        self.memory.clear()