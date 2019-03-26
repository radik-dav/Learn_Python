# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)

a, b = 179, 37
integer_division_result = 0

while a > b:
    integer_division_result += 1
    a -= b
print(integer_division_result)

# зачет!
