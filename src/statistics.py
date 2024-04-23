"""Модуль с реализацией класса TypingStatistics"""
from . import global_variables as my_space


class TypingStatistics:
    """Класс для управления статистикой печати"""

    def __init__(self, time: float = 0, correct: int = 0, errors: int = 0):
        self.time, self.correct, self.errors = time, correct, errors

    def add_error(self) -> None:
        """Обновить количество ошибок."""
        self.errors += 1

    def add_correct(self, time_spent: float):
        """Добавить одну верную букву"""
        self.time += time_spent
        self.correct += 1

    def get_typing_speed(self) -> float:
        """Выдать скорость печати."""
        if self.time == 0:
            return 0
        return round(self.correct * my_space.SECS_PER_MINUTE / self.time, 2)

    def get_error_rate(self) -> float:
        """Выдаёт количество ошибок"""
        return self.errors
