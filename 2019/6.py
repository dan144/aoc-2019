#!/usr/bin/env python3

import string

from copy import copy

inp = []
with open('6', 'r') as f:
    for line in f:
        inp.append(line.strip().split(')'))

p1 = 0
p2 = 0

orbits = {outer: inner for inner, outer in inp}
for planet in orbits.keys():
    while orbits.get(planet):
        p1 += 1
        planet = orbits.get(planet)

you = [orbits['YOU']]
while orbits.get(you[-1]):
    you.append(orbits.get(you[-1]))
san = [orbits['SAN']]
while san[-1] not in you:
    san.append(orbits.get(san[-1]))

you = you[:you.index(san[-1])+1]
p2 = len(san) + len(you) - 2

print('Part 1:', p1)
print('Part 2:', p2)

# vizualize
you_hops = '->'.join(you)
san_hops = '->'.join(san)
with open('dot6', 'w') as f:
    f.write('digraph ORBITS {\n')
    f.write('    nodesep=0.1;\n')
    f.write('    node[shape=circle];\n')
    f.write('    sep=0.1; \n')
    f.write('    edge[weight=1];\n')
    for outer, inner in orbits.items():
        path = '{}->{}'.format(outer, inner)
        color = 'red' if path in you_hops or path in san_hops or outer in {'YOU', 'SAN'} else 'black'
        f.write('    "{}" -> "{}" [ color={} ];\n'.format(inner, outer, color))
        if color == 'red':
            f.write('    "{}" [color=red];\n'.format(inner))
    f.write('    YOU [color=red,style=filled];\n')
    f.write('    SAN [color=red,style=filled];\n')
    f.write('}')
print('Run `dot -Tsvg -odot6.svg dot6 -v -Kdot`')
