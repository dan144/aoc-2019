#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('21', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

NL = '\n'
INS = [
    'NOT A J',
    'NOT B T',
    'OR T J',
    'NOT C T',
    'OR T J',
    'AND D J',
]
cmd_str = NL.join(INS) + NL + 'WALK' + NL
cmds = list(map(ord, cmd_str))

comp = Intcode(inp, cmds)
o = ''
while not comp.done:
    c = comp.run_until_output()
    if c > 255:
        p1 = c
    else:
        o += chr(c)
print(o)

print(f'Part 1: {p1}')



print(f'Part 2: {p2}')
