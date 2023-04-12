from abc import ABC, abstractmethod


class AbstractDataStorage(ABC):
    @abstractmethod
    def load_file(self, file_key: str) -> bytes:
        """Load file"""

    @abstractmethod
    def save_file(self, file_key: str, file_content: bytes) -> None:
        """Save file"""
