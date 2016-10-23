#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

import random

# GitHub проверка
"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

__author__ = 'belykh_olga'


# Необходимо сделать наоборот, сначала цифры 5*3 и добавить пробелы
class CardNewBase:
    def __init__(self):
        k = []
        for v in range(1, 100):
            g = random.randint(1, 90)
            # если в списке уже присутствует это значение, то перевести опять в начало цикла
            if g in k:
                continue
            else:
                k.append(g)
        # так как в каждой из трех строк не должны повторять значения, создадим сначала единый список
        # а потом разъединим его на три части по 9 штук
        h1 = k[:5]
        h2 = k[5:10]
        h3 = k[10:15]
        # отсортируем по возрастанию
        h1.sort()
        h2.sort()
        h3.sort()
        # соединим в матрицу
        self.m = [h1, h2, h3]

    @property
    def structure_card(self):
        for i in self.m:
            # Необходимо добавить пробелы к спискам
            for k in xrange(1, 5):
                i.insert(random.randint(0, len(i)), ' ')
        return self.m


class UpdateCard:
    def __init__(self, card, name):
        self.card = card
        self.name = name

    def view(self):
        # выведем получившуюся матрицу чисел
        print '{y:-^30}'.format(y=self.name)
        for i in self.card:
            for j in i:
                print '{}'.format(j),
            print
        print '{:-^24}'.format('-')

    # метод поиска цифр на карточке
    def find_lot(self, ch):
        for i in self.card:
            for j in i:
                if j == ch:
                    return True

    # метод зачеркивания цифр на карточке
    def delete_choise(self, ch):
        for i in self.card:
            for j in i:
                if j == ch:
                    i.insert(i.index(ch), 'X')
                    i.remove(ch)

    # метод является ли карточка пустая
    def clean_card(self):
        s = 0
        for stroka in self.card:
            for i in stroka:
                if i == 'X':
                    s += 1
        if s == 15:
            return True


# Создадим класс Бочонок
class Lot:
    def __init__(self):
        self.boch = [_ for _ in xrange(1, 91)]

    @property
    def choice_lot(self):
        return random.choice(self.boch)

    def remove_lot(self, x):
        return self.boch.remove(x)

    @property
    def view_lot(self):
        return self.boch


n = CardNewBase()
human = UpdateCard(n.structure_card, 'Игрок')

m = CardNewBase()
computer = UpdateCard(m.structure_card, 'Компьютер')

nn = Lot()
while nn.boch:
    human.view()
    computer.view()
    l = nn.choice_lot
    print 'Выпал бочонок номер: ', l

    if computer.clean_card():
        print 'Карточка соперника пуста. ВЫ ПРОИГРАЛИ :((.'
        break
    elif human.clean_card():
        print '***ПОЗДРАВЛЯЕМ С ПОБЕДОЙ***'
        break
    else:
        r_human = raw_input('Выберите продолжать(Y) или зачеркнуть цифру(N), для выхода из игры нажмите (E):  ')
        # Если пользователь выбрал продолжать
        if r_human == 'Y':
            computer.delete_choise(int(l))  # удаляем цифру из карточки соперника
            nn.remove_lot(l)
            # если цифра все таки присутствует в карточке игрока, выходим из цикла
            if human.find_lot(int(l)):
                print 'ВЫ ОШИБЛИСЬ И ПРОИГРАЛИ'
                break
            continue
        # Если пользователь выбрал зачеркнуть цифру
        elif r_human == 'N':
            computer.delete_choise(int(l))  # удаляем цифру из карточки соперника
            nn.remove_lot(l)
            print 'Зачеркиваем бочонок номер: ', l
            if human.find_lot(int(l)):
                human.delete_choise(int(l))
            else:
                print 'ВЫ ОШИБЛИСЬ И ПРОИГРАЛИ'
                break
        elif r_human == 'E':
            break
        else:
            # если другая буква, цифра из карточек не удаляется
            print 'Выберите Y или N'

# input("Press Enter")
