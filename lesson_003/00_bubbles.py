# -*- coding: utf-8 -*-
import random
import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 2 параметра: точка рисовании и шаг


def bubble(point_2, step_2):
    radius_2 = 50

    for _ in range(3):
        radius_2 += step_2
        sd.circle(center_position=point_2, radius=radius_2, width=2)


point = sd.get_point(100, 500)
bubble(point_2=point, step_2=10)

# Нарисовать 10 пузырьков в ряд

for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    bubble(point_2=point, step_2=5)

# Нарисовать три ряда по 10 пузырьков

for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point_2=point, step_2=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# Рисуем цветной пузырик с 3-мя параметрами  и случайным цветом


def random_color_bubbles(point_3, step_3, random_colors):
    radius_3 = 27
    for _ in range(3):
        radius_3 += step_3
        sd.circle(center_position=point_3, color=random_colors, radius=radius_3, width=3)


point = sd.get_point(50, 600)
random_color_bubble = sd.random_color()
random_color_bubbles(point_3=point, step_3=10, random_colors=random_color_bubble)


# Выводим произвольно 100 пузырей в разных местах

for _ in range(100):
    point = sd.random_point()
    random_color_bubble = sd.random_color()
    step = random.randint(3, 8)
    random_color_bubbles(point_3=point, step_3=step, random_colors=random_color_bubble)

sd.pause()

# зачет!
