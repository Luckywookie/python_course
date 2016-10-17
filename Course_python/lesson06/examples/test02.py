#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

f = [[random.randint(1, 91) for x in xrange(1, 10)] for y in xrange(1, 4)]
f[0].sort()
f[1].sort()
f[2].sort()
print f


a = []

for r in range(3):
    a.append([])
    for c in range(9):
        g = random.randint(1, 91)
        if g in a[r]:
            continue
        else:
            a[r].append(g)
            a[r].sort()

for r in a:
    print(r)

k = []

for v in range(1, 100):
    g = random.randint(1, 91)
    if g in k:
        continue
    else:
        k.append(g)

h1 = k[:9]
h2 = k[9:18]
h3 = k[18:27]

h1.sort()
h2.sort()
h3.sort()

h = [h1, h2, h3]

print h