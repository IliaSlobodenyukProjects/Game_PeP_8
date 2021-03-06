from sys import platform
from pathlib import Path
import os

if (platform == "linux"
        or platform == "linux2"):
    from screeninfo import get_monitors

    m = get_monitors()[0]  # получем первый монитор
    data = str(m).split(',')  # разделяем данные на части для обработки
    User_screen_w = int(data[2].split('=')[1])  # Ширина
    User_screen_h = int(data[3].split('=')[1])  # Высота

elif platform == "darwin":  # mac OS
    print(platform)

elif platform == "win32":
    import ctypes

    user32 = ctypes.windll.user32
    User_screen_w, User_screen_h = user32.GetSystemMetrics(0), \
                                   user32.GetSystemMetrics(1)

BASE_DIR = os.path.dirname(os.path.dirname('media'))
MEDIA_ROOT = Path(BASE_DIR, 'media')
MEDIA_URL = 'media'
