#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'belykh_olga'

import os
import shutil
import sys
import re

print 'os.name = ', os.name
print 'os.environ = ', os.environ
print 'os.getcwd() = ', os.getcwd()
print 'Файлы в текущей папке: ', os.listdir(os.getcwd())
print "current dir = ", os.path.dirname(__file__)

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

f = raw_input('Введите 1, чтобы создать папку или 0, чтобы удалить')
name = raw_input('Введите имя папки')

if f == '1':
    try:
        os.mkdir(name)
    except OSError:
        print('Такая директория уже существует')
elif f == '0':
    try:
        os.rmdir(name)
    except OSError:
        print('Такой директории не существует')
else:
    print 'Программа завершена'


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

lst = os.listdir(os.getcwd())

for i in lst:
    if os.path.isdir(i):
        print i


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

filename = os.path.split(str(sys.argv))
openfile = str(re.sub(u'[^А-Яа-яA-Za-z\.\_\d]*', u'', filename[-1]))
print openfile

shutil.copy(openfile, 'copy.py')

