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
OUTER = 0
INNER = 1

def add_level():
    r = []
    for y in range(size[0]):
        r.append([None] * size[1])
    return r

def map_adj(dist, locs, recurse):
    n_locs = []
    for y, x, level in locs:
        for direction in {N, S, E, W}:
            n_x = x + DX.get(direction, 0)
            n_y = y + DY.get(direction, 0)
            space = board[n_y][n_x]
            if space == '.':
                if dist[level][n_y][n_x] is None or \
                   dist[level][n_y][n_x] + 1 < dist[level][y][x]:
                   #dist[level][n_y][n_x] > dist[level][y][x] + 1 or \
                    dist[level][n_y][n_x] = dist[level][y][x] + 1
                    n_locs.append((n_y, n_x, level))
            elif space in string.ascii_uppercase:
                nn_x = n_x + DX.get(direction, 0)
                nn_y = n_y + DY.get(direction, 0)
                portal = (board[nn_y][nn_x] + board[n_y][n_x])[::-1 if direction in {S,E} else 1]
                if portal not in {'AA', 'ZZ'}:
                    p_locs = portals[portal]
                    if (y, x) == p_locs[OUTER]:
                        if level == 0 and recurse:
                            continue
                        n_y, n_x = p_locs[INNER]
                        n_l = level - 1 if recurse else level
                    else:
                        n_y, n_x = p_locs[OUTER]
                        n_l = level + 1 if recurse else level
                    if n_l > 50: # max depth, for speed
                        continue

                    if n_l == len(dist):
                        dist.append(add_level())
                    if dist[n_l][n_y][n_x] is None or \
                       dist[n_l][n_y][n_x] + 1 < dist[level][y][x]:
                       #dist[n_l][n_y][n_x] > dist[level][y][x] + 1 or \ # shorter path found via cycle
                        dist[n_l][n_y][n_x] = dist[level][y][x] + 1
                        n_locs.append((n_y, n_x, n_l))
    return n_locs

def comp_dist(f, t, recurse):
    dist = [add_level()]
    dist[0][f[0]][f[1]] = 0
    locs = [(f[0], f[1], 0)]

    while not dist[0][t[0]][t[1]] and locs:
        locs = map_adj(dist, locs, recurse)

    #for level in range(len(dist)):
    #    y = -1
    #    for line in dist[level]:
    #        y += 1
    #        print(''.join((board[y][x] if line[x] is None else str(line[x]%10) for x in range(len(line)))))
    #    input()
    return dist[0][t[0]][t[1]]

board = []
for line in inp:
    board.append(list(line[:-1]))

portals = {}
for y in range(len(board)-1):
    for x in range(len(board[y])-1):
        if board[y][x] == 'A':
            if board[y+1][x] =='A':
                if y+2 < len(board):
                    start = y+2, x
                else:
                    start = y-1, x
            elif board[y][x+1] == 'A':
                if x+2 < len(board[y]):
                    start = y, x+2
                else:
                    start = y, x-1
        elif board[y][x] == 'Z':
            if board[y+1][x] =='Z':
                if y+2 < len(board):
                    end = y+2, x
                else:
                    end = y-1, x
            elif board[y][x+1] == 'Z':
                if x+2 < len(board[y]):
                    end = y, x+2
                else:
                    end = y, x-1
        if board[y][x] in string.ascii_uppercase:
            if board[y+1][x] in string.ascii_uppercase:
                n_y, n_x = y+1, x
                outer = y in {0, len(board) - 2}
                l_x = x
                l_y = y + 2 if y < 2 or board[y-2][x] != '.' else y - 1
            elif board[y][x+1] in string.ascii_uppercase:
                n_y, n_x = y, x+1
                l_y = y
                l_x = x + 2 if x < 2 or board[y][x-2] != '.' else x - 1
                outer = x in {0, len(board[y]) - 2}
            else:
                continue # not portal

            portal = board[y][x] + board[n_y][n_x]
            if portal in {'AA', 'ZZ'}:
                continue
            if portal not in portals:
                portals[portal] = [0, 0]
            if outer:
                portals[portal][OUTER] = (l_y, l_x)
            else:
                portals[portal][INNER] = (l_y, l_x)

size = y+1, x+1
#y, x = start
#p_board[y][x] = 'S'
#y, x = end
#p_board[y][x] = 'E'
#for portal, locs in portals.items():
#    print(portal, locs)
#    y, x = locs[0]
#    p_board[y][x] = 'O'
#    y, x = locs[1]
#    p_board[y][x] = 'I'
#for line in board:
#    print(''.join(line))
#input()

p1 = comp_dist(start, end, False)
print(f'Part 1: {p1}')

p2 = comp_dist(start, end, True)
print(f'Part 2: {p2}')
