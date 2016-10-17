#!/usr/bin/env python
# -*- coding: utf-8 -*-



# =================================
#     Логические операции
# =================================

# Логический тип
# По сути представляет из себя числа 1 и 0
# С некоторыми особенностями отображения на экране:
x = True
y = False
print('bool --> ', x, '/', y)
print("1 + True = ", 1 + True)  # True, по сути, и есть 1

# Логические опараторы
# > Больше
# < Меньше
# == Равно
# != Не равно
# >= Больше или равно
# <= Меньше или равно
print("5 > 6 -->", 5 > 6)
print("2 != 7 -->", 2 != 7)

# Любое значение может быть преобразовано к логическому типу функией bool()
print("bool(0) -->", bool(0))
print("bool(-1) -->", bool(-1))
print("bool('') -->", bool(""))
print("bool('0') -->", bool("0"))
print("bool(False) -->", bool(False))

