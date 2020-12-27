#!/usr/bin/env python3

import string

inp = []
with open('4', 'r') as f:
    inp = f.readline()

p1 = 0
p2 = 0

l, h = inp.split('-')

for x in range(int(l), int(h)+1):
    s = str(x)
    p1_adj = False
    p2_adj = False
    adj_c = 0
    if not any(d*2 in s for d in string.digits) or sorted(s) != list(s):
        continue
    p1 += 1
    p2 += any(d*2 in s and not d*3 in s for d in string.digits)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
