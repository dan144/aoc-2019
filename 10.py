#!/usr/bin/env python3

from collections import OrderedDict

board = []
with open('10', 'r') as f:
    for line in f:
        board.append(list(line.strip()))

p1 = 0
p2 = 0


def dist(a1, a2):
    dx = a1[0] - a2[0]
    dy = a1[1] - a2[1]
    m = (dx*dx + dy*dy)**.5
    dy /= m
    dx /= m
    return round(dx, 8), round(dy, 8), m


n_y = len(board)
n_x = len(board[0])
asteroids = []

for y in range(n_y):
    row = board[y]
    for x in range(n_x):
        if row[x] != '.':
            asteroids.append((x,y))

for a1 in asteroids:
    angles = set()
    for a2 in asteroids:
        if a1 == a2:
            continue
        dx, dy, _ = dist(a1, a2)
        angles.add((dx, dy))
    if len(angles) > p1:
        p1 = len(angles)
        base = a1

print(f'Part 1: {p1} at {base}')

for asteroid in asteroids:
    if asteroid == base:
        continue
    dx, dy, m = dist(asteroid, base)
    angles.add(((round(dx, 8), round(dy, 8))))

q = [[], [], [], []]
has = [False] * 4
cardinals = {
    0: (0.0, -1.0),
    1: (1.0, 0.0),
    2: (0.0, 1.0),
    3: (-1.0, 0.0),
}

for angle in angles:
    if angle == cardinals[0]:
        has[0] = True
    elif angle[1] < 0 and angle[0] > 0:
        q[0].append(angle)
    elif angle == cardinals[1]:
        has[1] = True
    elif angle[1] > 0 and angle[0] > 0:
        q[1].append(angle)
    elif angle == cardinals[2]:
        has[2] = True
    elif angle[1] > 0 and angle[0] < 0:
        q[2].append(angle)
    elif angle == cardinals[3]:
        has[3] = True
    elif angle[1] < 0 and angle[0] < 0:
        q[3].append(angle)

at_angle = OrderedDict()
for i in range(4):
    if has[i]:
        at_angle[cardinals[i]] = []
    q[i].sort(key = lambda x: x[0]/x[1], reverse=True)
    for angle in q[i]:
        at_angle[angle] = []

for asteroid in asteroids:
    if asteroid == base:
        continue
    dx, dy, m = dist(asteroid, base)
    at_angle[(dx, dy)].append(asteroid + (m,))

for angle in at_angle.keys():
    at_angle[angle].sort(key = lambda x: x[2])

destroyed = 0
while destroyed < 200:
    for angle in at_angle.keys():
        if at_angle[angle]:
            des = at_angle[angle].pop(0)
            destroyed += 1
        if destroyed == 200:
            p2 = 100*des[0] + des[1]
            break

print(f'Part 2: {p2} at ({des[0]}, {des[1]})')
