#!/usr/bin/env python3

from intcode import Intcode

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
import re
for line in inp:
    moon = list(map(int, re.findall(r'-?\d+', line)))
    moon += [0, 0, 0]
    moons.append(moon)
for moon in moons:
    print(moon)

for t in range(1000):
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

t += 1
print(t)
for moon in moons:
    PE = sum(map(abs, moon[:VX]))
    KE = sum(map(abs, moon[VX:]))
    p1 += PE* KE

print(f'Part 1: {p1}')



print(f'Part 2: {p2}')
