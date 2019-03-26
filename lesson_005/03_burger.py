# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."
# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.
# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger


def double_cheeseburger_recipe():
    print('Рецепт двойного чизбургера')
    my_burger.add_a_bun()
    my_burger.add_cutlet()
    my_burger.add_cheese()
    my_burger.add_cutlet()
    my_burger.add_cheese()
    my_burger.add_cucumber()
    my_burger.add_tomato()
    my_burger.add_mayo()
    my_burger.add_onion()
    my_burger.add_a_bun()
    print('Готово !')


double_cheeseburger_recipe()

print('\n')


def homemade_burger():
    print('Рецепт домашнего бургера')
    my_burger.add_a_bun()
    my_burger.add_lettuce_leaves()
    my_burger.add_big_beef_cutlet()
    my_burger.add_onion()
    my_burger.add_tomato()
    my_burger.add_cucumber()
    my_burger.add_mustard()
    my_burger.add_a_bun()
    print('Готово !')


homemade_burger()

# зачет!
