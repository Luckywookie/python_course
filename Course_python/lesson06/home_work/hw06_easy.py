#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

__author__ = 'belykh_olga'


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Side:
    def __init__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2

    @property
    def otr(self):
        l = math.sqrt((self.dot2.x - self.dot1.x) ** 2 + (self.dot2.y - self.dot1.y) ** 2)
        return l


class Pol:
    def __init__(self, *args):
        self._dots = args

    @property
    def sides(self):
        sides = []
        prev_dot = self.dots[-1]
        for dot in self.dots:
            sides.append(Side(prev_dot, dot))
            prev_dot = dot
        return sides

    @property
    def dots(self):
        return self._dots

    @property
    def perimeter(self):
        return sum([s.otr for s in self.sides])


polygon = Pol(Dot(0, 0), Dot(5, 5), Dot(0, 5), Dot(5, 0))

print polygon.perimeter



class Figure:
    def __init__(self, a, b, c):
        self.la = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        self.lb = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
        self.lc = math.sqrt((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2)

    @property
    def angle(self):
        alfa = math.acos(((self.la ** 2 + self.lb ** 2 - self.lc ** 2) / (2 * self.la * self.lb)) * math.pi / 180)
        return alfa

    @property
    def p_triangle(self):
        p = round((self.la + self.lb + self.lc), 1)
        return 'Периметр треугольника {} см'.format(p)

    @property
    def area_triangle(self):
        s = round((0.5 * self.la * self.lb * math.sin(self.angle)), 1)
        return 'Площадь треугольника: {} см2'.format(s)

    @property
    def height(self):
        len_h = round((self.lb * math.sin(self.angle)), 1)
        return 'Высота треугольника равна: {} см'.format(len_h)


new = Figure((1, 0), (3, 5), (5, 0))

print new.area_triangle, new.height, new.p_triangle

# print new.lb, new.la, new.lc

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.

'''
    Рассмотрим трапецию вида:

        B  _______  C
         /         \
        /           \
    A  /_____________\  D     ось X


'''


class Trapez:
    def __init__(self, a, b, c, d):
        # Вычислим длины трапеции по координатам точек - AB, BC, CD, DA, а так же ее диагонали AC и BD
        self.ab = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
        self.bc = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
        self.cd = math.sqrt((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2)
        self.da = math.sqrt((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2)
        self.ac = math.sqrt((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2)
        self.bd = math.sqrt((d[0] - b[0]) ** 2 + (d[1] - b[1]) ** 2)

    @property
    def trap(self):
        if self.ac == self.bd:
            return 'Равнобедренная трапеция'
        else:
            return 'Не равнобедренная трапеция'

    @property
    def peri(self):
        return 'Периметр трапеции: {} см'.format(round((self.ab + self.bc + self.cd + self.da), 1))

    @property
    def area_trap(self):
        if self.ac == self.bd:
            # S = ((BC+DA)/2)*sqrt(4*(AB**2)-(BC-DA)**2)
            s = ((self.bc + self.da) / 2) * math.sqrt(4 * (self.ab**2) - (self.bc - self.da)**2)
            return 'Площадь равнобедренной трапеции: {} см'.format(s)
        else:
            return 'Не могу вычислить площадь данной фигуры'


tr = Trapez((0, 0), (5, 3), (5, 9), (0, 12))

print tr.peri, tr.trap, tr.area_trap


