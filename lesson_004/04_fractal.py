# -*- coding: utf-8 -*-

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2 )Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с углом рисования равным углу ветви,
#   длиной ветви меньшей чем длина ветви с коэффициентом 0.75

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

import simple_draw as sd
sd.resolution = (1200, 800)
root_point = sd.get_point(300, 30)


def draw_branches(point, angle, length, delta):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=4)
    v1.draw(sd.COLOR_DARK_ORANGE)
    next_point = v1.end_point
    next_angle_left = angle + delta
    next_angle_right = angle - delta
    next_length = length * .75
    draw_branches(point=next_point, angle=next_angle_left, length=next_length, delta=delta)
    draw_branches(point=next_point, angle=next_angle_right, length=next_length, delta=delta)


draw_branches(point=root_point, angle=90, length=100, delta=30)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()

# зачет!
