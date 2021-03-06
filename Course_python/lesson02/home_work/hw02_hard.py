#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Белых Ольга

# Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
# Определить координату y, точки с заданной координатой x

equation = 'y=-12x + 11111140.2121'
x = 2.5

res = equation.split('=')
y0 = res[1].split('x + ')

y = -float(y0[0])*x + float(y0[1])

print y

# вычислите и выведите y

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy', проверить корректно ли введена дата
# Условия коррекности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год приводиться к целому положитеьному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)
from datetime import datetime

# Пример корректной даты
date = '01.11.1985'
d = datetime.strptime(date, "%d.%m.%Y")
# Примеры некорректных дат
date1 = '01.22.1001'
date2 = '1.12.1001'
date3 = '-2.10.3001'

# d1 = datetime.strptime(date1, "%d.%m.%Y")
# d2 = datetime.strptime(date1, "%d.%m.%Y")
# d3 = datetime.strptime(date1, "%d.%m.%Y")

# Не успела сделать, лучше сдам пока без нее. Может завтра успею осилить.
# Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа
# на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача: нужно научится по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3