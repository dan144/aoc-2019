#!/usr/bin/env python3

from intcode import Intcode
import string

inp = []
with open('20', 'r') as f:
    #inp = list(map(int, f.readline().split(',')))
    for line in f:
        inp.append(line)

p1 = 0
p2 = 0

N = 1
S = 2
W = 3
E = 4
DX = {W: -1, E: 1}
DY = {N: -1, S: 1}

def map_adj(dist, locs):
    n_locs = []
    for y, x in locs:
        for direction in {N, S, E, W}:
            n_x = x + DX.get(direction, 0)
            n_y = y + DY.get(direction, 0)
            space = board[n_y][n_x]
            if space == '.':
                if dist[n_y][n_x] is None:
                    dist[n_y][n_x] = dist[y][x] + 1
                    n_locs.append((n_y, n_x))
                elif dist[y][x] + 1 < dist[n_y][n_x]:
                    dist[n_y][n_x] = dist[y][x] + 1
                    n_locs.append((n_y, n_x))
            elif space in string.ascii_uppercase:
                nn_x = n_x + DX.get(direction, 0)
                nn_y = n_y + DY.get(direction, 0)
                portal = ''.join(sorted(board[nn_y][nn_x] + board[n_y][n_x]))
                if portal not in {'AA', 'ZZ'}:
                    locs = portals[portal]
                    n_y, n_x = locs[1] if (y, x) == locs[0] else locs[0]
                    if dist[n_y][n_x] is None:
                        dist[n_y][n_x] = dist[y][x] + 1
                        n_locs.append((n_y, n_x))
                    elif dist[y][x] + 1 < dist[n_y][n_x]:
                        dist[n_y][n_x] = dist[y][x] + 1
                        n_locs.append((n_y, n_x))
    return n_locs

def comp_dist(f, t):
    n_dist = []
    for y in range(size[0]):
        n_dist.append([None] * size[1])
    locs = [f]
    n_dist[f[0]][f[1]] = 0

    while locs:
        locs = map_adj(n_dist, locs)
    #for line in n_dist:
        #print(''.join(('x' if x is None else str(x) for x in line)))
    return n_dist[t[0]][t[1]]

board = []
for line in inp:
    board.append(list(line[:-1]))

portals = {}
for y in range(len(board)-1):
    for x in range(len(board[y])-1):
        if board[y][x] == 'A':
            if board[y+1][x] =='A':
                start = y+2, x
            elif board[y][x+1] == 'A':
                start = y, x+2
        elif board[y][x] == 'Z':
            if board[y+1][x] =='Z':
                end = y-1, x
            elif board[y][x+1] == 'Z':
                end = y, x+2
        if board[y][x] in string.ascii_uppercase:
            for direction in {S, E}:
                n_x = x + DX.get(direction, 0)
                n_y = y + DY.get(direction, 0)
                if n_y < 0 or n_y >= len(board) or n_x < 0 or n_x >= len(board[y]):
                    continue
                if board[n_y][n_x] in string.ascii_uppercase:
                    portal = ''.join(sorted(board[y][x] + board[n_y][n_x]))
                    nn_x = n_x + DX.get(direction, 0)
                    nn_y = n_y + DY.get(direction, 0)
                    if nn_y < 0 or nn_y >= len(board):
                        nn_y -= 3*DY.get(direction, 0)
                    elif nn_x < 0 or nn_x >= len(board[y]):
                        nn_x -= 3*DX.get(direction, 0)
                    elif board[nn_y][nn_x] != '.':
                        nn_y -= 3*DY.get(direction, 0)
                        nn_x -= 3*DX.get(direction, 0)
                    print(portal)
                    if portal in portals:
                        portals[portal].append((nn_y, nn_x))
                    else:
                        portals[portal] = [(nn_y, nn_x)]
                    break
size = y+1, x+1
#y, x = start
#board[y][x] = 'S'
#y, x = end
#board[y][x] = 'E'
#for locs in portals.values():
#    print(locs)
#    for loc in locs:
#        y, x = loc
#        board[y][x] = '!'
#for line in board:
#    print(''.join(line))
p1 = comp_dist(start, end)

print(f'Part 1: {p1}')



print(f'Part 2: {p2}')
