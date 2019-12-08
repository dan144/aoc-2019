#!/usr/bin/env python3

inp = []
with open('1', 'r') as f:
    for line in f:
        inp.append(int(line))

p1 = 0
p2 = 0

for i in inp:
    p1 += int(i / 3) - 2
    while i > 0:
        i = int(i / 3) - 2
        if i > 0:
            p2 += i

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
