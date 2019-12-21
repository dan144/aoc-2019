#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('21', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

NL = '\n'

INS = [ # T=? J=?
    'NOT A J', # J=~A
    'NOT B T', # T=~B
    'OR T J',  # J=~A+~B
    'NOT C T', # T=~C
    'OR T J',  # J=~A+~B+~C
    'AND D J', # J=(~A+~B+~C)D
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

RUN_INS = [
    'NOT E T', # T=~E
    'NOT T T', # T=E
    'OR H T',  # T=E+H
    'AND T J', # (~A+~B+~C)D(E+H)
]

cmd_str = NL.join(INS + RUN_INS) + NL + 'RUN' + NL
cmds = list(map(ord, cmd_str))

comp = Intcode(inp, cmds)
o = ''
while not comp.done:
    c = comp.run_until_output()
    if c > 255:
        p2 = c
    else:
        o += chr(c)
print(o)

print(f'Part 2: {p2}')
