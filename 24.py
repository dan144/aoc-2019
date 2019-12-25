#!/usr/bin/env python3

from copy import deepcopy

inp = []
with open('24', 'r') as f:
    for line in f:
        inp.append(line)

p1 = 0
p2 = 0

BUG = '#'
SPACE = '.'

def b_count(b):
    c = 0
    for line in b:
        for char in line:
            if char == BUG:
                c += 1
    return c

def count_all(bs):
    c = 0
    for b in bs:
        c += b_count(b)
    return c

def run(olds, recurse):
    if recurse:
        a = []
        for l in range(sy):
            a.append(['.'] * sx)
        olds.insert(0, deepcopy(a))
        olds.append(deepcopy(a))

    ns = []
    for l in range(len(olds)):
        ns.append([])
        for i in range(sy):
            ns[-1].append(['.'] * sx)


    for l in range(len(ns)):
        for y in range(sy):
            for x in range(sx):
                check = {(0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0)}

                if recurse:
                    if y == my and x == mx:
                        continue
                    if y == my:
                        if x == mx + 1:
                            check.remove((0, 0, -1))
                            check.update({(1, ny, sx-1) for ny in range(sy)})
                        elif x == mx - 1:
                            check.remove((0, 0, 1))
                            check.update({(1, ny, 0) for ny in range(sy)})
                    elif x == mx:
                        if y == my + 1:
                            check.remove((0, -1, 0))
                            check.update({(1, sy-1, nx) for nx in range(sx)})
                        elif y == my - 1:
                            check.remove((0, 1, 0))
                            check.update({(1, 0, nx) for nx in range(sx)})

                    if y == 0:
                        check.add((-1, my - 1, mx))
                    elif y == sy - 1:
                        check.add((-1, my + 1, mx))

                    if x == 0:
                        check.add((-1, my, mx - 1))
                    elif x == sx - 1:
                        check.add((-1, my, mx + 1))

                count = 0
                for dl, dy, dx in check:
                    if l + dl < 0 or l + dl >= len(olds):
                        continue
                    if dl == 0:
                        if x + dx < 0 or x + dx >= sx or y + dy < 0 or y + dy >= sy:
                            continue

                    if dl == 0:
                        count += 1 if olds[l+dl][y+dy][x+dx] == BUG else 0
                    else:
                        count += 1 if olds[l+dl][dy][dx] == BUG else 0
                if olds[l][y][x] == BUG and count != 1:
                    ns[l][y][x] = SPACE
                elif olds[l][y][x] == SPACE and count in {1, 2}:
                    ns[l][y][x] = BUG
                else:
                    ns[l][y][x] = olds[l][y][x]

    if recurse:
        if b_count(ns[0]) == 0:
            ns = ns[1:]
        if b_count(ns[-1]) == 0:
            ns = ns[:-1]
    return ns

def score(board):
    s = 0
    p = 1
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == BUG:
                s += p
            p *= 2
    return s

def disp(board):
    print()
    for line in board:
        print(''.join(line))

def disp_all(boards):
    for board in boards:
        print()
        disp(board)
    print('---')

board = []
for line in inp:
    board.append(list(line.strip()))
boards = [deepcopy(board)]

sy, sx = len(board), len(board[0])
my = sy // 2
mx = sx // 2

scores = set()
s = score(boards[0])
scores.add(s)
while True:
    boards = run(boards, False)
    p1 = score(boards[0])
    if p1 in scores:
        break
    scores.add(p1)
print(f'Part 1: {p1}')

boards = [board]
for mn in range(200):
    boards = run(boards, True)

p2 = count_all(boards)
print(f'Part 2: {p2}')
