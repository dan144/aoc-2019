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

loc = int(''.join(map(str, inp[:7])))
# elem n only affect by things after since base pattern begins with n zeros
signal = (copy(inp) * 10000)[loc:]
items = len(signal)
for phase in range(100):
    sys.stdout.write(f'\rPhase {phase}')
    n_pattern = []
    value = sum(signal) # pattern is all ones from location of signal onward
    for elem in range(items):
        n_pattern.append(abs(value) % 10)
        value -= signal[elem] # leave this element behind
    signal = n_pattern

print()
p2 = ''.join(map(str, signal[:8]))
print(f'Part 2: {p2}')
