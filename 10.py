#!/usr/bin/env python3

from collections import OrderedDict

board = []
with open('10', 'r') as f:
    for line in f:
        board.append(list(line.strip()))

p1 = 0
p2 = 0

n_y = len(board)
n_x = len(board[0])
asteroids = []

for y in range(n_y):
    row = board[y]
    for x in range(n_x):
        if row[x] != '.':
            asteroids.append((x,y))

can_see = {}
for a1 in asteroids:
    x1, y1 = a1
    angles = set()
    for a2 in asteroids:
        if a1 == a2:
            continue

        x2, y2 = a2
        dy = y2 - y1
        dx = x2 - x1
        m = (dx*dx + dy*dy)**.5
        dy /= m
        dx /= m
        #if dx and dy:
        angle = ((round(dy, 8), round(dx, 8)))
        #elif dy:
        #    angle = 'inf' if dy > 0 else 'ninf'
        #else:
        #    angle = 'r' if dx > 0 else 'l'
        angles.add(angle)
    can_see[a1] = len(angles)

for k, v in can_see.items():
    if v > p1:
        p1 = v
        base = k

print(f'Part 1: {p1}')
print(base)
board[base[1]][base[0]] = 'X'

x1, y1 = base
for a2 in asteroids:
    if a2 == base:
        continue

    x2, y2 = a2
    dy = y2 - y1
    dx = x2 - x1
    m = (dx*dx + dy*dy)**.5
    dy /= m
    dx /= m
    angle = ((round(dy, 8), round(dx, 8)))
    angles.add(angle)

q = [[], [], [], []]
has = [False] * 4
cardinals = {
    0: (-1.0, 0.0),
    1: (0.0, 1.0),
    2: (1.0, 0.0),
    3: (0.0, -1.0),
}
for angle in angles:
    if angle == cardinals[0]:
        has[0] = True
    elif angle[0] < 0 and angle[1] > 0:
        q[0].append(angle)
    elif angle == cardinals[1]:
        has[1] = True
    elif angle[0] > 0 and angle[1] > 0:
        q[1].append(angle)
    elif angle == cardinals[2]:
        has[2] = True
    elif angle[0] > 0 and angle[1] < 0:
        q[2].append(angle)
    elif angle == cardinals[3]:
        has[3] = True
    elif angle[0] < 0 and angle[1] < 0:
        q[3].append(angle)
    else:
        print(angle)


at_angle = OrderedDict()
for i in range(4):
    if has[i]:
        at_angle[cardinals[i]] = []
    q[i].sort(key = lambda x: x[1]/x[0] * (-1 if i in {0, 1, 2, 3} else 1))
    for dy, dx in q[i]:
        at_angle[(dy, dx)] = []

for asteroid in asteroids:
    if asteroid == base:
        continue
    x, y = asteroid
    dx = x - base[0]
    dy = y - base[1]
    m = (dx*dx + dy*dy)**.5
    dy /= m
    dx /= m
    angle = ((round(dy, 8), round(dx, 8)))
    at_angle[angle].append((y, x, m))

sorted_angles = OrderedDict()
for angle, asteroids in at_angle.items():
    asteroids.sort(key = lambda x: x[2])
    sorted_angles[angle] = asteroids

destroyed = 0
while destroyed < 200:
    for angle in sorted_angles.keys():
        if sorted_angles[angle]:
            des = sorted_angles[angle].pop(0)
            destroyed += 1
            board[des[0]][des[1]] = str(destroyed % 9)
        if destroyed == 200:
            print(des)
            p2 = 100*des[1] + des[0]
            break

print(f'Part 2: {p2}')
