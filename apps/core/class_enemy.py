import pygame
from media.settings.settings import user_screen_w
from media.captures.actions.enemy_media import walk
from media.settings.set import enemy_w, enemy_h, speed

run_animation = []  # ghjdthrf

for image in walk:
    run_animation.append(
        pygame.transform.scale(
            image, (
                enemy_w, enemy_h)))


class Enemy(
    pygame.sprite.Sprite):
    def __init__(
            self, groups, x, y,
            width, height):

        super().__init__(
            groups)

        self.animCount = 0
        self.image = run_animation[self.animCount]
        self.rect = self.image.get_rect(
            x=x, bottom=y + height + 500)
        self.speedX = 0
        self.Left = False
        self.hp = 2

        self.speedY = 0
        self.grav = 2
        self.on_ground = True  # Стоит на земле
        self.ground = y + height + 40
        self.y = y
        self.x = x
        self.range = 40
        self.hhp = 0

    def update(
            self, herogroup):

        self.herogroup = herogroup
        keys = pygame.key.get_pressed()

        self.rect.x += self.speedX
        self.rect.y += self.speedY

        if not self.Left:
            self.speedX = speed
            if self.rect.right > user_screen_w:
                self.speedX = 0
                self.Left = True
        else:
            self.speedX = -speed
            if self.rect.right < 150:
                self.speedX = 0
                self.Left = False

        if not self.on_ground:
            self.speedY += self.grav

        if self.rect.bottom >= self.ground:
            self.rect.bottom = self.ground
            self.on_ground = True
            self.speedY = 0

        self.animation()

        if keys[pygame.K_e]:
            self.attacka()
            if self.hhp == 9:
                pygame.quit()

    def check_collizion(
            self, platforms):

        if pygame.sprite.spritecollideany(
                self, platforms):
            if self.speedY != 0:
                if self.speedY > 0:
                    self.on_ground = True
                self.speedY = 0
        else:
            self.speedY += self.grav

    def animation(
            self):

        if self.speedX:
            # Если скорость по Х не нулевая, значит я иду
            self.animCount += 1
            # Счётчик подсчитывает, какую картинку по счёту я должен показать
            if self.animCount == len(run_animation):
                # если я дошёл до последней картинки в списке картинок
                self.animCount = 0
                # то обнуляю счётчик, чтобы начать сначала

            self.image = run_animation[self.animCount]
            # Достаю картинку с нужным номером из списка
            if self.speedX > 0:
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
