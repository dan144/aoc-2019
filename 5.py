#!/usr/bin/python3.6

import string

inp = []
with open('5', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

POS = 0
IMM = 1
mode = POS

def run(reg, m_val, n, v):
    i = 0
    # reg[1] = n
    # reg[2] = v
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
            reg[r1] = m_val
            i += 2
        elif ins == 4:
            m_val = reg[r1]
            i += 2
            print(m_val)
        else:
            print(f'error: {ins}')
            break
    return m_val

m_val = 1
from copy import copy
reg = copy(inp)
m_val = run(reg, m_val, 0, 0)
p1 = m_val

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
