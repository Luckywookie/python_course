#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# ***********************  Human  **********************************
class Human(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.age = age
        self.surname = surname

    @property
    def view_fullname(self):
        return self.name + ' ' + self.surname


# **************************  Student  *******************************
class Student(Human):
    def __init__(self, name, surname, age, class_number):
        Human.__init__(self, name, surname, age)
        self.class_number = class_number
        self.parent = None

    def has_parent(self, mother, father):
        self.parent = mother + ' и ' + father
        return 'Родители:  ' + self.parent

    @property
    def view_class_number(self):
        return self.class_number
        #return 'Ученик', self.name, self.surname, 'учится в классе', self.class_number


# **************************  Teacher  *******************************
class Teacher(Human):
    def __init__(self, name, surname, age, lesson):
        Human.__init__(self, name, surname, age)
        self.lesson = lesson

    def teach_class(self, *args):
        return args


parent1 = Human('Наталья', 'Новикова', 41)
parent2 = Human('Олег', 'Новиков', 44)

#print student1.has_parent(parent1.view_fullname, parent2.view_fullname)

teacher1 = Teacher('Olga', 'Ivanova', 31, 'Math')
print teacher1.teach_class('5B', '6B', '7D')

teachers = [Teacher('Александра', 'Новиков', 45, 'Математика'),
            Teacher('Нона', 'Беликова', 56, 'Русский'),
            Teacher('Мария', 'Сосновская', 32, 'ИЗО'),
            Teacher('Георгий', 'Лопас', 66, 'Труд'),
            Teacher('Виктория', 'Заповалова', 25, 'Литература'),
            Teacher('Виктор', 'Всезнайкин', 39, 'История')]


students = [Student('Андрей', 'Новиков', 12, '6В'),
            Student('Алексей', 'Павлов', 14, '8Г'),
            Student('Нюша', 'Слабая', 11, '5А'),
            Student('Алена', 'Черных', 11, '5А'),
            Student('Боня', 'Куцый', 11, '5А'),
            Student('Ляля', 'Кузнецова', 11, '5В')]

for i in students:
    if i.view_class_number == '5А':
        print i.name, i.surname, i.view_class_number


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
