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


def display(points):
    mn_x = min({x for x, _ in points.keys()})
    mn_y = min({y for _, y in points.keys()})
    mx_x = max({x for x, _ in points.keys()})
    mx_y = max({y for _, y in points.keys()})

    m_x = mx_x - mn_x
    m_y = mx_y - mn_y

    o = []
    for i in range(m_x+1):
        o.append(['.'] * (m_y+1))

    for point, color in points.items():
        if color == WHITE:
            x = mx_x - point[0]
            y = point[1] - mx_y - 1
            o[x][y] = '#'

    for line in o:
        print(''.join(line))


def get_points(c):
    direction = UP
    points = {}
    x, y = 0, 0
    comp = Intcode(inp, [c])
    while not comp.done:
        color, turn = comp.run_until_n_output(2)
        points[(x, y)] = color
        direction = (direction + (1 if turn == RIGHT else -1)) % 4
        x += dx.get(direction, 0)
        y += dy.get(direction, 0)

        n_color = points.get((x, y), BLACK)
        comp.inputs.append(n_color)
    return points


points = get_points(BLACK)
p1 = len(points.keys())
print(f'Part 1: {p1}')

points = get_points(WHITE)
print('Part 2:')
display(points)
