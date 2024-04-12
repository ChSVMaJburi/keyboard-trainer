"""Основной файл"""
import sys

import pygame
import src.global_variables as my_space
from src.gui_interface import Button, TypingTrainerGUI
from src.storage_manager import StorageManager
from src.text_manager import TextManager


def init_pygame():
    """Файл для начальных базовых действий pygame"""
    pygame.init()
    my_space.screen = pygame.display.set_mode(my_space.DISPLAY_SIZE)
    my_space.screen.fill(my_space.GREY)
    pygame.font.init()
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
        TextManager("Check your typing skills", my_space.FONT_SIZE, my_space.YELLOW).print_to_gui((220, 70))
        start_button.draw_button()
        start_button.change_color_on_hover()
        my_space.screen.blit(keyboard_image, (370, 400))
        pygame.display.update()
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or (
                    event.type == pygame.MOUSEBUTTONDOWN and start_button.rect.collidepoint(mouse_position)):
                started = True
                my_space.screen.fill(my_space.GREY, start_button.rect)
                my_space.screen.fill(my_space.GREY, pygame.Rect(370, 400, 370, 300))
        pygame.display.update()


if __name__ == "__main__":
    init_pygame()
    display_the_start_screen()
    aminov = TypingTrainerGUI()
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over:
                continue
            aminov.input_symbol(event)
            aminov.display_text()
            my_space.screen.fill(my_space.GREY, pygame.Rect(50, 600, 1000, 200))
            aminov.display_statistics()
            if len(aminov.need_text.text) == aminov.correct_index:
                my_space.screen.fill(my_space.GREY, pygame.Rect(220, 70, 600, 170))
                TextManager("Game Over", my_space.FONT_SIZE * 2, my_space.YELLOW).print_to_gui((200, 50))
                StorageManager("statistic.txt").save_statistics(aminov.all_time_stats.time,
                                                                 aminov.all_time_stats.correct,
                                                                 aminov.all_time_stats.errors)
                game_over = True
                break
        pygame.display.update()
