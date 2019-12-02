#!/usr/bin/python3.6

from copy import copy

inp = []
with open('2', 'r') as f:
    for line in f:
        inp = list(map(int, line.split(',')))

p1 = 0
p2 = 0

def run(reg, n, v):
    i = 0
    reg[1] = n
    reg[2] = v
    while True:
        ins = reg[i]
        if ins == 99:
            break
        r1 = reg[i+1]
        r2 = reg[i+2]
        w = reg[i+3]
        if ins == 1:
            reg[w] = reg[r1] + reg[r2]
        elif ins == 2:
            reg[w] = reg[r1] * reg[r2]
        else:
            print(f'error: {ins}')
            break
        i += 4

reg = copy(inp)
run(reg, 12, 2)
p1 = reg[0]

for n in range(100):
    for v in range(100):
        reg = copy(inp)
        run(reg, n, v)
        if reg[0] == 19690720:
            p2 = 100 * n + v
            break
    if p2:
        break

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
