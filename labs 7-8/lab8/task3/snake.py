import pygame
import time
import random

pygame.init()

window_x = 720
window_y = 480
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Улучшенная Змейка')

# Цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
direction = 'RIGHT'
change_to = direction
snake_speed = 15

score = 0
level = 1
level_up_score = 3

# Функция создания фрукта
def create_fruit():
    weight = random.choice([10, 20, 30])  # Вес фрукта
    position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    spawn_time = pygame.time.get_ticks()
    return {'position': position, 'weight': weight, 'spawn_time': spawn_time, 'timer': 5000}

fruit = create_fruit()

# Функция отображения счета и уровня
def show_score_and_level():
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render('Score: ' + str(score) + ' Level: ' + str(level), True, white)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Функция окончания игры
def game_over():
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render('Your Score is: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

fps_controller = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    # Обновление позиции головы змеи
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10

    # Рост змейки
    snake_body.insert(0, list(snake_position))
    if snake_position == fruit['position']:
        score += fruit['weight']
        if score % (level_up_score * level) == 0:  # Проверяем, достигли ли мы условия для перехода на следующий уровень
            level += 1
            snake_speed += 1  # Увеличиваем скорость змейки
        fruit = create_fruit()
    else:
        snake_body.pop()

    # Проверка исчезновения фрукта
    if pygame.time.get_ticks() - fruit['spawn_time'] > fruit['timer']:
        fruit = create_fruit()

    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(fruit['position'][0], fruit['position'][1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x-10 or snake_position[1] < 0 or snake_position[1] > window_y-10 or snake_position in snake_body[1:]:
        game_over()

    show_score_and_level()

    pygame.display.update()

    fps_controller.tick(snake_speed)
