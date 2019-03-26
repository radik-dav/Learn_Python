# -*- coding: utf-8 -*-
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны

# Нарисовать все фигуры
# Выделить общую часть алгоритма рисования в отдельную функцию
# Придумать, как устранить разрыв в начальной точке фигуры

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


import simple_draw as sd
sd.resolution = (800, 900)

point_0 = sd.get_point(100, 100)
point_1 = sd.get_point(400, 100)
point_2 = sd.get_point(100, 400)
point_3 = sd.get_point(400, 400)


def drawing_figure(point, angle, length, step):
    v = sd.get_vector(start_point=point, angle=angle, length=length, width=4)
    for angle in range(angle, 360, step):
        v = sd.get_vector(start_point=v.end_point, angle=angle, length=length, width=4)
        v.draw()


def triangle(point, angle, length, side):
    step = 360 // side
    drawing_figure(point, angle, length, step)


def square(point, angle, length, side):
    step = 360 // side
    drawing_figure(point, angle, length, step)


def pentagon(point, angle, length, side):
    step = 360 // side
    drawing_figure(point, angle, length, step)


def hexagon(point, angle, length, side):
    step = 360 // side
    drawing_figure(point, angle, length, step)


triangle(point=point_0, angle=15, length=120, side=3)
square(point=point_1, angle=15, length=120, side=4)
pentagon(point=point_2, angle=15, length=120, side=5)
hexagon(point=point_3, angle=15, length=120, side=6)


sd.pause()

# зачет!
