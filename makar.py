import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Цвета
grey = (169, 169, 169)    # Серый для зайца
dgrey = (150, 150, 150)    # Серый для головы
black = (0, 0, 0)         # Черный для контуров, глаз и усов
pink = (255, 182, 193)    # Розовый для ушей
light_pink = (255, 228, 225)  # Светло-розовый для носа
white = (255, 255, 255)   # Белый для белков глаз

# Функции для рисования
def draw_body(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_head(surface, x, y, size, color):
    circle(surface, color, (x, y), size // 2)

def draw_ear(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_leg(surface, x, y, width, height, color):
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))

def draw_eye(surface, x, y, size, color):
    circle(surface, color, (x, y), size)

def draw_nose(surface, x, y, size, color):
    polygon(surface, color, [(x, y), (x - size // 2, y + size), (x + size // 2, y + size)])

def draw_whiskers(surface, x, y):
    line(surface, black, (x + 5, y), (x + 20, y + 10), 2)
    line(surface, black, (x + 5, y), (x + 25, y + 5), 2)
    line(surface, black, (x + 5, y), (x + 27, y), 2)
    line(surface, black, (x + 5, y), (x + 23, y - 5), 2)  # Усы справа
    line(surface, black, (x - 5, y), (x - 20, y + 10), 2)
    line(surface, black, (x - 5, y), (x - 25, y + 5), 2)
    line(surface, black, (x - 5, y), (x - 27, y), 2)
    line(surface, black, (x - 5, y), (x - 23, y - 5), 2)  # Усы слева

# Основной цикл
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # Заполнение фона
    screen.fill((135, 206, 250))  # Небесно-голубой фон

    # Рисуем зайца
    draw_leg(screen, 150, 350, 35, 50, dgrey)  # Левая нога зад
    draw_leg(screen, 250, 350, 35, 50, dgrey)  # Правая нога зад

    draw_body(screen, 200, 290, 160, 150, grey)  # Тело
    draw_head(screen, 200, 200, 90, dgrey)         # Голова
    draw_ear(screen, 175, 120, 45, 110, grey)  # Левое ухо
    draw_ear(screen, 225, 120, 45, 110, grey)  # Правое ухо
    draw_ear(screen, 175, 120, 30, 100, pink)  # Левое ухо
    draw_ear(screen, 225, 120, 30, 100, pink)  # Правое ухо
    draw_leg(screen, 180, 350, 35, 90, dgrey)  # Левая нога
    draw_leg(screen, 220, 350, 35, 90, dgrey)  # Правая нога

    # Рисуем глаза
    draw_eye(screen, 180, 190, 10, black)           # Левый глаз
    draw_eye(screen, 220, 190, 10, black)           # Правый глаз

    # Рисуем нос
    draw_nose(screen, 200, 220, 10, light_pink)     # Нос

    # Рисуем усы
    draw_whiskers(screen, 200, 225)                  # Усы

    # Обновление дисплея
    pygame.display.update()

pygame.quit()
