# -*- coding: utf-8 -*-

# Создать пакет, в котором собрать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Каждую функцию разместить в своем модуле. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)


import simple_draw as sd
import painting_snippets.smile
import painting_snippets.rainbow
import painting_snippets.house_roof
import painting_snippets.wall
import painting_snippets.tree
import painting_snippets.sun
import painting_snippets.snowfall

painting_snippets.rainbow.draw_rainbow()
painting_snippets.house_roof.roof_draw()
painting_snippets.wall.draw_wall()
painting_snippets.smile.smile(smile_point=sd.get_point(635, 160))
painting_snippets.sun.draw_sun()
painting_snippets.snowfall.snowfall_draw()


sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# зачет!
