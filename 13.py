#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('13', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

p = set()
comp = Intcode(inp)
xs = set()
ys = set()
comp.reg[2122] = 1
while not comp.done:
    x = comp.run_until_output()
    y = comp.run_until_output()
    t = comp.run_until_output()
    xs.add(x)
    ys.add(y)
    p.add((x, y, t))
    if t == 2:
        p1 += 1

print(f'Part 1: {p1}')

mn_x = min(xs)
mx_x = max(xs)
mn_y = min(ys)
mx_y = max(ys)
board = []
for y in range(mx_y+1):
    board.append([0] * (mx_x+1))
for x, y, t in p:
    board[y][x] = t

def disp():
    for line in board:
        print(''.join(map(str, line)))

N = 0
L = -1
R = 1
comp = Intcode(inp)
comp.reg[0] = 2
comp.reg[2120] = 3
while not comp.done:
    comp.inputs.append(0)
    x = comp.run_until_output()
    y = comp.run_until_output()
    z = comp.run_until_output()
p2 = z

print(f'Part 2: {p2}')
