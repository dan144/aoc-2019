#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('15', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

N = 1
S = 2
W = 3
E = 4

WALL = 0
OPEN = 1
OXY = 2
DROID = 3

DX = {W: -1, E: 1}
DY = {N: -1, S: 1}
reverse = {N: S, S: N, W: E, E: W}

points = {}
o_x, o_y = 21, 21 # offset value to make minimum x, y values 0, 0

x, y = o_x, o_y
moves_left = {(x, y): [N, S, E, W]}
moves = []
comp = Intcode(inp)
while moves_left:
    moves_here = moves_left[x, y]
    if not moves_here:
        if not moves:
            break # when there's no moves forward and no moves back, it's done
        move = reverse[moves.pop()]
        x += DX.get(move, 0)
        y += DY.get(move, 0)
        comp.inputs.append(move)
        res = comp.run_until_output()
        assert res  # moving backward should always work
        continue

    move = moves_here.pop()
    comp.inputs.append(move)
    res = comp.run_until_output()

    m_x = x + DX.get(move, 0)
    m_y = y + DY.get(move, 0)
    points[m_x, m_y] = res
    if res:
        if res == 2:
            oxy = (m_x, m_y)
        x, y = m_x, m_y
        moves.append(move)
        if (x, y) not in moves_left:
            moves_left[x, y] = [N, E, S, W]

mx_x = max({x for x, _ in points.keys()}) + 1
mx_y = max({y for _, y in points.keys()}) + 1

board = []
for y in range(mx_y):
    board.append([0] * mx_x)

for point, spot in points.items():
    board[point[1]][point[0]] = spot
board[o_y][o_x] = DROID

def pretty(s):
    if s == WALL:
        return '#'
    if s == OPEN:
        return ' '
    if s == OXY:
        return '!'
    return 'D'

for line in board:
    print(''.join(map(pretty, line)))

def map_adj(dist, locs):
    n_locs = set()
    for y, x in locs:
        for direction in {N, S, E, W}:
            n_x = x + DX.get(direction, 0)
            n_y = y + DY.get(direction, 0)
            if board[n_y][n_x] != WALL:
                if dist[n_y][n_x] is None:
                    dist[n_y][n_x] = dist[y][x] + 1
                    n_locs.add((n_y, n_x))
                elif dist[y][x] + 1 < dist[n_y][n_x]:
                    dist[n_y][n_x] = dist[y][x] + 1
                    n_locs.add((n_y, n_x))
    return n_locs

dist = []
for y in range(mx_y):
    dist.append([None] * mx_x)
dist[o_y][o_x] = 0
locs = {(o_y, o_x)}
while dist[oxy[1]][oxy[0]] is None:
    locs = map_adj(dist, locs)

p1 = dist[oxy[1]][oxy[0]]
print(f'Part 1: {p1}')

dist = []
for y in range(mx_y):
    dist.append([None] * mx_x)
dist[oxy[1]][oxy[0]] = 0
locs = {(oxy[1], oxy[0])}
while locs:
    locs = map_adj(dist, locs)

for line in dist:
    p2 = max(set(filter(lambda x: x is not None, line)) | {p2})


print(f'Part 2: {p2}')
