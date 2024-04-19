import pygame as pg
import random

# Инициализация Pygame
pg.init()

# Установка размеров окна и частоты обновления кадров в секунду
w, h, fps = 400, 600, 60
is_running, lose = True, False
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Игра-гонки')
clock = pg.time.Clock()

# Подгрузка фонового изображения и изображения для экрана окончания игры
y = 0
ry = 2
step, enemy_step, score, score_coin = 5, 5, 0, 0
game_over_img = pg.image.load("gameover.png").convert()
bg = pg.image.load("AnimatedStreet.png").convert()
game_over_img = pg.transform.scale(game_over_img, (w, h))

# Загрузка шрифта для отображения счета
font = pg.font.SysFont("Verdana", 20)

# Классы для игровых объектов
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), -50)

    def update(self):
        global score
        self.rect.y += enemy_step
        if self.rect.top > h:
            score += 1
            self.rect.center = (random.randint(30, w - 30), -50)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (w // 2, h - 70)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.rect.left > 0:
            self.rect.x -= step
        if keys[pg.K_d] and self.rect.right < w:
            self.rect.x += step

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
       # Загружаем изображение
        original_image = pg.image.load("coin.png").convert_alpha()
        # Уменьшаем изображение до нужного размера, например до 20x20 пикселей
        self.image = pg.transform.scale(original_image, (20, 20))
        self.rect = self.image.get_rect()
        # Задаем рандомные координаты для монетки
        self.rect.center = (random.randint(30, w - 30), random.randint(30, h - 130))
# Создание игровых объектов
player = Player()
enemies = pg.sprite.Group()
coins = pg.sprite.Group()
for _ in range(5):  # Создание нескольких врагов для увеличения сложности игры
    enemies.add(Enemy())
coins.add(Coin())

# Основной игровой цикл
while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    # Прокрутка фона
    rel_y = y % bg.get_rect().height
    screen.blit(bg, (0, rel_y - bg.get_rect().height))
    if rel_y < h:
        screen.blit(bg, (0, rel_y))
    y += ry

    # Логика игры
    player.update()
    enemies.update()
    coins.update()

    # Проверка на столкновения
    if pg.sprite.spritecollide(player, enemies, False):
        lose = True

    for coin in coins:
        if pg.sprite.collide_rect(player, coin):
            score_coin += 1
            coin.kill()
            coins.add(Coin())

    # Отрисовка всех объектов
    for entity in enemies:
        screen.blit(entity.image, entity.rect)
    for coin in coins:
        screen.blit(coin.image, coin.rect)
    screen.blit(player.image, player.rect)

    # Отображение счета
    coin_score_text = font.render(f'Монеты: {score_coin}', True, pg.Color('black'))
    screen.blit(coin_score_text, (10, 10))

    # Проверка на окончание игры
    if lose:
        screen.blit(game_over_img, (0, 0))

    pg.display.flip()

pg.quit()