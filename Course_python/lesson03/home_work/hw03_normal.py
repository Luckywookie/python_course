#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Белых Ольга

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fib(n):
    f = [1, 1]
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    print f

fib(10)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    lst = []
    i = 0
    l = len(origin_list)

    while i < l:
        mini = min(origin_list)
        lst.append(mini)
        origin_list.remove(mini)
        i += 1
    print lst

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filter_my(filter_lst, delitel):
    lst = []
    i = 0
    l = len(filter_lst)

    while i < l:
        if filter_lst[i] % delitel == 0:
            lst.append(filter_lst[i])
        i += 1
    print lst

filter_my([1, 5, 9, 5, 18], 3)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def paral(a, b, c, d):
    if a[0] == b[0] and c[0] == d[0]:
        if b[1] == c[1] and d[1] == a[1]:
            return True


print paral((1, 1), (1, 4), (4, 4), (4, 1))

