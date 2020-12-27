#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('5', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

comp = Intcode(inp, [1])
p1 = comp.run_with_output()
print(f'Part 1: {p1}')

comp = Intcode(inp, [5])
p2 = comp.run_with_output()
print(f'Part 2: {p2}')
