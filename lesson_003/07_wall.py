# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

wall = sd.resolution
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

width = 100
height = 50
# полкирпича
width_half_brick = width // 2

# Чтобы отдельно переменную не заводить, лучше использовать функцию enumerate()
for row, y in enumerate(range(0, 610, 50)):
    for x in range(0, 610, 100):
        # если четный ряд
        if row % 2 == 0:
            x += width_half_brick

        point_1 = sd.get_point(x - width, y - height)
        point_2 = sd.get_point(x, y)
        sd.rectangle(left_bottom=point_1, right_top=point_2, color=sd.COLOR_DARK_ORANGE, width=6)


sd.pause()

# зачет!
