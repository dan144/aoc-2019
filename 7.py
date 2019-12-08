#!/usr/bin/env python3

from itertools import permutations

from intcode import Intcode

inp = []
with open('7', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

for p in permutations([0, 1, 2, 3, 4]):
    amp = 0
    amps = []
    for phase in p:
        comp = Intcode(inp, [phase, amp])
        amp = comp.run_until_output()
        amps.append(amp)
    p1 = max(p1, amp)
    if p1 == amp:
        p1_perm = tuple(map(str, p))
        p1_amps = tuple(map(str, amps))

print(f'Part 1: {p1}')

for p in permutations([5, 6, 7, 8, 9]):
    comps = []
    for x in range(5):
        comps.append(Intcode(inp, [p[x]]))

    amp = 0
    amps = []
    while any(not comp.done for comp in comps):
        for x in range(5):
            comps[x].inputs.append(amp)
            amp = comps[x].run_until_output()
            if amp is not None:
                amps.append(amp)
        last_amp = last_amp if amp is None else amp
    p2 = max(p2, last_amp)
    if p2 == last_amp:
        p2_perm = tuple(map(str, p))
        p2_amps = tuple(map(str, amps))

print(f'Part 2: {p2}')

# visualization
print()
print('Part 1')
print()
l = len(str(max(map(int, p1_amps))))
header_fmt = ' {} {:' + str(l+1) + '}'
header = '  '
line = '0->'
for i in range(len(p1_amps)):
    header += header_fmt.format('ABCDE'[i], '(' + p1_perm[i] + ')')
    line += p1_amps[i]
    if i != len(p1_perm) - 1:
        line += ('-'*(l+3 - len(p1_amps[i]))) + '>'
print(header)
print(line)
print()
print()

print('Part 2')
print()
l = len(str(max(map(int, p2_amps))))
header = '  '
for i in range(len(p2_amps)):
    if i < len(p2_perm):
        header += header_fmt.format('ABCDE'[i], '(' + p2_perm[i] + ')')
    elif i == len(p2_perm):
        print(header)

    if i == 0:
        line = '0->'
    elif i % len(p2_perm) == 0:
        print(line)
        print('   .' + '-' * (len(line) - 5) + "'")
        print('   v')
        line = '   '
    line += p2_amps[i]
    if i % len(p2_perm) != len(p2_perm) - 1:
        line += ('-'*(l+1 - len(p2_amps[i]))) + '>'
print(line)
print()
