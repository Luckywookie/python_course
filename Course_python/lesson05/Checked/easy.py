#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'belykh_olga'

import os

# 2016.10.17_08:11:47 checked. prusanov
# Отлично!

def chdr():
    name = raw_input('Введите имя папки \n')
    try:
        os.chdir(name)
        print 'Вы успешно перешли в директорию: ', os.getcwd()
    except OSError:
        print('Такой директории не существует')


def lstdr():
    try:
        print 'В текущей директории находятся: \n', os.listdir(os.getcwd())
    except OSError:
        print('Такой директории не существует')


def rmdr():
    name = raw_input('Введите имя папки \n')
    try:
        os.rmdir(name)
        print 'Вы успешно удалили папку: ', name
    except OSError:
        print('Такой директории не существует')


def mkdr():
    name = raw_input('Введите имя папки \n')
    try:
        os.mkdir(name)
        print 'Вы успешно создали папку: ', name
    except OSError:
        print('Такая директория уже существует')

