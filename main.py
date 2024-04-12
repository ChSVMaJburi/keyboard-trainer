"""Основной файл"""
import sys

import pygame
import src.global_variables as my_space
from src.gui_interface import display_text, Button


def init_pygame():
    """Файл для начальных базовых действий pygame"""
    pygame.init()
    my_space.screen = pygame.display.set_mode(my_space.DISPLAY_SIZE)
    my_space.screen.fill(my_space.GREY)
    my_space.FONT = pygame.font.SysFont('Latin Modern Roman', my_space.FONT_SIZE)
    pygame.display.set_caption("Typing Trainer")
    pygame.display.set_icon(pygame.image.load('images/icon.png'))


def display_the_start_screen() -> None:
    """"Создает кнопку "START GAME", рисует ее на экране и обрабатывает события мыши"""
    started = False
    start_button = Button((300, 300), "START TYPING")
    keyboard_image = pygame.image.load('images/keyboard_image.png')
    # keyboard_image = pygame.transform.scale(keyboard_image, (300, 200))
    while not started:
        display_text("Check your typing skills", (220, 70), my_space.WHITE)
        start_button.draw_button()
        start_button.change_color_on_hover()
        my_space.screen.blit(keyboard_image, (370, 400))
        pygame.display.update()
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  start_button.rect.collidepoint(mouse_position)):
                started = True
                my_space.screen.fill(my_space.GREY, start_button.rect)
                my_space.screen.fill(my_space.GREY, pygame.Rect(370, 400, 370, 300))
        pygame.display.update()


if __name__ == "__main__":
    init_pygame()
    pygame.font.init()
    display_the_start_screen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
