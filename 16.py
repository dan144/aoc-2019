#!/usr/bin/env python3

import sys

from copy import copy

inp = []
with open('16', 'r') as f:
    inp = list(map(int, list(f.readline().strip())))

p1 = 0
p2 = 0

base = [0, 1, 0, -1]

signal = copy(inp)
items = len(signal)
for phase in range(100):
    sys.stdout.write(f'\rPhase {phase}')
    n_pattern = []
    for elem in range(items):
        value = 0
        for j in range(items):
            value += int(signal[j]) * base[((j+1)//(elem+1)) % len(base)]
        n_pattern.append(abs(value) % 10)
    signal = n_pattern

print()
p1 = ''.join(map(str, signal[:8]))
print(f'Part 1: {p1}')



print(f'Part 2: {p2}')
