#!/usr/bin/env python3

from copy import copy

from intcode import Intcode

inp = []
with open('25', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0

NL = '\n'
DX = {'east': 1, 'west': -1}
DY = {'north': -1, 'south': 1}

def make_cmd(s):
    return list(map(ord, s))

comp = Intcode(inp)

dirs = []
items = set()
cmd = ''
cmds = []
d = {}
x, y = 0, 0

while not comp.done:
    lines = 0
    chs = ''
    cmd = ''.join(cmd)
    if cmd in {'north', 'south', 'east', 'west'}:
        x += DX.get(cmd, 0)
        y += DY.get(cmd, 0)
        dirs = []
        items = set()
    while True:
        chs = ''
        c = ''
        while c != NL:
            c = chr(comp.run_until_output())
            chs += c

        lines += 1
        chs = chs.strip()

        print(chs, end='')
        if chs.startswith('- '):
            chs = chs.split(' ', maxsplit=1)[1]
            if chs in {'north', 'south', 'east', 'west'}:
                dirs.append(chs)
            else:
                items.add(chs)

        if lines == 50:
            break
        if chs == 'Command?':
            print(' ', end='')
            break
        print()

    if (x, y) not in d:
        d[x, y] = copy(dirs)
    cmd = input()
    comp.inputs.extend(make_cmd(cmd + NL))


print(f'Part 1: {p1}')
