#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

__author__ = 'belykh_olga'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) - в Linux начинается с /, в Windows с имени диска
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь. Исходной директорией считать ту,
# в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

print 'sys.argv = ', sys.argv


def print_help():
    print u"help - получение справки"
    print u"mkdir <dir_name> - создание директории"
    print u"ping - тестовый ключ"


def make_dir():
    if not dir_name:
        print u"Необходимо указать имя директории вторым параметром"
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print u'директория {} создана'.format(dir_name)
    except OSError:
        print u'директория {} уже существует'.format(dir_name)


def ping():
    print "pong"

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print "Задан неверный ключ"
        print "Укажите ключ help для получения справки"
