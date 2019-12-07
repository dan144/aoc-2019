#!/usr/bin/python3.6

import string

from copy import copy

inp = []
with open('7', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

POS = 0
IMM = 1
mode = POS

def run(reg, i_value):
    i = 0
    values = []
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
        r3 = i+3 if mp3 == IMM else reg[i+3]
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
            values.append(value)
            i += 2
            if reg[i] % 100 == 99:
                line = f'Diagnostic code: {value}'
            else:
                line = f'Test: {value}{" - FAILED " if value != 0 else ""}'
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
    return values

from itertools import permutations
perms = permutations([0, 1, 2, 3, 4])
m_m = 0
vals = []
for p in perms:
    m = [0]
    for phase in p:
        reg = copy(inp)
        amp = run(reg, [phase, m[-1]])
        print(amp)
        m.append(amp[0])
        vals.append(amp[0])
    val = max(vals)
    print(val)
    # m = int(str('{:05}'.format(amp[0]))[::-1])
    if val > m_m:
        m_m = val
        p1 = m_m

# not 12340
# not 96710
# not 97610
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
