#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('11', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

BLACK = 0
WHITE = 1
LEFT = 0
RIGHT = 1
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

dx = {UP: 1, DOWN: -1}
dy = {LEFT: -1, RIGHT: 1}

direction = UP
board = {}
x, y = 0, 0
comp = Intcode(inp, [BLACK])
while not comp.done:
    color = comp.run_until_output()
    board[(x, y)] = color
    turn = comp.run_until_output()
    direction = (direction + (1 if turn == RIGHT else -1)) % 4
    x += dx.get(direction, 0)
    y += dy.get(direction, 0)

    n_color = board.get((x, y), BLACK)
    comp.inputs.append(n_color)

p1 = len(board.keys())

print(f'Part 1: {p1}')

direction = UP
board = {}
x, y = 0, 0
comp = Intcode(inp, [WHITE])
while not comp.done:
    color = comp.run_until_output()
    board[(x, y)] = color
    turn = comp.run_until_output()
    direction = (direction + (1 if turn == RIGHT else -1)) % 4
    x += dx.get(direction, 0)
    y += dy.get(direction, 0)

    n_color = board.get((x, y), BLACK)
    comp.inputs.append(n_color)

mn_x = min({x for x, _ in board.keys()})
mn_y = min({y for _, y in board.keys()})
mx_x = max({x for x, _ in board.keys()})
mx_y = max({y for _, y in board.keys()})
print(mn_x, mx_x, mn_y, mx_y)

m_x = mx_x - mn_x
m_y = mx_y - mn_y

o = []
for i in range(m_x+1):
    o.append(['#'] * (m_y+1))

print(m_x, m_y)

for point, color in board.items():
    if color == WHITE:
        o[point[0]*-1][point[1]*-1] = '.'

for line in o:
    print(''.join(line))
