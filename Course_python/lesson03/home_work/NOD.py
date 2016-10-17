#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Белых Ольга

def evkl(a, b):
    if b == 0:
        return a
    else:
        return evkl(b, a % b)

print evkl(45, 15)
