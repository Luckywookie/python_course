#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
# Создадим класс карточки (массив 3х9)

'''
class RandCard:
    def __init__(self):
        k = []
        for v in range(1, 100):
            g = random.randint(1, 91)
            # если в списке уже присутствует это значение, то перевести опять в начало цикла
            if g in k:
                continue
            else:
                k.append(g)
        self.lst_k = k
'''


class Card:
    def __init__(self, name):
        self.name = name
        k = []
        for v in range(1, 100):
            g = random.randint(1, 91)
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
        return self.m

    def view(self):
        # выведем получившуюся матрицу чисел
        print '{y:-^30}'.format(y=self.name)
        for i in self.struct:
            for j in i:
                print '{}'.format(j),
            print
        print '{:-^24}'.format('-')

    def find_lot(self):
        if Lot.choice_lot in self.struct:
            return 'Yes'
        else:
            return 'NO'

    def delete_choise(self):
        if nnn.choice_lot in self.struct:
            self.m.remove(nnn.choice_lot)

    def winner(self):
        if not self.struct:
            print 'Поздравляем с победой'


# Создадим класс для выбора бочонка
class Lot:
    def __init__(self):
        self.boch = [_ for _ in xrange(1, 91)]

    @property
    def choice_lot(self):
        return 'Выпал бочонок: {}'.format(random.choice(self.boch))


# Надо создать класс для поиска бочонка в карточке.

human = Card(' Игрок 1 ')
human.view()

computer = Card(' Компьютер ')
computer.view()

nnn = Lot()
print nnn.choice_lot

# создадим программу раздачи лоточков
while human.struct or computer.struct:
    nnn = Lot()
    r_human = raw_input('Выберите продолжать(Y) или зачеркнуть цифру(N), для выхода и игры нажмите (E):  ')
    if r_human == 'Y':
        print Lot().choice_lot
    elif r_human == 'N':
        # не работает метод delete
        human.delete_choise()
        human.view()
    elif r_human == 'E':
        break
    else:
        print 'Выберите Y или N'

# после выхода из цикла проверяем победителя, им окажется тот у кого нет цифр в карточке
if not human.struct:
    print human.winner()
else:
    print computer.winner()

