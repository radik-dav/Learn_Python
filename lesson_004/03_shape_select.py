# -*- coding: utf-8 -*-

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

import simple_draw as sd
sd.resolution = (800, 900)

point_0 = sd.get_point(220, 350)


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


figures = {
    1: {'title': 'треугольник', 'function': triangle},
    2: {'title': 'квадрат','function': square},
    3: {'title': 'пятиугольник', 'function': pentagon},
    4: {'title': 'шестиугольник','function': hexagon}
}

# Логичнее эту строчку здесь сделать
print('Список доступных фигур')
for code_figure in figures:
    print(code_figure, ':', figures[code_figure]['title'])

user_input = input("Введите, номер желаемой фигуры: ")
code_figure = int(user_input)

if code_figure not in figures:
    print('Вы ввели некоректный номер')
else:

    print('Вы ввели', code_figure, ' : ', figures[code_figure]['title'])

    # Тут можно вместо всех if-else сделать в одну строчку :)
    # figures[code_figure]['function'](point=point_0, angle=15, length=120, side=code_figure + 2)

    if code_figure == 1:
        figures[code_figure]['function'](point=point_0, angle=15, length=120, side=3)
    elif code_figure == 2:
        figures[code_figure]['function'](point=point_0, angle=15, length=120, side=4)
    elif code_figure == 3:
        figures[code_figure]['function'](point=point_0, angle=15, length=120, side=5)
    else:
        figures[code_figure]['function'](point=point_0, angle=15, length=120, side=6)


sd.pause()

# зачет!
