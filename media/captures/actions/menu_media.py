import pygame

Button_h = 260
Button_w = 640

Button_start = [
    pygame.image.load(
        "../../media/captures/actions/"
        "Tiles/Menu/play_button_passive.764.png").subsurface(0, 200, Button_w, Button_h),
    pygame.image.load(
        "../../media/captures/actions/"
        "Tiles/Menu/play_button_active.352.png").subsurface(0, 200, Button_w, Button_h),

]

Button_exit = [
    pygame.image.load("../../media/captures/actions/"
                      "Tiles/Menu/"
                      "exit_button_passive.208.png").subsurface(
        0, 200,
        Button_w,
        Button_h),
    pygame.image.load("../../media/captures/actions/"
                      "Tiles/Menu/"
                      "exit_button_active.139.png").subsurface(
        0, 200, Button_w,
        Button_h),
]

Button_base = [
    pygame.Surface((
        Button_w, Button_h - 50)),
    pygame.Surface((
        Button_w, Button_h - 50))
]
