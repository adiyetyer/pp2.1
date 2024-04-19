import pygame as pg
import random

pg.init()

w, h, fps = 400, 600, 60
is_running, lose = True, False
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Игра-гонки')
clock = pg.time.Clock()

y = 0
ry = 2
step, enemy_step, coin_step, score, score_coin = 5, 5, 5, 0, 0
font = pg.font.SysFont("Verdana", 20)

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
        global step
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.rect.left > 0:
            self.rect.x -= step
        if keys[pg.K_d] and self.rect.right < w:
            self.rect.x += step

class Coin(pg.sprite.Sprite):
    def __init__(self, player_rect):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("coin.png").convert_alpha(), (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, w - 30), -50)
        self.player_rect = player_rect
        self.weight = random.randint(1, 5)  # Вес монеты будет случайным числом от 1 до 5

    def update(self):
        global score_coin, enemy_step, coin_step
        if self.rect.colliderect(self.player_rect):
            score_coin += self.weight  # Добавляем вес монеты к общему счету монет
            self.rect.center = (random.randint(30, w - 30), -50)
            self.weight = random.randint(1, 5)  # Генерируем новый вес для следующей монеты
            # Увеличиваем скорость врагов в зависимости от суммарного веса собранных монет
            if score_coin % 15 == 0:  # Если сумма весов достигла кратного 15 значения
                enemy_step += 1
                coin_step += 1
        else:
            direction = pg.Vector2(self.player_rect.center) - pg.Vector2(self.rect.center)
            direction.normalize_ip()
            self.rect.move_ip(direction * coin_step)

player = Player()
enemies = pg.sprite.Group()
coins = pg.sprite.Group()
for _ in range(5):
    enemies.add(Enemy())

for _ in range(3):
    coins.add(Coin(player.rect))

background_img = pg.image.load("AnimatedStreet.png").convert()
game_over_img = pg.image.load("gameover.png").convert_alpha()
game_over_img = pg.transform.scale(game_over_img, (w, h))

while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    rel_y = y % h
    screen.blit(background_img, (0, rel_y - background_img.get_rect().height))
    if rel_y < h:
        screen.blit(background_img, (0, rel_y))
    y += ry

    for entity in enemies:
        screen.blit(entity.image, entity.rect)
    for coin in coins:
        screen.blit(coin.image, coin.rect)

    screen.blit(player.image, player.rect)

    player.update()

    if pg.sprite.spritecollide(player, enemies, False):
        lose = True

    for entity in enemies:
        entity.rect.y += enemy_step
        if entity.rect.top > h:
            score += 1
            entity.rect.center = (random.randint(30, w - 30), -50)

    if lose:
        screen.blit(game_over_img, (0, 0))

    for coin in coins:
        coin.update()

    coin_score_text = font.render(f'Coins: {score_coin}', True, pg.Color('white'))
    screen.blit(coin_score_text, (10, 10))

    pg.display.flip()

pg.quit()
