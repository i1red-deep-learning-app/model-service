from model_service.domain.data_storage.abstract_data_storage import AbstractDataStorage
from model_service.domain.data_storage.exceptions import LoadingFailedException, SavingFailedException


class FakeDataStorage(AbstractDataStorage):
    _files: dict[str, bytes]

    def __init__(self) -> None:
        self._files = {}

    def load_file(self, file_key: str) -> bytes:
        if file_key not in self._files:
            raise LoadingFailedException("File not present")

        return self._files[file_key]

    def save_file(self, file_key: str, file_content: bytes) -> None:
        if file_key in self._files:
            raise SavingFailedException(f"File with {file_key=} is already present")

        self._files[file_key] = file_content
