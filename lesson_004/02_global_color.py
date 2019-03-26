# -*- coding: utf-8 -*-

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

import simple_draw as sd
sd.resolution = (800, 900)

point_0 = sd.get_point(100, 100)
point_1 = sd.get_point(400, 100)
point_2 = sd.get_point(100, 400)
point_3 = sd.get_point(400, 400)

colors = {
    1: {'title': 'Красный', 'value': sd.COLOR_DARK_RED},
    2: {'title': 'Оранжевый', 'value': sd.COLOR_ORANGE},
    3: {'title': 'Желтый', 'value': sd.COLOR_YELLOW},
    4: {'title': 'Зеленый', 'value': sd.COLOR_GREEN},
    5: {'title': 'Голубой', 'value': sd.COLOR_CYAN},
    6: {'title': 'Синий', 'value': sd.COLOR_BLUE},
    7: {'title': 'Фиолетовый', 'value': sd.COLOR_PURPLE}
}


def drawing_figure(point, angle, length, step):
    v = sd.get_vector(start_point=point, angle=angle, length=length, width=4)
    for angle in range(angle, 360, step):
        v = sd.get_vector(start_point=v.end_point, angle=angle, length=length, width=4)
        v.draw(figure_color)


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


# Логичнее эту строчку здесь сделать
print('Список доступных цветов')
for colors_code in colors:
    print(colors_code, ':', colors[colors_code]['title'])

user_input = input("Введите, номер желаемого цвета: ")
colors_code = int(user_input)

if colors_code not in colors:
    print('Вы ввели некоректный номер')
else:
    print('Вы ввели', colors_code, ' : ', colors[colors_code]['title'])
    figure_color = colors[colors_code]['value']
    triangle(point=point_0, angle=15, length=120, side=3)
    square(point=point_1, angle=15, length=120, side=4)
    pentagon(point=point_2, angle=15, length=120, side=5)
    hexagon(point=point_3, angle=15, length=120, side=6)


sd.pause()

# зачет!
