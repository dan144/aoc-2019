#!/usr/bin/env python3

inp = []
with open('3', 'r') as f:
    inp1 = f.readline().split(',')
    inp2 = f.readline().split(',')

p1 = 0
p2 = 0

steps = {}


def parse(dirs):
    global steps
    x, y = 0, 0
    s = 0
    wire = set()
    for move in dirs:
        direction = move[0]
        length = int(move[1:])
        for i in range(length):
            s += 1
            x += {'R': 1, 'L': -1}.get(direction, 0)
            y += {'U': 1, 'D': -1}.get(direction, 0)
            wire.add((x, y))
            steps[(x, y)] = s + steps.get((x,y), 0)
    return wire


w1 = parse(inp1)
w2 = parse(inp2)

for point in w1 & w2:
    md = abs(point[0]) + abs(point[1])
    p1 = md if p1 == 0 or md < p1 else p1
    p2 = steps[point] if p2 == 0 or steps[point] < p2 else p2

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
