#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Белых Ольга

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.

import random

a = str(random.randint(1, 10**5))
print 'Число: ', a, ' , максимальная цифра в чсиле: ', max(a)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.

# вариант 1

y = 5
z = 3

y = y + z
z = y - z
y = y - z

print y, z

# вариант 2

r = 4
s = 10

r, s = s, r
print r, s

# вариант 3

s = [r, s][1]
r = [r, s][0]

print r, s

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4
# a*x**2 + b*x + c = 0.
# D = b**2 - 4*a*c

import math

# Решаем уравнение вида a*x**2 + b*x + c = 0.
# Для этого вычислим его дискриминант D = b**2 - 4*a*c и проанализируем его

a = 1
b = -8
c = 12

D = b**2 - 4*a*c

if D > 0:
    x1 = (b*(-1) - math.sqrt(D))/(2*a)
    x2 = (b*(-1) + math.sqrt(D))/(2*a)
    print 'Уравнение имеет два корня', 'x1 = ', x1, ', x2 = ', x2
elif D == 0:
    x = (b*(-1))/(2*a)
    print 'Уравнение имеет один корень', 'x = ', x
else:
    print 'Уравнение не имеет решений'



