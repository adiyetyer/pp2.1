import pygame, sys
pygame.init()
scr_width = 800
scr_height = 600
fps = 100
timer = pygame.time.Clock()
screen = pygame.display.set_mode([scr_width, scr_height])
pygame.display.set_caption('Живопись')
size_rn = 5
color_rn = 'white'
painting = []


# Меню инструментов
def menu(size, color):
    pygame.draw.rect(screen, 'gray', [0, 0, scr_width, 70])
    pygame.draw.line(screen, 'black', (0, 70), (scr_width, 70), 3)
    sizes = [20, 15, 10, 5]  # Размеры кистей
    positions = [35, 95, 155, 215]  # Позиции кистей
    brushes = []
    for i, s in enumerate(sizes):
        x = 10 + i * 60
        rect = pygame.draw.rect(screen, 'black', [x, 10, 50, 50])
        pygame.draw.circle(screen, 'white', (positions[i], 35), s/2)
        brushes.append(rect)
        if size == s:
            pygame.draw.rect(screen, 'green', [x, 10, 50, 50], 3)

    # Отображение текущего цвета
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 5)
    
    # Палитра цветов
    colors = []
    rgb = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 255, 255), (0, 0, 0)]
    color_positions = [(scr_width - 35, 10), (scr_width - 35, 35), (scr_width - 60, 10), (scr_width - 60, 35), (scr_width - 85, 10), (scr_width - 85, 35)]
    for i, pos in enumerate(color_positions):
        rect = pygame.draw.rect(screen, rgb[i], [pos[0], pos[1], 25, 25])
        colors.append(rect)
    
    return brushes, colors, rgb

# Рисование на холсте
def paint(paints):
    for color, pos, size in paints:
        pygame.draw.circle(screen, color, pos, size)

while True:
    timer.tick(fps)
    screen.fill('white')
    
    mousepos = pygame.mouse.get_pos()
    leftmouse = pygame.mouse.get_pressed()[0]
    
    if mousepos[1] > 70 and leftmouse:
        painting.append((color_rn, mousepos, size_rn))
    
    paint(painting)
    
    if mousepos[1] > 70:
        pygame.draw.circle(screen, color_rn, mousepos, size_rn)
    
    brushes, colors, rgb = menu(size_rn, color_rn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, brush in enumerate(brushes):
                    if brush.collidepoint(event.pos):
                        size_rn = sizes[i]
                for i, color in enumerate(colors):
                    if color.collidepoint(event.pos):
                        color_rn = rgb[i]
    
    pygame.display.update()
