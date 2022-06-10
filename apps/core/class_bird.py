import pygame
from media.settings.settings import User_screen_w
from media.captures.actions.bird_media import Fly
from media.settings.constants import Bird_w, Bird_h, Speed_bird

fly_animation = []
for image in Fly:
    fly_animation.append(
        pygame.transform.scale(
            image, (Bird_w, Bird_h)))


class Bird(
    pygame.sprite.Sprite):

    def __init__(
            self, groups, x,
            y, width, height):
        super().__init__(
            groups)
        self.anim_count = 0
        self.image = fly_animation[self.anim_count]
        self.rect = self.image.get_rect(
            x=x, bottom=y + height + 500)
        self.speed_x = 0
        self.Left = False

    def update(
            self):

        if not self.Left:
            self.speed_x = Speed_bird
            if self.rect.right > User_screen_w:
                self.speed_x = 0
                self.Left = True
        else:
            self.speed_x = -Speed_bird
            if self.rect.right < 150:
                self.speed_x = 0
                self.Left = False

        self.rect.x += self.speed_x
        self.animation()

    def animation(
            self):

        if self.speed_x:
            self.anim_count += 1
            if self.anim_count == len(fly_animation):
                self.anim_count = 0

            self.image = fly_animation[self.anim_count]
            if self.speed_x < 0:  # Если двигаюсь вправо,
                self.image = pygame.transform.flip(
                    self.image, True, False)
