#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =============================
#    Перегрузка операторов
# =============================

# Имена методов, начинающиеся и заканчивающиеся двумя символами подчеркивания __X__, имеют специальное назначение.
# Такие методы вызываются автоматически, когда объект участвует в соответствующей операции.
# Возвращаемое значение метода становится результатом соответствующей операции.


class Vector:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    # Перегружаем оператор +
    def __add__(self, other):
        return Vector((self.x + other.x, self.y + other.y))

    def as_point(self):
        return self.x, self.y

    # Формируем удобное отображение объекта при выводе функцией print()
    def __str__(self):
        return "V(x:{} y:{})".format(self.x, self.y)

# Создаем экземпляры класса (объекты)
v1 = Vector((10, 15))
v2 = Vector((12, 10))

# Наши объекты участвуют в операции сложения (+)
v3 = v1 + v2
# На самом деле это работает так:
# v3 = v1.__add__(v2)
# Благодаря перегрузке, мы можем использовать более удобную и привычную запись: v3 = v1 + v2

# Выводим результат
print('v3 = ', v3)
# Функция print() для получения строки для вывода вызывает методы __str__()
print('v3 + v3 =', v3 + v3)

# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html
