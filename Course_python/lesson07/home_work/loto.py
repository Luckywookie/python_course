#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
import random

__author__ = 'belykh_olga'


# Создадим класс карточки (массив 3х9)
# SOS!!! Не стабильно по 5 цифр получается
# Как будто он затирает и ищет в затертых уже. Пробовала вынести в отдельный класс и наследовать, тоже самое получилось
class Card:
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
        h1 = k[:9]
        h2 = k[9:18]
        h3 = k[18:27]
        # отсортируем по возрастанию
        h1.sort()
        h2.sort()
        h3.sort()
        # соединим в матрицу
        self.m = [h1, h2, h3]

    @property
    def struct(self):
        new = []
        for i in self.m:
            # создадим список уникальных рандомных чисел, которые будем выкидывать из карточек
            for s in xrange(1, 5):
                # используем рандомный выбор чисел из списков
                # видимо он иногда повторяется, поэтому выкидывается меньшее количество чисел из карточки
                r = random.choice(i)
                if r in new:
                    continue
                else:
                    new.append(r)

            # далее в каждой строчке выбросим все значения из списка рандомных чисел,
            # заменив их на пробел
            for j in i:
                if j in new:
                    for k in new:
                        if k == j:
                            i.insert(i.index(k), ' ')
                            i.remove(j)
#        print 'список', new
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
                    i.insert(i.index(ch), ' ')
                    i.remove(ch)

    # метод является ли карточка пустая
    # не смогла проверить работает ли метод
    def clean_card(self):
        for i in self.card:
            if all(number == ' ' for number in i):
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


n = Card()
human = UpdateCard(n.struct, 'Игрок')

m = Card()
computer = UpdateCard(m.struct, 'Компьютер')

nn = Lot()
while nn.boch:
    human.view()
    computer.view()
    l = nn.choice_lot
    nn.remove_lot(l)
    print 'Выпал бочонок номер: ', l
#    print nn.view_lot
    r_human = raw_input('Выберите продолжать(Y) или зачеркнуть цифру(N), для выхода из игры нажмите (E):  ')
    if r_human == 'Y':
        computer.delete_choise(int(l))
        if human.find_lot(int(l)):
            print 'Вы проиграли'
            break
        else:
            if computer.clean_card():
                print 'Карточка соперника пуста'
                break
        continue
    elif r_human == 'N':
        print 'Зачеркиваем бочонок номер: ', l
        computer.delete_choise(int(l))
        if human.find_lot(int(l)):
            human.delete_choise(int(l))
            if human.clean_card():
                print 'Поздравляем с победой'
                break
        else:
            print 'Вы проиграли'
            break
    elif r_human == 'E':
        break
    else:
        print 'Выберите Y или N'
else:
    if human.clean_card():
        print 'Поздравляем с победой'
    else:
        print 'что-то пошло не так или Вы вышли из игры'


