import pygame
from pygame.draw import *
import math
import random

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 500))
screen.fill((255, 255, 255))

def random_color():
    """Генерация случайного цвета."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_person(surface, x, y):
    """Рисует человечка с центром в точке (x, y)."""
    # Случайные цвета для частей тела
    skin_color = random_color()
    body_color = random_color()
    hair_color = random_color()
    eye_color = random_color()

    # Тело
    circle(surface, body_color, (x, y + 150), 75)  # пузо
    ellipse(surface, skin_color, (x - 75, y - 50, 150, 175))  # лицо

    # Руки
    polygon(surface, skin_color, [(x - 85, y + 100), (x - 95, y + 100), (x - 150, y - 80), (x - 140, y - 80)])  # левая рука
    polygon(surface, skin_color, [(x + 85, y + 100), (x + 95, y + 100), (x + 150, y - 80), (x + 140, y - 80)])  # правая рука

    ellipse(screen, skin_color, (150, 100, 30, 50))  # лодошка1
    ellipse(screen, skin_color, (720, 100, 30, 50))  # лодошка2

    # Лицо
    polygon(surface, (0, 0, 0), [(x + 45, y + 60), (x - 45, y + 60), (x, y + 100)], 5)  # рот (обводка)
    polygon(surface, (255, 0, 0), [(x + 45, y + 60), (x - 45, y + 60), (x, y + 100)])  # рот
    polygon(surface, (255, 100, 100), [(x + 5, y + 40), (x - 5, y + 40), (x, y + 50)])  # нос

    # Волосы
    for angle in range(210, 330, 10):
        x1 = x + 100 * math.cos(math.radians(angle))
        y1 = y+50  - 20 + 100 * math.sin(math.radians(angle))
        x2 = x + 75 * math.cos(math.radians(angle + 5))
        y2 = y + 50 - 20 + 75 * math.sin(math.radians(angle + 5))
        x3 = x + 75 * math.cos(math.radians(angle - 5))
        y3 = y+50 - 20 + 75 * math.sin(math.radians(angle - 5))
        polygon(surface, (0, 0, 0), [(x1, y1), (x2, y2), (x3, y3)], 5)
        polygon(surface, hair_color, [(x1, y1), (x2, y2), (x3, y3)])

    # Глаза
    circle(surface, (0, 0, 0), (x + 25, y + 20), 21)  # правый глаз (обводка)
    circle(surface, (0, 0, 0), (x - 25, y + 20), 21)  # левый глаз (обводка)
    circle(surface, eye_color, (x + 25, y + 20), 20)  # правый глаз
    circle(surface, eye_color, (x - 25, y + 20), 20)  # левый глаз
    circle(surface, (0, 0, 0), (x - 25, y + 20), 5)  # зрачок левого глаза
    circle(surface, (0, 0, 0), (x + 25, y + 20), 5)  # зрачок правого глаза

    # Рукава
    polygon(surface, (0, 0, 0), [(x - 80, y + 70), (x - 50, y + 105), (x - 70, y + 150), (x - 110, y + 140), (x - 110, y + 90)], 5)  # левый рукав (обводка)
    polygon(surface, (0, 0, 0), [(x + 80, y + 70), (x + 50, y + 105), (x + 70, y + 150), (x + 110, y + 140), (x + 110, y + 90)], 5)  # правый рукав (обводка)
    polygon(surface, body_color, [(x - 80, y + 70), (x - 50, y + 105), (x - 70, y + 150), (x - 110, y + 140), (x - 110, y + 90)])  # левый рукав
    polygon(surface, body_color, [(x + 80, y + 70), (x + 50, y + 105), (x + 70, y + 150), (x + 110, y + 140), (x + 110, y + 90)])  # правый рукав

# Рисуем двух человечков
draw_person(screen, 300, 200)  # Первый человечек
draw_person(screen, 600, 200)  # Второй человечек

# Табличка
polygon(screen, (0, 0, 0), [(200, 80), (200, 115), (700, 115), (700, 80)], 5)  # обводка таблички
polygon(screen, (0, 255, 0), [(200, 80), (200, 115), (700, 115), (700, 80)])  # табличка

# Текст на табличке
font = pygame.font.Font(None, 48)
text = font.render("PYTHON is AMAZING", True, (0, 0, 0))
text_rect = text.get_rect(center=(450, 100))
screen.blit(text, text_rect)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()