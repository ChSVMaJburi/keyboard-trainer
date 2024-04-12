"""Модуль с классом хранящим статистику"""
import global_variables as my_space


class TypingStatistics:
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
        return self.correct / self.time * my_space.SECS_PER_MINUTE

    def get_error_rate(self) -> float:
        """Выдаёт количество ошибок"""
        return self.errors
