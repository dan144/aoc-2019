#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('19', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

for x in range(50):
    for y in range(50):
        comp = Intcode(inp, [x, y])
        p1 += comp.run_until_output() == 1
print(f'Part 1: {p1}')

count = []
y = 0
x = 1060 # don't waste time
while not p2:
    x += 1
    count.append([])
    if x == 1:
        continue
    last = 0
    while len(count[-1]) < 2:
        comp = Intcode(inp, [x, y])
        o = comp.run_until_output()
        if o != last:
            if x < 50 and y < 50:
                p1 += 1
            count[-1].append(y)
            last = o
        y += 1
    y = count[-1][0]
    w = count[-1][1] - count[-1][0]
    for s_y in range(count[-1][0], count[-1][1]):
        if all((Intcode(inp, [x+99, s_y]).run_until_output() == 1,
                Intcode(inp, [x, s_y+99]).run_until_output() == 1)):
            p2 = 10000*x + s_y
            break
    print(f'Col {x}, width={w}, range={count[-1]}')

print(f'Part 2: {p2}')
