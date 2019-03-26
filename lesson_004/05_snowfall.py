# -*- coding: utf-8 -*-

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

import simple_draw as sd
import random
sd.resolution = (1200, 800)
N = 20
x_coordinates = [coord_x for coord_x in range(100, 1100, 50)]
y_coordinates = [coord_y for coord_y in range(800, 1900, 30)]
sizes_rays = [rays_snowflakes for rays_snowflakes in range(10, 100, 5)]


x = []
y = []
size_snowflakes = []
old_snowflakes = []


def snow_draw(x, y, length, color):
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=length, factor_a=0.5, color=color)


for i in range(0, N):
    x.append(x_coordinates[random.randint(0, len(x_coordinates) - 1)])
    y.append(y_coordinates[random.randint(0, len(y_coordinates) - 1)])
    size_snowflakes.append(sizes_rays[random.randint(0, len(sizes_rays) - 1)])


while True:
    sd.start_drawing()
    for i in range(0, len(x)):
        snow_draw(x[i], y[i], size_snowflakes[i], sd.background_color)
        if y[i] > size_snowflakes[i]:
            y[i] = y[i] - 5
            delta = random.randint(-5, 5)
            x[i] = x[i] + delta
        else:
            if i not in old_snowflakes:
                old_snowflakes.append(i)
                if y[i] <= 400:
                    x.append(x_coordinates[random.randint(0, len(x_coordinates) - 1)])
                    y.append(y_coordinates[random.randint(0, len(y_coordinates) - 1)])
                    size_snowflakes.append(sizes_rays[random.randint(0, len(sizes_rays) - 1)])
        snow_draw(x[i], y[i], size_snowflakes[i], sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(0.08)
    if sd.user_want_exit():
        break

sd.pause()


# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

# зачет!
