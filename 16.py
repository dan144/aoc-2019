#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('16', 'r') as f:
    inp = list(f.readline().strip())

p1 = 0
p2 = 0

base = [0, 1, 0, -1]
for phase in range(100):
    print(phase)
    n_pattern = []
    for elem in range(len(inp)):
        pattern = []
        for i in range(len(base)):
            pattern.extend([base[i]] * (elem+1))
        #pattern.pop(0)
        #print(pattern)
        value = 0
        for j in range(len(inp)):
            #print(f'{int(inp[j])} * {pattern[(j+1) % len(pattern)]}')
            value += int(inp[j]) * pattern[(j+1) % len(pattern)]
        n_pattern.append(abs(value) % 10)
    inp = list(map(str, n_pattern))
    #print(''.join(inp))
    #input()

p1 = ''.join(inp[:8])
print(f'Part 1: {p1}')



print(f'Part 2: {p2}')
