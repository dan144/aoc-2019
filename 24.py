#!/usr/bin/env python3

from copy import deepcopy

inp = []
with open('24', 'r') as f:
    for line in f:
        inp.append(line)
board = []
for line in inp:
    board.append(list(line.strip()))

p1 = 0
p2 = 0

BUG = '#'
SPACE = '.'

def run(old):
    n = []
    for i in range(len(old)):
        n.append([0] * len(old[i]))

    for y in range(len(old)):
        for x in range(len(old[y])):
            count = 0
            for dy, dx in {(-1, 0), (0, -1), (0, 1), (1, 0)}:
                if x + dx < 0 or x + dx >= len(old[y]) or y + dy < 0 or y + dy >= len(old):
                    continue
                count += 1 if old[y+dy][x+dx] == BUG else 0
            if old[y][x] == BUG and count != 1:
                n[y][x] = SPACE
            elif old[y][x] == SPACE and count in {1, 2}:
                n[y][x] = BUG
            else:
                n[y][x] = old[y][x]
    return n

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

disp(board)
scores = set()
s = score(board)
scores.add(s)
while True:
    board = run(board)
    p1 = score(board)
    if p1 in scores:
        break
    scores.add(p1)
    disp(board)

disp(board)
#not 528328671
print(f'Part 1: {p1}')



print(f'Part 2: {p2}')
