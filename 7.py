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
            pass
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

perms = permutations([0, 1, 2, 3, 4])
m_m = 0
vals = []
for p in perms:
    m = [0]
    for phase in p:
        reg = copy(inp)
        _, _, amp = run(reg, 0, [phase, m[-1]])
        m.append(amp)
        vals.append(amp)
    val = max(vals)
    if val > m_m:
        m_m = val
        p1 = m_m

perms = permutations([5, 6, 7, 8, 9])
m_m = 0
vals = []
for p in perms:
    val = 0
    regs = []
    for _ in range(5):
        regs.append(copy(inp))
    ips = [0] * 5
    amp = 0
    first = True
    while True:
        for x in range(5):
            reg = regs[x]
            ip = ips[x]
            regs[x], ips[x], amp = run(reg, ip, [p[x], amp] if first else [amp])
        first = False
        if amp is None:
            break
        vals.append(amp)
    val = vals[-1]
    if val > m_m:
        m_m = val
        p2 = m_m

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
