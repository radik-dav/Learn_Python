#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте 2 разных списка:

# список "моя семья" (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Я','Жена', 'Дочь']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['Радик', 178],
    ['Юлия', 156],
    ['Милана', 70],
]

# Выведите на консоль рост отца: "Рост отца ХХХ см"

# Выведите на консоль общий рост вашей семьи: "Рост всей семьи УУУ см"
# Общий рост семьи считать как сумму ростов всех членов семьи

father_height = my_family_height[0][1]
my_wife_height = my_family_height[1][1]
my_daughter_height = my_family_height[2][1]

total_family_height = father_height + my_wife_height + my_daughter_height

print('Рост отца', father_height, 'см' )
print('Рост всей семьи', total_family_height, 'см')

# зачет!

