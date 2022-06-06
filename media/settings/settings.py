from sys import platform

if (platform == "linux"
        or platform == "linux2"):
    from screeninfo import get_monitors

    m = get_monitors()[0]  # получем первый монитор
    data = str(m).split(',')  # разделяем данные на части для обработки
    user_screen_w = int(data[2].split('=')[1])  # Ширина
    user_screen_h = int(data[3].split('=')[1])  # Высота

elif platform == "darwin":  # mac OS
    print(platform)

elif platform == "win32":
    import ctypes

    user32 = ctypes.windll.user32
    user_screen_w, user_screen_h = user32.GetSystemMetrics(0), \
                                   user32.GetSystemMetrics(1)

elif platform == "win64":
    import ctypes

    user32 = ctypes.windll.user32
    user_screen_w, user_screen_h = user64.GetSystemMetrics(0), \
                                   user64.GetSystemMetrics(1)
