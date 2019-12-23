#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('23', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

comps = []
for c in range(50):
    comps.append(Intcode(inp, [c, -1]))

#comps[0].inputs.extend([-1, -1])
NAT = [0, 0]
dst = 0
idled = set()
last_y = -1
while not p2:
    o = []
    try:
        for _ in range(3):
            o.append(comps[dst].run_until_output())
        idled = set()
        dst, x, y = o
        if dst == 255:
            if p1 == 0:
                p1 = y
            NAT = x, y
            dst = 0
        else:
            comps[dst].inputs.extend([x, y])
    except IndexError:
        if dst != 255:
            idled.add(dst)
        if list(sorted(idled)) == list(range(50)):
            if last_y == NAT[1]:
                p2 = last_y
            comps[0].inputs.extend(NAT)
            last_y = NAT[1]
        dst += 1
        dst = dst % 50

print(f'Part 1: {p1}')

#comp = Intcode(inp)
#while not comp.done:
#    o = comp.run_until_output()

print(f'Part 2: {p2}')
