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
            return reg, i, value
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
    return reg, i, None

for p in permutations([0, 1, 2, 3, 4]):
    amp = 0
    for phase in p:
        reg = copy(inp)
        _, _, amp = run(reg, 0, [phase, amp])
    p1 = max(p1, amp)

for p in permutations([5, 6, 7, 8, 9]):
    regs = []
    for _ in range(5):
        regs.append(copy(inp))
    ips = [0] * 5
    amp = 0
    first = True
    while amp is not None:
        for x in range(5):
            regs[x], ips[x], amp = run(regs[x], ips[x], [p[x], amp] if first else [amp])
        first = False
        last_amp = last_amp if amp is None else amp
    p2 = max(p2, last_amp)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
