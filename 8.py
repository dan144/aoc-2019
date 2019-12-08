#!/usr/bin/env python3

import re

from itertools import permutations

from intcode import Intcode

inp = []
with open('8', 'r') as f:
    inp = f.readline().strip()

W = 25
H = 6

chunk_size = int(W * H)
chunk_n = int(len(inp) / chunk_size)
mn = None
for chunk_i in range(chunk_n):
    chunk_s = chunk_i * chunk_size
    chunk_e = (chunk_i+1) * chunk_size
    chunk = inp[chunk_s:chunk_e]
    z = len(re.findall(r'0', chunk))
    if mn is None or z < mn:
        mn = z
        p1 = len(re.findall(r'1', chunk)) * len(re.findall(r'2', chunk))

print(f'Part 1: {p1}')

BLACK = '0'
WHITE = '1'
TRANSPARENT = '2'

board = []
for _ in range(H):
    board.append([TRANSPARENT] * W)
for i in range(len(inp)):
    loc = i % chunk_size
    x = int(loc / W)
    y = int(loc % W)
    if board[x][y] == TRANSPARENT:
        board[x][y] = inp[i]

print('Part 2:')
for line in board:
    o = ''
    for c in line:
        o += '*' if c == WHITE else ' '
    print(o)
