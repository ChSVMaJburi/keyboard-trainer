"""Реализован класс Text"""
import sys
from typing import Tuple
from . import global_variables as my_space

import pygame


class TextManager:
    """Класс для управления текстом"""

    def __init__(self, text: str, font_size: int = my_space.FONT_SIZE,
                 color: Tuple[int, int, int] = my_space.BLACK) -> None:
        self.text, self.font, self.font_size, self.color = text, pygame.font.SysFont('Latin Modern Roman',
                                                                                     font_size), font_size, color

    def input_from_gui(self) -> None:
        """Функция для получения строки с графического интерфейса"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def print_to_gui(self, coordinate: Tuple[int, int]) -> None:
        """Функция для вывода в графический интерфейс наш текст"""
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = coordinate
        my_space.screen.blit(text_surface, text_rect)

    def remove_first_letter(self):
        """Удаляет первую букву слова"""
        self.text = self.text[1:]

    def add_letter(self, letter: str) -> None:
        """Добавляет в конец текста новую букву"""
        self.text += letter
