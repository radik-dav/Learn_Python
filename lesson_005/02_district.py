# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as resident_1
from district.central_street.house1.room2 import folks as resident_2
from district.central_street.house2.room1 import folks as resident_3
from district.central_street.house2.room2 import folks as resident_4
from district.soviet_street.house1.room1 import folks as resident_5
from district.soviet_street.house1.room2 import folks as resident_6
from district.soviet_street.house2.room1 import folks as resident_7
from district.soviet_street.house2.room2 import folks as resident_8

districts = resident_1 + resident_2 + resident_3 + resident_4 + resident_5 + resident_6 + resident_7 + resident_8
# Добавим пробел еще после запятой
all_residents = ', '.join(districts)
print('На районе живут: ', all_residents)

# зачет!



