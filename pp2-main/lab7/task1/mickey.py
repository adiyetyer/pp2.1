import pygame
import sys
from datetime import datetime

# Инициализация Pygame
pygame.init()

# Установка размера окна и часов
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
clock_face = pygame.image.load('mickey.jpg').convert_alpha()  # Путь к изображению циферблата
minute_hand = pygame.image.load('minutes.png').convert_alpha()  # Путь к изображению минутной стрелки
second_hand = pygame.image.load('seconds.png').convert_alpha()  # Путь к изображению секундной стрелки
center_of_clock = (400, 300)  # Центр циферблата

# Функция для рисования стрелок
def draw_hand(image, angle):
    # Поворот изображения стрелки
    rotated_image = pygame.transform.rotate(image, angle)
    # Получение нового прямоугольника, который ограничивает повернутое изображение
    new_rect = rotated_image.get_rect(center=center_of_clock)
    # Рисование стрелки
    screen.blit(rotated_image, new_rect.topleft)

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Получение текущего времени
    now = datetime.now()
    seconds = now.second + now.microsecond / 1000000
    minutes = now.minute + now.hour * 60 + seconds / 60

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Рисование циферблата
    screen.blit(clock_face, (0, 0))

    # Расчет углов для стрелок
    minute_angle = (minutes % 60) / 60 * 360
    second_angle = seconds / 60 * 360

    # Рисование стрелок
    draw_hand(minute_hand, -minute_angle)  # Минутная стрелка
    draw_hand(second_hand, -second_angle)  # Секундная стрелка

    # Обновление экрана
    pygame.display.flip()
    # Ограничение кадров в секунду
    pygame.time.Clock().tick(60)
