#!/usr/bin/env python
# -*- coding: utf-8 -*-



# =================================
#     Переменные и типы данных
# =================================

# Переменные используются для хранения данных в программе

# Требования к имени переменных:
# 1. Имя переменной может содержать a-z, A-Z, 0-9, _ (символ нижнего подчеркивания)
# 2. Имя переменной не может начинаться с цифры
# 3. Не рекомендуется использовать зарезервированные слова и имена встроенных функций
#   в качестве имени переменной

# type() - позволяет узнать тип данных, хранящихся в переменной
x = 10      # int
print('type(10) -> ', type(x))
# python - язык с динамической типизацией. Переменная может указывать на объекты различных типов.
x = -2.4    # float
print('type(-2.4) -> ', type(x))

# print(X) <-- ошибка
# Нельзя использовать переменную прежде чем ей будет присвоено значение
# x и X - разные переменные, python - регистрочувствительный

x += 1  # краткая запись выражения: x = x + 1
print('x = ', x)

# =================================
#         Приведение типов
# =================================

# Для приведения к типу существуют функции, имена которых соответствуют приводимым типам
# int() --> int str() --> str и т.д.

# типы можно конвертировать друг в друга
print('float(2) --> ', float(2))
print('int(2.12) --> ', int(2.12))  # вещественное число приводится к целому путем отбрасывания дробной части
print('Prise is: ' + str(11.32) + '$')

# print(2 + '4') <-- ошибка
# нельзя складывать строку и число
print(str(2) + '4')  # Но можно так
print(2 + int('4'))  # Или так


# =================================
#              None
# =================================

# Специальный объект None
# Обозначает буквально "ничего"
# Обычно используется для задания начального значения переменным
a = None
# None и False — разные вещи!
print(None == False)

# None равен только себе и никакому другому типу
print(None == None)

