import pygame
from media.settings.settings import User_screen_h, User_screen_w
from media.captures.actions.menu_media import (Button_start,
    Button_h, Button_w, Button_base, Button_exit)

pygame.init()

try:
    Button_base[0].fill((100, 100, 100))
    Button_base[1].fill((255, 0, 0))
except IndexError:
    print('Нет такого файла')


class Button(
    pygame.sprite.Sprite):
    def __init__(
            self, button_name, y,
            width=Button_w, height=Button_h):
        # button_name - какая кнопка вызывается
        super().__init__()
        self.button_name = button_name
        self.width = width
        self.height = height

        self.active = False

        self.images = Button_base
        if self.button_name == 'START':
            self.images = Button_start
        else:
            self.images = Button_exit

        self.image = self.images[self.active]

        self.rect = self.image.get_rect(
            centerx=User_screen_w // 2, y=y)

    def update(
            self, *args):
        self.image = self.images[self.active]


class Menu():
    def __init__(
            self, win):
        self.win = win
        # Экран для отрисовки

        self.active_button = 0
        self.buttons = [
            Button("START", Button_h * 0 + 230),
            Button("EXIT", Button_h * 1 + 270),
        ]

    def update(
            self):
        self.win.fill(
            (56, 67, 128))

        for b in self.buttons:
            b.update()
            self.win.blit(b.image, b.rect)
        pygame.display.update()

    def up(
            self):
        if self.active_button:
            self.buttons[self.active_button].active = False
            self.active_button -= 1
            self.buttons[self.active_button].active = True

    def down(
            self):
        if self.active_button + 1 != len(self.buttons):
            self.buttons[self.active_button].active = False
            self.active_button += 1
            self.buttons[self.active_button].active = True
