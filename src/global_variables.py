"""Класс с константными значениями"""
import pygame

DISPLAY_SIZE = (1024, 768)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 180, 180)
RED = (255, 0, 0)
GREY = (80, 80, 80)
BLOCK_SIZE = 50
LIGHT_GRAY = (192, 192, 192)
BUTTON_MARGIN = -10
TEXT_MARGIN = 0
YELLOW = (255, 255, 100)

RECTANGLE = (550, 332, 154, 72)

screen: pygame.surface.Surface
FONT_SIZE = 50
GAME_OVER: pygame.font.Font
FONT: pygame.font.Font

SECS_PER_MINUTE = 60