#!/usr/bin/env python3

import re

from copy import deepcopy
from math import gcd

inp = []
with open('12', 'r') as f:
    for line in f:
        inp.append(line)

p1 = 0
p2 = 0

X = 0
Y = 1
Z = 2
VX = 3
VY = 4
VZ = 5

moons = []
for line in inp:
    moon = list(map(int, re.findall(r'-?\d+', line)))
    moon += [0, 0, 0]
    moons.append(moon)
o_pos = deepcopy(moons)

def step():
    global moons
    for i in range(len(moons)):
        for j in range(len(moons)):
            if i <= j:
                continue
            m1 = moons[i]
            m2 = moons[j]

            # gravity
            for v in (VX, VY, VZ):
                if m1[v-3] == m2[v-3]:
                    continue
                m1[v] += (1 if m1[v-3] < m2[v-3] else -1)
                m2[v] += (1 if m2[v-3] < m1[v-3] else -1)

    # velocity
    for moon in moons:
        for p in (X, Y, Z):
            moon[p] += moon[p+3]

for t in range(1000):
    step()
for moon in moons:
    PE = sum(map(abs, moon[:VX]))
    KE = sum(map(abs, moon[VX:]))
    p1 += PE* KE

print(f'Part 1: {p1}')


def lcm(ns):
    v = 1
    for x in ns:
        v = v * x // gcd(v, x)
    return v


moons = deepcopy(o_pos)
r = [0, 0, 0]
step()
steps = 1
while not all(r):
    for x in range(3):
        if r[x]:
            continue
        for i in range(len(moons)):
            if moons[i][x+3] != 0 or moons[i][x] != o_pos[i][x]:
                break
        else:
            r[x] = steps
    step()
    steps += 1

p2 = lcm(r)
print(f'Part 2: {p2}')
