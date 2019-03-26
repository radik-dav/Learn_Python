# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw
import random

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

point = simple_draw.get_point(100, 450)


def smile(smile_point):
    # Радиус смайлика
    radius = 50

    # Радиус глаз
    eyes_radius = 10

    # Рисуем окружность для смайлика
    simple_draw.circle(center_position=smile_point, color=simple_draw.COLOR_YELLOW, radius=radius, width=0)

    # Рисуем глаза
    point1 = simple_draw.get_point(smile_point.x - 25, smile_point.y + 10)
    point2 = simple_draw.get_point(smile_point.x + 25, smile_point.y + 10)
    simple_draw.circle(center_position=point1, color=simple_draw.COLOR_DARK_PURPLE, radius=eyes_radius, width=0)
    simple_draw.circle(center_position=point2, color=simple_draw.COLOR_DARK_PURPLE, radius=eyes_radius, width=0)

    # Рисуем рот
    point3 = simple_draw.get_point(smile_point.x - 25, smile_point.y - 20)
    point4 = simple_draw.get_point(smile_point.x - 20, smile_point.y - 10)
    point5 = simple_draw.get_point(smile_point.x + 20, smile_point.y - 10)
    point6 = simple_draw.get_point(smile_point.x + 10, smile_point.y - 30)
    simple_draw.polygon(point_list=[point3, point4, point5, point6], color=simple_draw.COLOR_RED, width=2)


# рандомно выводим смайлики
for _ in range(10):
    point = simple_draw.random_point()
    smile(smile_point=point)

simple_draw.pause()

# зачет!
