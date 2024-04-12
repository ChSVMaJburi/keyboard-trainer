"""Файл с реализацией TextLoader"""
import os
import random


class TextLoader:
    """Класс, который загружает текст из файла"""

    def __init__(self, directory_path: str) -> None:
        self.texts_path = directory_path
        self.count_of_texts = len(os.listdir(directory_path))

    def load_random_text(self) -> str:
        """Загружает рандомный текст из файла и возвращает его в виде строки."""
        index = random.randint(1, self.count_of_texts)
        with open(f"../{self.texts_path}/{index}.txt", encoding="UTF-8") as text:
            return text.read()
