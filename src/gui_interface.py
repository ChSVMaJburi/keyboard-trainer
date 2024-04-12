"""Реализация класса для отображения графического интерфейса"""
from typing import Tuple, List

import pygame
import src.global_variables as my_space


class TypingTrainerGUI:
    def __init__(self):
        pass

    def display_text(self, text: str):
        """Отобразить текст для набора."""
        pass

    def update_statistics(self, errors: int, typing_speed: float):
        """Обновить статистику ошибок и скорости печати."""
        pass

    def block_invalid_characters(self, invalid_characters: List[str]):
        """Блокировать неправильные символы в поле ввода."""
        pass


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
        print(self.text_position)
        print(self.draw)
        print(self.rect)
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


def display_text(text: str, offset: Tuple[int, int], text_color: Tuple[int, int, int]):
    """Отображает текст на экране."""
    text_surface = my_space.FONT.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = offset
    my_space.screen.blit(text_surface, text_rect)
