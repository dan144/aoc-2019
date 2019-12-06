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
        p2_index = i

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# vizualize
you = you[p2_index:]
san = san[san.index(you[0]):]
you_hops = '->'.join(you)
san_hops = '->'.join(san)
with open('dot6', 'w') as f:
    f.write('digraph ORBITS {\n')
    f.write('    node[color=none; shape=plaintext];\n')
    f.write('    nodesep=0.1; \n')
    f.write('    sep=0.1; \n')
    f.write('    edge[weight=1];\n')
    for inner, outers in orbits.items():
        for outer in outers:
            path = '{}->{}'.format(inner, outer)
            color = 'red' if path in you_hops or path in san_hops or outer in {'YOU', 'SAN'} else 'black'
            line = '    "{}" -> "{}" [ color={} ];\n'.format(inner, outer, color)
            f.write(line)
    f.write('    YOU [color=red,style=filled];\n')
    f.write('    SAN [color=red,style=filled];\n')
    f.write('}')
print('Run `dot -Tsvg -odot6.svg dot6 -v -Kdot`')
