#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

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

y = [h1, h2, h3]

# print y

new = []
for i in y:
    for s in xrange(1, 5):
        r = random.choice(i)
        if r in new:
            continue
        else:
            new.append(r)
#    print new
    for j in i:
        if j in new:
            for k in new:
                if k == j:
                    i.insert(i.index(k), ' ')
                    i.remove(j)

# print new

for i in y:
    for j in i:
        print '{}'.format(j),
    print

