#!/usr/bin/env python
# -*- coding: utf-8 -*-


# =================================
# Логические выражения и ветвление
# =================================

# Результат любого логического выражения либо "Ложь" (False), либо "Истина" (True)
# Логические операторы >(больше) <(меньше) ==(равно) !=(не равно) >=(Больше или равно) <=(меньше или равно)

print('2 > 4 --> ', 2 > 4)
print('4 == 4 --> ', 4 == 4)

# Допускаются составные логические выражения
print('2 < 6 < 10 -->', 2 < 6 < 10)
print('2 < 0 < 10 -->', 2 < 0 < 10)

# Операторы and(и), or(или), not(не)
print('2 > 0 and 2 > 10 -->', 2 > 0 and 2 > 10)  # True, если оба выражения True
print('2 > 0 or 2 > 10 -->', 2 > 0 or 2 > 10)  # True, если любое выражение True
print('not(2 > 0) -->', not(2 > 0))  # инвертор - меняет результат на противоположный

# Операторы ветвления
age = 12
if age >= 18:
    print('Пользователь совершеннолетний')
    access = True  # доступ куда-либо
else:
    print('Пользователь НЕсовершеннолетний')
    access = False  # доступ куда-либо

# if <логическое выражение>:
#     блок if
#     блок if
#     блок if

# !!!В языке python операторными скобками (отделяющими блоки) являются ОДИНАКОВЫЕ оступы слева

# После инструкции if может находиться любое значение, которое будет автоматически преобразовано к типу bool
if 2 + 2 - 8:
    print('Ура!')

print('bool(False) -->', bool(False))
print('bool(0) -->', bool(0))
print('bool("") -->', bool(""))  # Пустая строка
print('bool([]) -->', bool([]))  # Пустой список
# В остальных случаях функция bool() --> True

# !Не пишите так:
if access == True:
    print('Welcome!')
# Пишите так:
if access:
    print('Welcome!')
# Результат одинаковый, но в первом случае вы показываете свою неграмотность

# Полный вариант оператора ветвления
color = 'red'

if color == 'blue':
    print('синий')
elif color == 'red':  # elif сокращение от else if (иначе если)
    print('красный')
elif color == 'green':
    print('зеленый')
else:  # else выполняется, только если все предыдущие проверки вернули False
    print('неизвестный цвет')

# Допускается вкладывать инструкции друг в друга:
n = 20
if n > 0:
    if n < 50:
        print('n больше нуля, но меньше 50')
# !Но старайтесь избегать вложения, чем больше уровень вложенности, тем сложнее читать ваш код
# Предыдущий код лучше переписать так:
if n > 0 and n < 50:
    print('n больше нуля, но меньше 50')
# Или так:
if 0 < n < 50:
    print('n больше нуля, но меньше 50')
