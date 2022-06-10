import pygame
from media.captures.actions.hero_media import Walk, Idle, Attack
from media.settings.constants import Hero_h, Hero_w, Speed_hero, Jump_hero, Gravitation

runAnimation = []
for image in Walk:
    runAnimation.append(
        pygame.transform.scale(
            image, (Hero_w, Hero_h)))
jumpAnimation = []

idleAnimation = []
for image in Idle:
    idleAnimation.append(
        pygame.transform.scale(
            image, (Hero_w, Hero_h)))  # PeP_8
attackAnimation = []
for image in Attack:  # PeP_8
    attackAnimation.append(
        pygame.transform.scale(
            image, (Hero_w, Hero_h)))


class Hero(
    pygame.sprite.Sprite):

    def __init__(
            self, groups, screen_h,
            enemygroup):
        super().__init__(
            groups)
        self.anim_count = 0
        self.image = runAnimation[self.anim_count]
        self.hp = 4

        self.rect = self.image.get_rect(
            x=5, bottom=screen_h)
        self.speed_x = 0
        self.a = self.get_coords()

        # Движение по Y
        self.speed_y = 0
        self.on_ground = True  # Стоит на земле
        self.is_jump = False  # прыгает или нет
        self.ground = screen_h
        self.enemygroup = enemygroup

        self.idleLeft = True
        self.attack = False

    def update(
            self, platforms):

        keys = pygame.key.get_pressed()
        self.speed_x = 0
        if keys[pygame.K_a]:  # ЛЕВО
            self.idleLeft = True
            if self.rect.left > 0:
                self.speed_x = -Speed_hero
            self.a = self.get_coords()

        elif keys[pygame.K_d]:
            self.idleLeft = False
            self.speed_x = Speed_hero

        if (keys[pygame.K_SPACE]
                and self.on_ground):  # ПРЫЖОК
            self.speed_y -= Jump_hero
            self.on_ground = False

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if not self.on_ground:
            self.speed_y += Gravitation

        if self.rect.bottom >= self.ground:
            self.rect.bottom = self.ground
            self.on_ground = True
            self.speed_y = 0

        if (keys[pygame.K_e]
                and self.speed_x == 0):  # атака
            if not self.attack:
                self.anim_count = 0
            self.attack = True
            self.attacka()

        self.check_collizion(
            platforms)
        #    var = self.onGrond
        self.animation()
        self.is_alive()

    def check_collizion(
            self, Platform):

        if pygame.sprite.spritecollideany(
                self, Platform):
            if self.speed_y != 0:
                if self.speed_y > 0:
                    self.on_ground = True
                self.speed_y = 0
        else:
            self.on_ground = False

    def is_alive(
            self):
        if self.hp:
            return True
        else:
            return False

    def attacka(
            self):
        hits = pygame.sprite.spritecollide(
            self, self.enemygroup, True,
            pygame.sprite.collide_circle)
        if hits:
            return True

    def animation(
            self):
        # ATAKA
        if self.attack:
            if self.anim_count >= len(attackAnimation) // 2:
                # если я дошёл до последней картинки в списке картинок
                self.anim_count = 0
                self.attack = False
                # то обнуляю счётчик, чтобы начать сначала
            self.image = attackAnimation[self.anim_count]
            # Достаю картинку с нужным номером из списка

        # БЕГ
        elif self.speed_x:
            # Если скорость по Х не нулевая, значит я иду
            if self.anim_count >= len(runAnimation):
                # если я дошёл до последней картинки в списке картинок
                self.anim_count = 0
                # то обнуляю счётчик, чтобы начать сначала

            self.image = runAnimation[self.anim_count]
            # Достаю картинку с нужным номером из списка


        # СТОИТ
        else:  # иначе скорость = 0, значит стою на месте
            if self.anim_count >= len(idleAnimation):
                self.anim_count = 0
            self.image = idleAnimation[self.anim_count]

        if not self.idleLeft:
            self.image = pygame.transform.flip(
                self.image, True, False)
        self.anim_count += 1
        # Счётчик подсчитывает, какую картинку по счёту я должен показать

    def get_coords(
            self):
        return self.rect.x, self.rect.y
