#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('13', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

for i in range(len(inp)-2):
    if inp[i] == 0 and inp[i+1] == 3 and inp[i+2] == 0:
        ball = i + 1
        break

p1 = 0
p2 = 0

comp = Intcode(inp)
while not comp.done:
    _, _, t = comp.run_until_n_output(3)
    p1 += t == 2

print(f'Part 1: {p1}')

comp = Intcode(inp)
comp.reg[0] = 2
for r in range(ball - 17, ball + 18):
    comp.reg[r] = 1 # fake wall
while not comp.done:
    comp.inputs.append(0)
    _, _, s = comp.run_until_n_output(3)
    p2 = s

print(f'Part 2: {p2}')
