import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 500))
screen.fill((255, 255, 255))

# Первый человек
ellipse(screen, (255, 192, 203), (240, 130, 30, 50))  # левая рука
ellipse(screen, (255, 192, 203), (520, 130, 30, 50))  # правая рука
polygon(screen, (0, 0, 0), [(220, 130), (220, 165), (580, 165), (580, 130)], 5)  # обводка таблички
polygon(screen, (0, 255, 0), [(220, 130), (220, 165), (580, 165), (580, 130)])  # табличка
polygon(screen, (255, 192, 203), [(315, 350), (305, 350), (250, 170), (260, 170)])  # левая рука
polygon(screen, (255, 192, 203), [(485, 350), (495, 350), (540, 170), (530, 170)])  # правая рука
circle(screen, (250, 120, 50), (400, 400), 75)  # тело
ellipse(screen, (255, 192, 203), (325, 200, 150, 175))  # лицо
polygon(screen, (0, 0, 0), [(445, 310), (355, 310), (400, 350)], 5)  # рот
polygon(screen, (255, 0, 0), [(445, 310), (355, 310), (400, 350)])  # рот
polygon(screen, (255, 100, 100), [(405, 290), (395, 290), (400, 300)])  # нос
# волосы
for angle in range(210, 330, 10):
    x1 = 400 + 100 * math.cos(math.radians(angle))
    y1 = 280 + 100 * math.sin(math.radians(angle))
    x2 = 400 + 75 * math.cos(math.radians(angle + 5))
    y2 = 280 + 75 * math.sin(math.radians(angle + 5))
    x3 = 400 + 75 * math.cos(math.radians(angle - 5))
    y3 = 280 + 75 * math.sin(math.radians(angle - 5))
    polygon(screen, (0, 0, 0), [(x1, y1), (x2, y2), (x3, y3)], 5)
    polygon(screen, (177, 31, 220), [(x1, y1), (x2, y2), (x3, y3)])
circle(screen, (0, 0, 0), (425, 270), 21)  # правый глаз
circle(screen, (0, 0, 0), (375, 270), 21)  # левый глаз
circle(screen, (114, 170, 255), (425, 270), 20)  # правый глаз
circle(screen, (114, 170, 255), (375, 270), 20)  # левый глаз
circle(screen, (0, 0, 0), (375, 270), 5)  # зрачок левого глаза
circle(screen, (0, 0, 0), (425, 270), 5)  # зрачок правого глаза
polygon(screen, (0, 0, 0), [(320, 320), (350, 355), (330, 400), (290, 390), (290, 340)], 5)  # обводка левого рукава
polygon(screen, (0, 0, 0), [(480, 320), (450, 355), (470, 400), (510, 390), (510, 340)], 5)  # обводка правого рукава
polygon(screen, (250, 120, 50), [(320, 320), (350, 355), (330, 400), (290, 390), (290, 340)])  # левый рукав
polygon(screen, (250, 120, 50), [(480, 320), (450, 355), (470, 400), (510, 390), (510, 340)])  # правый рукав

# Второй человек
ellipse(screen, (255, 192, 203), (540, 130, 30, 50))  # левая рука
ellipse(screen, (255, 192, 203), (820, 130, 30, 50))  # правая рука
polygon(screen, (0, 0, 0), [(520, 130), (520, 165), (880, 165), (880, 130)], 5)  # обводка таблички
polygon(screen, (0, 255, 0), [(520, 130), (520, 165), (880, 165), (880, 130)])  # табличка
polygon(screen, (255, 192, 203), [(615, 350), (605, 350), (550, 170), (560, 170)])  # левая рука
polygon(screen, (255, 192, 203), [(785, 350), (795, 350), (840, 170), (830, 170)])  # правая рука
circle(screen, (250, 120, 50), (700, 400), 75)  # тело
ellipse(screen, (255, 192, 203), (625, 200, 150, 175))  # лицо
polygon(screen, (0, 0, 0), [(745, 310), (655, 310), (700, 350)], 5)  # рот
polygon(screen, (255, 0, 0), [(745, 310), (655, 310), (700, 350)])  # рот
polygon(screen, (255, 100, 100), [(705, 290), (695, 290), (700, 300)])  # нос
# волосы
for angle in range(210, 330, 10):
    x1 = 700 + 100 * math.cos(math.radians(angle))
    y1 = 280 + 100 * math.sin(math.radians(angle))
    x2 = 700 + 75 * math.cos(math.radians(angle + 5))
    y2 = 280 + 75 * math.sin(math.radians(angle + 5))
    x3 = 700 + 75 * math.cos(math.radians(angle - 5))
    y3 = 280 + 75 * math.sin(math.radians(angle - 5))
    polygon(screen, (0, 0, 0), [(x1, y1), (x2, y2), (x3, y3)], 5)
    polygon(screen, (177, 31, 220), [(x1, y1), (x2, y2), (x3, y3)])
circle(screen, (0, 0, 0), (725, 270), 21)  # правый глаз
circle(screen, (0, 0, 0), (675, 270), 21)  # левый глаз
circle(screen, (114, 170, 255), (725, 270), 20)  # правый глаз
circle(screen, (114, 170, 255), (675, 270), 20)  # левый глаз
circle(screen, (0, 0, 0), (675, 270), 5)  # зрачок левого глаза
circle(screen, (0, 0, 0), (725, 270), 5)  # зрачок правого глаза
polygon(screen, (0, 0, 0), [(620, 320), (650, 355), (630, 400), (590, 390), (590, 340)], 5)  # обводка левого рукава
polygon(screen, (0, 0, 0), [(780, 320), (750, 355), (770, 400), (810, 390), (810, 340)], 5)  # обводка правого рукава
polygon(screen, (250, 120, 50), [(620, 320), (650, 355), (630, 400), (590, 390), (590, 340)])  # левый рукав
polygon(screen, (250, 120, 50), [(780, 320), (750, 355), (770, 400), (810, 390), (810, 340)])  # правый рукав

# Текст на табличке
font = pygame.font.Font(None, 48)
text = font.render("PYTHON is AMAZING", True, (0, 0, 0))
text_rect = text.get_rect(center=(450, 150))
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