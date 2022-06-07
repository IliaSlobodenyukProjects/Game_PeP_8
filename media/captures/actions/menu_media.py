import pygame


button_h = 260
button_w = 640

button_start = [
    pygame.image.load(
        "../../media/captures/actions/Tiles/Menu/play_button_passive.764.png").subsurface(0, 200, button_w, button_h),
    pygame.image.load(
        "../../media/captures/actions/Tiles/Menu/play_button_active.352.png").subsurface(0, 200, button_w, button_h),

]

button_base = [
    pygame.Surface((
        button_w, button_h - 50)),
    pygame.Surface((
        button_w, button_h - 50))
]