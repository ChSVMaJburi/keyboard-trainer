"""Модуль с классом для хранения статистики"""
from typing import Tuple


class StorageManager:
    """Класс для сохранения и загрузки статистики"""
    def __init__(self, file_path: str):
        self.path = file_path

    def save_statistics(self, time: float = 0, correct: int = 0, errors: int = 0):
        """Сохранить статистику в файл."""
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(str(time))
            file.write(str(correct))
            file.write(str(errors))

    def load_statistics(self) -> Tuple[float, int, int]:
        """Загрузить статистику из файла и вернуть ее."""
        with open(self.path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return float(lines[0]), int(lines[1]), int(lines[2])
