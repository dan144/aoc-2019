#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('2', 'r') as f:
    for line in f:
        inp = list(map(int, line.split(',')))

p1 = 0
p2 = 0

comp = Intcode(inp)
p1 = comp.run_with_nv(12, 2)
print(f'Part 1: {p1}')

for n in range(100):
    for v in range(100):
        comp = Intcode(inp)
        if comp.run_with_nv(n, v) == 19690720:
            p2 = 100 * n + v
            break
    if p2:
        break

print(f'Part 2: {p2}')
