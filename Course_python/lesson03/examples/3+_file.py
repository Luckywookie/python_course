#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================================
#         Работа с файлами
# =================================
import os

path = 'files/text.txt'  # не самый хороший способ задания пути
path = os.path.join('files', 'text.txt')  # хороший кроссплатформенный метод указания пути

f = open(path, 'r', encoding='UTF-8')
print(f.readlines())  # Считываем всю информацию из файла в виде списка строк
f.close()

# Наиболее правильный способ работы с файлами
# По окончанию инструкции with файл гарантированно будет закрыт, даже если произойдет ошибка
with open(path, 'r', encoding='UTF-8') as f:
    print(f.readlines())

DIR = 'files'

wanted_symbol = "@"
# wanted_symbol = "+"  # раскомментируйте, чтобы посмотреть как работает, если не найдено то, что искали
with open(os.path.join(DIR, 'data'), 'r', encoding='UTF-8') as f:
    for line in f:  # считываем файл построчно
        if wanted_symbol in line:  # пока не найдем нужную информацию
            print(line)
            break  # как нашли, заканчиваем чтение файла
    else:
        print("Искомая информация в файле '%s' не найдена" % f.name)
    # Файл будет автоматически закрыт по окончанию инструкции with

