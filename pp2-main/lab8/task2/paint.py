import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
win_width = 1000
win_height = 800
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Рисование')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Параметры рисования
brush_color = BLACK
brush_size = 5
drawing = False
current_shape = []
shapes = []

# Типы фигур
CIRCLE = 'circle'
RECTANGLE = 'rectangle'
LINE = 'line'
SQUARE = 'square'
RIGHT_TRIANGLE = 'right_triangle'
EQUILATERAL_TRIANGLE = 'equilateral_triangle'
RHOMBUS = 'rhombus'

# Выбранная фигура
selected_shape = None

# Шрифты
font = pygame.font.SysFont('Arial', 24)

# Создание кнопок
color_buttons = [
    {'color': BLACK, 'pos': (50, 50), 'label': 'Black'},
    {'color': RED, 'pos': (50, 100), 'label': 'Red'},
    {'color': GREEN, 'pos': (50, 150), 'label': 'Green'},
    {'color': BLUE, 'pos': (50, 200), 'label': 'Blue'},
]

size_buttons = [
    {'size': 5, 'pos': (150, 50), 'label': 'Small'},
    {'size': 10, 'pos': (150, 100), 'label': 'Medium'},
    {'size': 20, 'pos': (150, 150), 'label': 'Large'},
]

shape_buttons = [
    {'shape': CIRCLE, 'pos': (250, 50), 'label': 'Circle'},
    {'shape': RECTANGLE, 'pos': (250, 100), 'label': 'Rectangle'},
    {'shape': LINE, 'pos': (250, 150), 'label': 'Line'},
    {'shape': SQUARE, 'pos': (250, 200), 'label': 'Square'},
    {'shape': RIGHT_TRIANGLE, 'pos': (250, 250), 'label': 'Right Triangle'},
    {'shape': EQUILATERAL_TRIANGLE, 'pos': (250, 300), 'label': 'Equilateral Triangle'},
    {'shape': RHOMBUS, 'pos': (250, 350), 'label': 'Rhombus'},
]

clear_button = {'pos': (50, 250), 'label': 'Clear'}

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
                current_shape = [event.pos]
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Левая кнопка мыши
                drawing = False
                shapes.append((brush_color, brush_size, current_shape, selected_shape))
                current_shape = []
        elif event.type == pygame.MOUSEMOTION and drawing:
            current_shape.append(event.pos)

    # Обработка кнопок
    mouse_pos = pygame.mouse.get_pos()
    for btn in color_buttons:
        rect = pygame.Rect(btn['pos'][0], btn['pos'][1], 100, 40)
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
            brush_color = btn['color']
    for btn in size_buttons:
        rect = pygame.Rect(btn['pos'][0], btn['pos'][1], 100, 40)
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
            brush_size = btn['size']
    for btn in shape_buttons:
        rect = pygame.Rect(btn['pos'][0], btn['pos'][1], 100, 40)
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
            selected_shape = btn['shape']
    clear_rect = pygame.Rect(clear_button['pos'][0], clear_button['pos'][1], 100, 40)
    if clear_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
        shapes = []

    # Рисование на холсте
    win.fill(WHITE)
    for shape_color, shape_size, shape, shape_type in shapes:
        if len(shape) >= 2:
            if shape_type == CIRCLE:
                x1, y1 = shape[0]
                x2, y2 = shape[-1]
                radius = max(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.circle(win, shape_color, shape[0], radius, shape_size)
            elif shape_type == RECTANGLE:
                rect = pygame.Rect(shape[0][0], shape[0][1], shape[-1][0] - shape[0][0], shape[-1][1] - shape[0][1])
                pygame.draw.rect(win, shape_color, rect, shape_size)
            elif shape_type == LINE:
                pygame.draw.lines(win, shape_color, False, shape, shape_size)
            elif shape_type == SQUARE:
                rect = pygame.Rect(shape[0][0], shape[0][1], shape[-1][0] - shape[0][0], shape[-1][0] - shape[0][0])
                pygame.draw.rect(win, shape_color, rect, shape_size)
            elif shape_type == RIGHT_TRIANGLE:
                points = [shape[0], (shape[0][0], shape[-1][1]), shape[-1]]
                pygame.draw.polygon(win, shape_color, points, shape_size)
            elif shape_type == EQUILATERAL_TRIANGLE:
                length = shape[-1][0] - shape[0][0]
                height = int(length * (3 ** 0.5) / 2)
                points = [shape[0], (shape[-1][0], shape[0][1]), ((shape[0][0] + shape[-1][0]) // 2, shape[0][1] - height)]
                pygame.draw.polygon(win, shape_color, points, shape_size)
            elif shape_type == RHOMBUS:
                dx = (shape[-1][0] - shape[0][0]) // 2
                points = [(shape[0][0] + dx, shape[0][1]), (shape[-1][0], shape[0][1] + dx), (shape[0][0] + dx, shape[-1][1]), (shape[0][0], shape[0][1] + dx)]
                pygame.draw.polygon(win, shape_color, points, shape_size)

    # Рисование рамок кнопок
    for btn in color_buttons:
        pygame.draw.rect(win, BLACK, (btn['pos'][0], btn['pos'][1], 100, 40), 2)
    for btn in size_buttons:
        pygame.draw.rect(win, BLACK, (btn['pos'][0], btn['pos'][1], 100, 40), 2)
    for btn in shape_buttons:
        pygame.draw.rect(win, BLACK, (btn['pos'][0], btn['pos'][1], 100, 40), 2)
    pygame.draw.rect(win, BLACK, (clear_button['pos'][0], clear_button['pos'][1], 100, 40), 2)

    # Нанесение текста на кнопки
    for btn in color_buttons:
        text = font.render(btn['label'], True, BLACK)
        win.blit(text, (btn['pos'][0] + 10, btn['pos'][1] + 10))
    for btn in size_buttons:
        text = font.render(btn['label'], True, BLACK)
        win.blit(text, (btn['pos'][0] + 10, btn['pos'][1] + 10))
    for btn in shape_buttons:
        text = font.render(btn['label'], True, BLACK)
        win.blit(text, (btn['pos'][0] + 10, btn['pos'][1] + 10))
    text = font.render(clear_button['label'], True, BLACK)
    win.blit(text, (clear_button['pos'][0] + 10, clear_button['pos'][1] + 10))

    pygame.display.flip()
