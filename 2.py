import pygame
from pygame.draw import *
import math
import sys

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 500))
screen.fill((255, 255, 255))



ellipse(screen,(255,192,203),(290, 130, 30,50 ))#лодошка1
ellipse(screen,(255,192,203),(570, 130, 30,50 ))#лодошка2
polygon(screen, (0, 0, 0), [(270, 130), (270, 165), (630, 165), (630, 130)],5)  # обводка зеленка
polygon(screen, (0, 255, 0), [(270, 130), (270, 165), (630, 165), (630, 130)])  # зеленка
polygon(screen, (255,192,203), [(365, 350), (355, 350), (300, 170), (310, 170)])  #рука1
polygon(screen, (255,192,203), [(535, 350), (545, 350), (590, 170), (580, 170)])  #рука1
circle(screen, (250, 120, 50), (450,400 ), 75)  #пузо
ellipse(screen,(255,192,203),(375, 200, 150,175 ))#лицо
polygon(screen, (0,0,0), [(495, 310), (405, 310), (450, 350)],5)  #рот
polygon(screen, (255,0,0), [(495, 310), (405, 310), (450, 350)])  #рот
polygon(screen, (255,100,100), [(455, 290), (445, 290), (450, 300)])  #нос
#volos
for angle in range(210,330,10):
    x1=450+100*math.cos(math.radians(angle))
    y1=280+100*math.sin(math.radians(angle))
    x2 = 450 + 75 * math.cos(math.radians(angle+5))
    y2 = 280 + 75 * math.sin(math.radians(angle+5))
    x3 = 450 + 75 * math.cos(math.radians(angle - 5))
    y3 = 280 + 75 * math.sin(math.radians(angle - 5))
    polygon(screen, (0, 0, 0), [(x1, y1), (x2, y2), (x3, y3)],5)
    polygon(screen,(177,31,220),[(x1,y1),(x2,y2),(x3,y3)])
circle(screen, (0, 0, 0), (475,270 ), 21)  #глаз2
circle(screen, (0, 0, 0), (425,270 ), 21)  #глаз1
circle(screen, (114, 170, 255), (475,270 ), 20)  #глаз2
circle(screen, (114, 170, 255), (425,270 ), 20)  #глаз1
circle(screen, (0, 0, 0), (425,270 ), 5)  #глаз3
circle(screen, (0, 0, 0), (475,270 ), 5)  #глаз3
polygon(screen, (0, 0, 0), [(370, 320), (400, 355), (380, 400), (340, 390),(340,340)],5)  # обводка_рукав1
polygon(screen, (0, 0, 0), [(530, 320), (500, 355), (520, 400), (560, 390),(560,340)],5)  #обводка рукав2
polygon(screen, (250, 120, 50), [(370, 320), (400, 355), (380, 400), (340, 390),(340,340)])  #рукав1
polygon(screen, (250, 120, 50), [(530, 320), (500, 355), (520, 400), (560, 390),(560,340)])  #рукав2
font=pygame.font.Font(None, 48)
text = font.render("PYTHON is AMAZING",True,(0,0,0))
text_rect = text.get_rect(center=(450,150))
screen.blit(text,text_rect)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()