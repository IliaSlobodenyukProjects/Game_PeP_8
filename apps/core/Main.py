import pygame
from apps.core.class_hero import Hero
from apps.core.Menu import Menu
from media.levels.level import level1
from media.settings.settings import user_screen_h, user_screen_w
from media.levels.class_platform import Platform
from apps.core.class_enemy import Enemy
from apps.core.class_bird import Bird
from media.captures.actions.another import grass, \
    tree_1, tree_2, tree_3, tree_4, flower_2, flower_1, bg

pygame.init()
win = pygame.display.set_mode(
    (user_screen_w, user_screen_h), pygame.FULLSCREEN
)

bg = pygame.transform.scale(
    bg, (user_screen_w, user_screen_h)
)

clock = pygame.time.Clock()
FPS = 60

eng = []
all_sprites_group = pygame.sprite.Group()  # Группа вообще всех игровы объектов
platform_group = pygame.sprite.Group()  # Группа платформ
enemy_group = pygame.sprite.Group()  # Группа врагов
bot_group = pygame.sprite.Group()  # Группа животных

for i in range(len(enemy_group)):
    eng.append(Enemy)
hero = Hero(
    all_sprites_group, user_screen_h, enemy_group
)  # Создаём персонажа по шаблону из класса

hero_group = pygame.sprite.Group()
hero_group.add(hero)

# def draw_level():
#    Отрисовываем статичный фон
# Создаём персонажа по шаблону из класса
GRASS_sprite = pygame.transform.scale(
    grass, (650, 650)
)  # уменьшение размера травы

tree_1_sprite = pygame.transform.scale(
    tree_1, (250, 250)
)  # уменьшение размера дерева1

tree_2_sprite = pygame.transform.scale(
    tree_2, (450, 450)
)  # уменьшение размера дерева2

tree_3_sprite = pygame.transform.scale(
    tree_3, (650, 650)
)  # уменьшение размера дерева3

tree_4_sprite = pygame.transform.scale(
    tree_4, (465, 465)
)  # уменьшение размера дерева4

flower_1_sprite = pygame.transform.scale(
    flower_1, (150, 150)
)  # уменьшение размера цветка1

flower_2_sprite = pygame.transform.scale(
    flower_2, (125, 125)
)  # уменьшение размера цветка2


def drawWindow():
    win.blit(
        bg, (0, 0)
    )  # фон
    platform_group.draw(
        win
    )  # Отрисвываем уровень
    enemy_group.draw(
        win
    )
    bot_group.draw(
        win
    )  # боты в будущем
    win.blit(
        hero.image, hero.rect
    )  # главный герой
    pygame.display.update()  # обновление экрана


def showMenu():
    #    стартовое меню
    menu = Menu(
        win
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_UP:
                    menu.up()
                if event.key == pygame.K_DOWN:
                    menu.down()
                if event.key == 13:
                    if menu.activeButton == 0:  # Если выбрано "START GAME"
                        return
                    elif menu.activeButton == 1:
                        pygame.quit()

        menu.update()


def draw_level():
    bg.blit(
        tree_1_sprite, tree_1_sprite.get_rect(
            x=635, y=750
        )
    )  # создание дерева1
    bg.blit(
        tree_2_sprite, tree_2_sprite.get_rect(
            x=65, y=550
        )
    )  # создание дерева2
    bg.blit(
        tree_3_sprite, tree_3_sprite.get_rect(
            x=800, y=425
        )
    )  # создание дерева3
    bg.blit(
        tree_4_sprite, tree_4_sprite.get_rect(
            x=1500, y=565
        )
    )  # создание дерева4

    bg.blit(
        flower_1_sprite, flower_1_sprite.get_rect(
            x=1250, y=880
        )
    )  # создание цветка1
    bg.blit(
        flower_2_sprite, flower_2_sprite.get_rect(
            x=120, y=890
        )
    )  # создание цветка2

    bg.blit(
        GRASS_sprite, GRASS_sprite.get_rect(
            x=0, y=630
        )
    )  # создание травы
    bg.blit(
        GRASS_sprite, GRASS_sprite.get_rect(
            x=635, y=630
        )
    )
    bg.blit(
        GRASS_sprite, GRASS_sprite.get_rect(
            x=635 * 2, y=630
        )
    )


def create_platforms():
    # все
    platform_size_x = user_screen_w // len(level1[0])
    platform_size_y = user_screen_h // len(level1)

    x = 0
    y = 0
    for line in level1:
        for b in line:
            if b == "H":
                # Перемещаем ГГ на спавн
                hero.rect.x = x
                hero.rect.y = y
            elif b == 1:  # Создаём спрайт платформы
                Platform(
                    (all_sprites_group, platform_group),
                    x, y, platform_size_x, platform_size_y
                )
            elif b == "E":
                # Создаём спрайт врага
                Enemy(
                    (all_sprites_group, enemy_group),
                    x, y, platform_size_x, platform_size_y
                )
            elif b == "B":
                Bird(
                    (all_sprites_group, bot_group),
                    x, y, platform_size_x, platform_size_y
                )
            x += platform_size_x
        x = 0
        y += platform_size_y


showMenu()
create_platforms()
draw_level()

run = True
while run:
    clock.tick(FPS)  # ограничиваем ФПС
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если нажали на крестикв углу (его не видно в фуллскрин)
            run = False
        if event.type == pygame.KEYDOWN:  #
            if event.key == pygame.K_ESCAPE:
                run = False

    hero.update(
        platform_group
    )  # Обновляем героя

    enemy_group.update(
        hero_group
    )

    bot_group.update()
    drawWindow()

pygame.quit()
