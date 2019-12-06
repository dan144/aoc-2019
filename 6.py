#!/usr/bin/python3.6

import string

from copy import copy

inp = []
with open('6', 'r') as f:
    for line in f:
        inp.append(line.strip().split(')'))

p1 = 0
p2 = 0

orbits = {}
for inner, outer in inp:
    if inner in orbits:
        orbits[inner].append(outer)
    else:
        orbits[inner] = [outer]

o = orbits['COM']
level = 0
while o:
    level += 1
    p1 += len(o) * level
    n = []
    for b in o:
        n.extend(orbits.get(b, []))
    o = n

def parent(k):
    for i, o in orbits.items():
        if k in o:
            return [i]
    return []

you = parent('YOU')
while parent(you[0]):
    you = parent(you[0]) + you

san = parent('SAN')
while parent(san[0]):
    san = parent(san[0]) + san

for i in range(len(you)):
    if you[i] in san:
        p2 = len(you) + len(san) - 2 - i - san.index(you[i])

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
