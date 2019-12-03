#!/usr/bin/python3.6

inp = []
with open('3', 'r') as f:
    for line in f:
        inp.append(line.split(','))

p1 = 0
p2 = 0

wr = 0
steps = {}
for wire in inp:
    x, y = 0, 0
    s = 0
    t = set()
    for d in wire:
        dr = d[0]
        ln = int(d[1:])
        for i in range(ln):
            s += 1
            if dr == 'R':
                x += 1
            elif dr == 'L':
                x -= 1
            elif dr == 'U':
                y += 1
            else:
                y -= 1
            t.add((x, y))
            steps[(x, y)] = s + steps.get((x,y), 0)
    if wr == 0:
        wr = 1
        w1 = t
    else:
        w2 = t
        break

ins = []
for point in w1:
    if point in w2:
        ins.append(point)
        p2 = steps[point] if p2 == 0 or steps[point] < p2 else p2

md = []
for p in ins:
    x, y = p
    md.append(abs(x) + abs(y))

p1 = min(md)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
