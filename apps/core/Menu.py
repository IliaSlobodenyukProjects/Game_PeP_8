import pygame
from media.settings.settings import user_screen_h, user_screen_w
from media.captures.actions.menu_media import button_start, button_h, button_w, button_base

pygame.init()

button_exit = [
    pygame.image.load("../../media/captures/actions/Tiles/Menu/exit_button_passive.208.png").subsurface(0, 200,
                                                                                                        button_w,
                                                                                                        button_h),
    pygame.image.load("../../media/captures/actions/Tiles/Menu/exit_button_active.139.png").subsurface(0, 200, button_w,
                                                                                                       button_h),

]

button_base[0].fill((100, 100, 100))
button_base[1].fill((255, 0, 0))


class Button(
    pygame.sprite.Sprite):
    def __init__(
            self, button_name, y,
            width=button_w, height=button_h):
        # button_name - какая кнопка вызывается
        super().__init__()
        self.button_name = button_name
        self.width = width
        self.height = height

        self.active = False

        if self.button_name == 'START':
            self.images = button_start

        elif self.button_name == 'EXIT':
            self.images = button_exit
        else:
            self.images = button_base

        self.image = self.images[self.active]

        self.rect = self.image.get_rect(
            centerx=user_screen_w // 2, y=y)

    def update(
            self, *args):
        self.image = self.images[self.active]


class Menu():
    def __init__(self, win):
        self.win = win  # Экран для отрисовки

        self.activeButton = 0  # Бывшая переменная num, какая кнопка сейчас активна
        self.buttons = [
            Button("START", (button_h) * 0 + 230),
            #                        Button("OPTIONS", (BUTTON_H) * 1+270),
            Button("EXIT", (button_h) * 1 + 270),
        ]

    def update(
            self):
        self.win.fill(
            (56, 67, 128))

        for b in self.buttons:
            b.update()
            self.win.blit(b.image, b.rect)
        pygame.display.update()

    def up(self):
        if self.activeButton:
            self.buttons[self.activeButton].active = False
            self.activeButton -= 1
            self.buttons[self.activeButton].active = True

    def down(self):
        if self.activeButton + 1 != len(self.buttons):
            self.buttons[self.activeButton].active = False
            self.activeButton += 1
            self.buttons[self.activeButton].active = True
