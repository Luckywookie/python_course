#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.


class Human(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.age = age
        self.surname = surname

    def view_fullname(self):
        return self.name + ' ' + self.surname

 #   def set_name(self, new_name):
 #       self.name = new_name


class Parent(object):
    def __init__(self, name_parent, surname_parent):
        self.name_parent = name_parent
        self.surname_parent = surname_parent


class Student(Human, Parent):
    def __init__(self, name, surname, age, class_number, name_parent, surname_parent):
        Human.__init__(self, name, surname, age)
        Parent.__init__(self, name_parent, surname_parent)
        self.class_number = class_number

    def has_parent(self):
        return self.name_parent + ' ' + self.surname_parent

    def view_class_number(self):
        return 'Ученик учится в классе: ', self.class_number


class Teacher(Human):
    def __init__(self, name, surname, age, lesson):
        Human.__init__(self, name, surname, age)
        self.lesson = lesson

    def teach_class(self, *args):
        return args




# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
