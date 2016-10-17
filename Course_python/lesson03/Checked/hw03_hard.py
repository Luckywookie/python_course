#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Белых Ольга

# Задание-1:
# Написать программу выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# 2016.10.07_03:26:00 checked. prusanov
# Отлично!

# Сделаем функцию упрощения дроби по алгоритму Евклида
def evkl(a, b):
    if b == 0:
        return a
    else:
        return evkl(b, a % b)

f = raw_input('Введите выражение в формате -1 2/3 + -2 1/3, знак может быть разный ')

if not f.find(' + ') == -1:         # if ' + ' in f:   <- кажется, это то, что Вы хотели сделать
    str_f = f.split(' + ')
    act = '+'
elif not f.find(' - ') == -1:
    str_f = f.split(' - ')
    act = '-'
else:
    print 'error'

frac1 = str_f[0].split(' ')
frac2 = str_f[1].split(' ')


# функция для нахождения целой части, числителя, знаменателя и знака
def fr(ff):
    if len(ff) > 1:
        fract = ff[1]
        unit = abs(int(ff[0]))
        numer, denom = str(fract).split('/')
    else:
        if not ff[0].find('/') == -1:
            fract = ff[0]
            unit = 0
            numer, denom = str(fract).split('/')
        else:
            unit = abs(int(ff[0]))
            denom = 1
            numer = 0
    sign = ff[0][0]
    sum_num = int(unit) * int(denom) + abs(int(numer))

    return sign, sum_num, unit, denom

sign1, sum_num1, unit1, denominator1 = fr(frac1)
sign2, sum_num2, unit2, denominator2 = fr(frac2)

# print sign2, sum_num2, unit2, denominator2
# Выполним приведение к заменателю двух дробей
if sign1 == '-':
    ch1 = -sum_num1 * int(denominator2)
else:
    ch1 = sum_num1 * int(denominator2)

if sign2 == '-':
    ch2 = -sum_num2 * int(denominator1)
else:
    ch2 = sum_num2 * int(denominator1)

if act == '+':
    ch = ch1 + ch2
elif act == '-':
    ch = ch1 - ch2

# Вычислим общий знаменатель
denominator = int(denominator1) * int(denominator2)
number = abs(ch) // denominator
dr = abs(ch) - number * denominator
# Сделаем упрощение дроби
fraction = abs(evkl(denominator, dr))
# Выедем результат
if ch < 0:
    if dr and number:
        print 'Результат: -{} {}/{}'.format(number, dr/fraction, denominator/fraction)
    elif number:
        print 'Результат: -{}'.format(number)
    elif dr:
        print 'Результат: -{}/{}'.format(dr / fraction, denominator / fraction)
elif ch > 0:
    if dr and number:
        print 'Результат: {} {}/{}'.format(number, dr/fraction, denominator/fraction)
    elif number:
        print 'Результат: {}'.format(number)
    elif dr:
        print 'Результат: {}/{}'.format(dr / fraction, denominator / fraction)


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

