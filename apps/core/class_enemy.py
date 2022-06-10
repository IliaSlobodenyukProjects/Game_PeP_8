import pygame
from media.settings.settings import User_screen_w
from media.captures.actions.enemy_media import Walk
from media.settings.constants import Enemy_w, Enemy_h, Speed, Gravitation

run_animation = []
# Список, в котором хранятся
# анимации, и из которого они перебираются

for image in Walk:
    run_animation.append(
        pygame.transform.scale(
            image, (
                Enemy_w, Enemy_h)))


class Enemy(
    pygame.sprite.Sprite):
    def __init__(
            self, groups, x, y,
            width, height):

        super().__init__(
            groups)

        self.anim_count = 0
        self.image = run_animation[self.anim_count]
        self.rect = self.image.get_rect(
            x=x, bottom=y + height + 500)
        self.speed_x = 0
        self.left = False
        self.hp = 2

        self.speed_y = 0
        self.on_ground = True
        # Стоит на земле
        self.ground = y + height + 40
        # вычисления для коллизии
        self.y = y
        self.x = x
        self.range = 40
        self.hhp = 0

    def update(
            self, herogroup):

        self.herogroup = herogroup
        keys = pygame.key.get_pressed()

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if not self.left:
            self.speed_x = Speed
            if self.rect.right > User_screen_w:
                self.speed_x = 0
                self.left = True
        else:
            self.speed_x = -Speed
            if self.rect.right < 150:
                self.speed_x = 0
                self.left = False

        if not self.on_ground:
            self.speed_y += Gravitation

        if self.rect.bottom >= self.ground:
            self.rect.bottom = self.ground
            self.on_ground = True
            self.speed_y = 0

        self.animation()

        if keys[pygame.K_e]:
            self.attacka()
            if self.hhp == 9:
                pygame.quit()

    def check_collizion(
            self, platforms):

        if pygame.sprite.spritecollideany(
                self, platforms):
            if self.speed_y != 0:
                if self.speed_y > 0:
                    self.on_ground = True
                self.speed_y = 0
        else:
            self.speed_y += Gravitation

    def animation(
            self):

        if self.speed_x:
            # Если скорость по Х не нулевая, значит я иду
            self.anim_count += 1
            # Счётчик подсчитывает, какую картинку по счёту я должен показать
            if self.anim_count == len(run_animation):
                # если я дошёл до последней картинки в списке картинок
                self.anim_count = 0
                # то обнуляю счётчик, чтобы начать сначала

            self.image = run_animation[self.anim_count]
            # Достаю картинку с нужным номером из списка
            if self.speed_x > 0:
                # Если двигаюсь вправо,
                self.image = pygame.transform.flip(
                    self.image, True, False)
                # то отзеркаливаю картинку персонажа

    def get_coords(
            self):
        return self.x, self.y

    def attacka(
            self):
        hits = pygame.sprite.spritecollide(
            self, self.herogroup, False,
            pygame.sprite.collide_circle)
        if hits:
            self.hhp += 1
            return True
