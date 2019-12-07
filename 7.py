#!/usr/bin/python3.6

import string

from copy import copy
from itertools import permutations

inp = []
with open('7', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

POS = 0
IMM = 1
mode = POS

def run(reg, i, i_value):
    value = None
    while True:
        ins = reg[i]
        mp1 = int(ins / 100) % 10
        mp2 = int(ins / 1000) % 10
        mp3 = int(ins / 10000) % 10
        ins = ins % 100

        if ins == 99:
            break
        r1 = i+1 if mp1 == IMM else reg[i+1]
        r2 = i+2 if mp2 == IMM else reg[i+2]
        try:
            r3 = i+3 if mp3 == IMM else reg[i+3]
        except IndexError:
            pass # if this happens, you don't need it
        if ins == 1:
            reg[r3] = reg[r1] + reg[r2]
            i += 4
        elif ins == 2:
            reg[r3] = reg[r1] * reg[r2]
            i += 4
        elif ins == 3:
            reg[r1] = i_value.pop(0)
            i += 2
        elif ins == 4:
            value = reg[r1]
            i += 2
            break
        elif ins == 5:
            if reg[r1]:
                i = reg[r2]
            else:
                i += 3
        elif ins == 6:
            if reg[r1] == 0:
                i = reg[r2]
            else:
                i += 3
        elif ins == 7:
            reg[r3] = 1 if reg[r1] < reg[r2] else 0
            i += 4
        elif ins == 8:
            reg[r3] = 1 if reg[r1] == reg[r2] else 0
            i += 4
        else:
            print(f'Bad opcode: {ins} - FAILED')
            break
    return reg, i, i_value, value

for p in permutations([0, 1, 2, 3, 4]):
    amp = 0
    amps = []
    for phase in p:
        reg = copy(inp)
        amp = run(reg, 0, [phase, amp])[-1]
        amps.append(amp)
    p1 = max(p1, amp)
    if p1 == amp:
        p1_perm = tuple(map(str, p))
        p1_amps = tuple(map(str, amps))

for p in permutations([5, 6, 7, 8, 9]):
    regs = []
    inps = []
    for x in range(5):
        regs.append(copy(inp))
        inps.append([p[x]])
    ips = [0] * 5
    amp = 0
    amps = []
    while amp is not None:
        for x in range(5):
            inps[x].append(amp)
            regs[x], ips[x], inps[x], amp = run(regs[x], ips[x], inps[x])
            if amp is not None:
                amps.append(amp)
        last_amp = last_amp if amp is None else amp
    p2 = max(p2, last_amp)
    if p2 == last_amp:
        p2_perm = tuple(map(str, p))
        p2_amps = tuple(map(str, amps))

print(f'Part 1: {p1}')
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
