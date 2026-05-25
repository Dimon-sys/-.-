import pygame
import sys
import math
import datetime

pygame.init()

FPS = 1
WIN_WIDTH = 500
WIN_HEIGHT = 500
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
BLACK = (0, 0, 0, 0)
RED = (255, 0, 0)
CENTER = (WIN_WIDTH//2, WIN_HEIGHT//2)
RADIUS = 180
SEC_LENGTH = 150
MIN_LENGTH = 120
HOUR_LENGTH = 90

clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

def get_clock_angles():
    #возвращает углы в градусах для стрелок на основе текущего системного времени
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute + seconds / 60.0
    hours = (now.hour % 12) + minutes / 60.0

    sec_angle = seconds * 6            # 360° / 60 сек
    min_angle = minutes * 6            # 360° / 60 мин
    hour_angle = hours * 30            # 360° / 12 ч

    return hour_angle, min_angle, sec_angle


#Цикл обработки событий
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill(WHITE)

    pygame.draw.circle(sc, BLACK, CENTER, 200, 3)
    pygame.draw.circle(sc, BLACK, CENTER, RADIUS, 1)
    pygame.draw.circle(sc, BLACK, CENTER, 2, 1)

    #Рисуем деления
    for i in range(60):
        angle_deg = i * 6  # 360/60 = 6 градусов на минуту
        angle_rad = math.radians(angle_deg - 90)
        # Внутренняя и внешняя точки деления
        inner_radius = RADIUS - 15
        outer_radius = RADIUS - 5

        x1 = CENTER[0] + inner_radius * math.cos(angle_rad)
        y1 = CENTER[1] + inner_radius * math.sin(angle_rad)
        x2 = CENTER[0] + outer_radius * math.cos(angle_rad)
        y2 = CENTER[1] + outer_radius * math.sin(angle_rad)
        pygame.draw.line(sc, BLACK, (x1, y1), (x2, y2), 3 if i % 5 == 0 else 1)

        #числа на циферблате
        if i % 5 == 0:
            number_radius = RADIUS - 35
            number_x = CENTER[0] + number_radius * math.cos(angle_rad)
            number_y = CENTER[1] + number_radius * math.sin(angle_rad)
            number = (i // 5) if (i // 5) != 0 else 12
            font = pygame.font.SysFont(None, 20)
            text = font.render(str(number), True, BLACK)
            text_rect = text.get_rect(center=(number_x, number_y))
            sc.blit(text, text_rect)

    hour_angle, min_angle, sec_angle = get_clock_angles()

    #секундная стрелка
    sec_rad = math.radians(sec_angle-90)  # -90 чтобы 0° смотрело вверх
    sec_x = CENTER[0] + SEC_LENGTH * math.cos(sec_rad)
    sec_y = CENTER[1] + SEC_LENGTH * math.sin(sec_rad)
    pygame.draw.line(sc, RED, CENTER, (sec_x, sec_y), 1)

    #минутная стрелка
    min_rad = math.radians(min_angle-90)
    min_x = CENTER[0] + MIN_LENGTH * math.cos(min_rad)
    min_y = CENTER[1] + MIN_LENGTH * math.sin(min_rad)
    pygame.draw.line(sc, BLACK, CENTER, (min_x, min_y), 3)

    #часовая стрелка
    hour_rad = math.radians(hour_angle-90)
    hour_x = CENTER[0] + HOUR_LENGTH * math.cos(hour_rad)
    hour_y = CENTER[1] + HOUR_LENGTH * math.sin(hour_rad)
    pygame.draw.line(sc, BLACK, CENTER, (hour_x, hour_y), 5)



    pygame.display.flip()
    clock.tick(FPS)