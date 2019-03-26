# -*- coding: utf-8 -*-
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
# создать_снежинки(N) - создает N снежинок
# нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
# сдвинуть_снежинки() - сдвигает снежинки на один шаг
# номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
# удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
# создать_снежинки(N)

import simple_draw as sd
from lesson_006.snowfall import create_snowflakes, snow_draw, move_snowflakes, numbers_reaching_bottom_screen, \
    add_new_snowflake, remove_snowflakes

create_snowflakes()
while True:
    sd.start_drawing()
    snow_draw(sd.background_color)
    move_snowflakes()
    snow_draw(sd.COLOR_WHITE)
    reached_bottom = numbers_reaching_bottom_screen()
    if reached_bottom:
        add_new_snowflake(reached_bottom)
        remove_snowflakes(reached_bottom)

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
