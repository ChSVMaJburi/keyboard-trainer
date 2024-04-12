"""Реализация класса для отображения графического интерфейса"""
import sys
from typing import Tuple, List

import pygame
import src.global_variables as my_space
from src.statistics import TypingStatistics
from src.storage_manager import StorageManager
from src.text_manager import TextManager
from src.text_loader import TextLoader
from datetime import time, datetime


class TypingTrainerGUI:
    def __init__(self):
        self.need_text = TextManager(TextLoader("./texts").load_random_text(), 25, my_space.WHITE)
        self.cur_text = TextManager("", 25, my_space.GREEN)
        self.all_time_stats = TypingStatistics(*StorageManager("./statistic.txt").load_statistics())
        self.cur_stats = TypingStatistics(0, 0, 0)
        self.time = datetime.now()
        self.correct_index = 0

    def display_text(self) -> None:
        """Отобразить текущий текст в графический интерфейс"""
        TextManager("Text:", 30, my_space.RED).print_to_gui((20, 200))
        self.need_text.print_to_gui((20, 250))
        TextManager("Your text:", 30, my_space.RED).print_to_gui((20, 300))
        self.cur_text.print_to_gui((20, 350))

    def display_statistics(self):
        """Отобразить статистику ошибок и скорости печати."""
        TextManager(f"Current Cpm: {self.cur_stats.get_typing_speed()}", 30, my_space.YELLOW).print_to_gui((25, 600))
        TextManager(f"Current errors: {self.cur_stats.get_error_rate()}", 30, my_space.YELLOW).print_to_gui((25, 635))
        TextManager(f"All time Cpm: {self.all_time_stats.get_typing_speed()}", 30, my_space.YELLOW).print_to_gui(
            (600, 600))
        TextManager(f"All time errors: {self.all_time_stats.get_error_rate()}", 30, my_space.YELLOW).print_to_gui(
            (600, 635))

    def input_symbol(self, event: pygame.event.Event) -> bool:
        """Попытка ввести символ"""
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type != pygame.KEYDOWN or event.key in (pygame.K_BACKSPACE, pygame.K_LSHIFT, pygame.K_RSHIFT):
            return False
        if event.unicode == self.need_text.text[self.correct_index]:
            self.cur_text.add_letter(event.unicode)
            self.correct_index += 1
            diff = (datetime.now() - self.time).total_seconds()
            self.cur_stats.add_correct(diff)
            self.all_time_stats.add_correct(diff)
            self.time = datetime.now()
        else:
            self.cur_stats.add_error()
            self.all_time_stats.add_error()


class Button:
    """
    Создает кнопки
    """

    def __init__(self, offset: Tuple[int, int], text: str):
        self.text = text
        self.button_width, self.button_height = my_space.FONT.size(self.text)

        self.coordinate = offset
        self.draw = (self.coordinate[0] + my_space.BUTTON_MARGIN, self.coordinate[1],
                     self.button_width - 2 * my_space.BUTTON_MARGIN, self.button_height - 2 * my_space.BUTTON_MARGIN)
        self.rect = pygame.Rect(self.draw)
        self.text_position = (self.coordinate[0] + self.button_width // 2 - self.button_width // 2 -
                              my_space.TEXT_MARGIN,
                              self.coordinate[1] + self.button_height // 2 - self.button_height // 2 -
                              my_space.TEXT_MARGIN)

        self.default_color = my_space.LIGHT_GRAY

    def draw_button(self, color: Tuple[int, int, int] = None) -> None:
        """
        Рисует кнопку в виде цветного прямоугольника
        Аргументы:
            цвет (tuple): цвет кнопки. По умолчанию значение равно None
        """
        if not color:
            color = self.default_color
        pygame.draw.rect(my_space.screen, color, self.draw)
        text = my_space.FONT.render(self.text, True, my_space.RED)
        my_space.screen.blit(text, self.text_position)

    def change_color_on_hover(self) -> None:
        """
        Изменение цвета кнопки при наведении курсора мыши на нее
        """
        coord = pygame.mouse.get_pos()
        if self.rect.collidepoint(coord):
            self.draw_button(my_space.GREY)
