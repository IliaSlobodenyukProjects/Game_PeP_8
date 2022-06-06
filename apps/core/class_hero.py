import pygame
from media.captures.actions.hero_media import walk, idle, attack
from media.settings.set import hero_h, hero_w, speed_hero, jump_hero

runAnimation = []
for image in walk:
    runAnimation.append(pygame.transform.scale(image, (hero_w, hero_h)))
jumpAnimation = []

idleAnimation = []
for image in idle:
    idleAnimation.append(pygame.transform.scale(image, (hero_w, hero_h)))  # PeP_8
attackAnimation = []
for image in attack:  # PeP_8
    attackAnimation.append(pygame.transform.scale(image, (hero_w, hero_h)))


class Hero(pygame.sprite.Sprite):

    def __init__(self, groups, screenH, enemygroup):
        super().__init__(groups)
        self.animCount = 0
        self.image = runAnimation[self.animCount]
        self.hp = 4

        self.rect = self.image.get_rect(x=5, bottom=screenH)
        self.speedX = 0
        self.a = self.get_coords()

        # Движение по Y
        self.speedY = 0
        self.grav = 2  # гравитация - скорость движения вниз
        self.onGrond = True  # Стоит на земле
        self.isJump = False  # прыгает или нет
        self.GROUND = screenH
        self.enemygroup = enemygroup

        self.idleLeft = True
        self.attack = False

    #        self.weapon = classes2[sprite][1]
    #        self.move = classes2[sprite][-2]

    def update(self, platforms):
        """
        Функция запускается из главной программы постоянно(в цикле)
        :param platforms:
        :return:
        """
        # добавь управление
        keys = pygame.key.get_pressed()
        self.speedX = 0
        if keys[pygame.K_a]:  # ЛЕВО
            self.idleLeft = True
            # self.idleRight = False
            if self.rect.left > 0:
                self.speedX = -speed_hero
            self.a = self.get_coords()

        elif keys[pygame.K_d]:  # ПРАВО
            self.idleLeft = False
            # self.idleRight = True
            # if self.rect.right < USER_SCREEN_W:
            self.speedX = speed_hero

        if keys[pygame.K_SPACE] and self.onGrond:  # ПРЫЖОК
            self.speedY -= jump_hero
            self.onGrond = False

        self.rect.x += self.speedX
        self.rect.y += self.speedY

        if not self.onGrond:
            self.speedY += self.grav

        if self.rect.bottom >= self.GROUND:
            self.rect.bottom = self.GROUND
            self.onGrond = True
            self.speedY = 0

        if keys[pygame.K_e] and self.speedX == 0:  # атака
            if not self.attack:
                self.animCount = 0
            self.attack = True
            self.attacka()

        self.check_collizion(platforms)
        #    var = self.onGrond
        self.animation()
        self.is_alive()

    def check_collizion(self, Platform):
        if pygame.sprite.spritecollideany(self, Platform):
            if self.speedY != 0:
                if self.speedY > 0:
                    self.onGrond = True
                self.speedY = 0
        else:
            self.onGrond = False

    def is_alive(self):
        if self.hp:
            return True
        else:
            return False

    def attacka(self):
        hits = pygame.sprite.spritecollide(self, self.enemygroup, True, pygame.sprite.collide_circle)
        if hits:
            return True

    def animation(self):
        # ATAKA
        if self.attack:
            if self.animCount >= len(attackAnimation) // 2:  # если я дошёл до последней картинки в списке картинок
                self.animCount = 0
                self.attack = False  # то обнуляю счётчик, чтобы начать сначала
            self.image = attackAnimation[self.animCount]  # Достаю картинку с нужным номером из списка

        # БЕГ
        elif self.speedX:  # Если скорость по Х не нулевая, значит я иду
            if self.animCount >= len(runAnimation):  # если я дошёл до последней картинки в списке картинок
                self.animCount = 0  # то обнуляю счётчик, чтобы начать сначала

            self.image = runAnimation[self.animCount]  # Достаю картинку с нужным номером из списка
            # if self.speedX > 0:  # Если двигаюсь вправо,
            #     self.image = pygame.transform.flip(self.image, True, False)  # то отзеркаливаю картинку персонажа

        # СТОИТ
        else:  # иначе скорость = 0, значит стою на месте
            if self.animCount >= len(idleAnimation):
                self.animCount = 0
            self.image = idleAnimation[self.animCount]

        #        if not self.onGrond:
        #        if self.animCount >= len(jumpAnimation):
        #                self.animCount = 0
        # self        self.image = jumpAnimation[self.animCount]

        # Если направление вправо, то зеркалим картинку
        if not self.idleLeft:
            self.image = pygame.transform.flip(self.image, True, False)
        self.animCount += 1  # Счётчик подсчитывает, какую картинку по счёту я должен показать

    def get_coords(self):
        return self.rect.x, self.rect.y
