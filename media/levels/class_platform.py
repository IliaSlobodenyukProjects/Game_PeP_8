import pygame
from media.captures.actions.platform import Platform_image


class Platform(
    pygame.sprite.Sprite
):
    def __init__(
            self, groups, x,
            y, w, h):
        super().__init__(
            groups)
        self.image = pygame.transform.scale(
            Platform_image, (180, 180))
        self.rect = self.image.get_rect(
            x=x, y=y)
