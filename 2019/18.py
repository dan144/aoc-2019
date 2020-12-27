#!/usr/bin/env python3

from copy import copy, deepcopy
import string
import threading

inp = []
with open('18', 'r') as f:
    #inp = list(map(int, f.readline().split(',')))
    for line in f:
        inp.append(line)

N = 1
S = 2
W = 3
E = 4
DX = {W: -1, E: 1}
DY = {N: -1, S: 1}

p1 = 0
p2 = 0

board = []
doors = set()
keys = {}
entrances = []
for y in range(len(inp)):
    line = list(inp[y])
    board.append([])
    for x in range(len(line)):
        char = line[x]
        if char == '@':
            entrances.append((y, x))
        elif char in string.ascii_lowercase:
            keys[char] = (y, x)
        elif char in string.ascii_uppercase:
            doors.add((y, x))
        board[-1].append(char)
size = y, x

def map_adj(dist, locs):
    n_locs = []
    for y, x, block in locs:
        for direction in {N, S, E, W}:
            n_x = x + DX.get(direction, 0)
            n_y = y + DY.get(direction, 0)
            space = board[n_y][n_x]
            if space in '.@' or space in string.ascii_lowercase:
                if dist[n_y][n_x] is None:
                    dist[n_y][n_x] = dist[y][x] + 1
                    n_locs.append((n_y, n_x, block))
                elif dist[y][x] + 1 < dist[n_y][n_x]:
                    dist[n_y][n_x] = dist[y][x] + 1
                    n_locs.append((n_y, n_x, block))
            elif space in string.ascii_uppercase:
                if dist[n_y][n_x] is None:
                    dist[n_y][n_x] = dist[y][x] + 1
                    n_locs.append((n_y, n_x, block + [space.lower()]))
                elif dist[y][x] + 1 < dist[n_y][n_x]:
                    dist[n_y][n_x] = dist[y][x] + 1
                    n_locs.append((n_y, n_x, block + [space.lower()]))
    return n_locs

def comp_dist(fs, t=None):
    n_dist = []
    for y in range(size[0]):
        n_dist.append([None] * size[1])
    locs = []
    for f in fs:
        locs.append(f + ([],))
        n_dist[f[0]][f[1]] = 0
    n_blocks = {}

    while locs:
        locs = map_adj(n_dist, locs)
        if t is None:
            for l_y, l_x, b in locs:
                if board[l_y][l_x] in string.ascii_lowercase:
                    key = board[l_y][l_x]
                    n_blocks[key] = b
        if t and n_dist[t[0]][t[1]] is not None:
            return n_dist[t[0]][t[1]]
    return n_dist, n_blocks

def comp_dists():
    n_dists = {}
    for key in keys.keys():
        k_y, k_x = keys[key]
        n_dists['@', key] = dist[k_y][k_x]
        k_dist, _ = comp_dist([keys[key]])
        for k, loc in keys.items():
            if k == key:
                continue
            if k_dist[loc[0]][loc[1]] is not None:
                n_dists[key, k] = k_dist[loc[0]][loc[1]]
    return n_dists

def compute_path(key_pattern):
    r_loc = deepcopy(entrances)
    d = 0
    for i in range(len(key_pattern)):
        key = key_pattern[i]
        owner = owners[key]
        owner_loc = r_loc[owner]
        d += comp_dist([owner_loc], keys[key])
        r_loc[owners[key]] = keys[key]
    return d

paths = {}
starts = set()
for key in keys.keys():
    can_add = set(keys.keys())
    can_add.remove(key)
    paths[key] = can_add

owners = {}
owns = [[], [], [], []]
for i in range(len(entrances)):
    dist, blocks = comp_dist([entrances[i]])
    for key, loc in keys.items():
        k_y, k_x = loc
        if dist[k_y][k_x]:
            owners[key] = i
            owns[i].append(key)

dist, blocks = comp_dist(entrances)
for key, bl in blocks.items():
    if not bl:
        starts.add(key)
    for b_key in bl:
        for p_key, p in paths.items():
            if b_key == p_key:
                continue
            if key in p:
                p.remove(key)

dists = comp_dists()

def compute_all_paths(pattern):
    global p1
    if p1 and compute_path(pattern) >= p1:
        return

    if len(pattern) == len(keys):
        d = compute_path(pattern)
        if p1 == 0 or d < p1:
            with l:
                if p1 == 0 or d < p1:
                    print(pattern, d)
                    p1 = d
        return

    try_keys = {k for k in keys if k not in pattern}
    try_keys = sorted(try_keys, key=lambda x: dists.get((pattern[-1], x), dists['@', x]))
    for key in try_keys:
        #if key in blocks:
        #    if not set(blocks[key]).issubset(pattern):
        #    continue
        compute_all_paths(pattern + [key])

threads = []
l = threading.Lock()


#for start in starts:
#    t = threading.Thread(target=compute_all_paths, args=([start],))
#    t.start()
#    threads.append(t)
#
#for t in threads:
#    t.join()

print(f'Part 1: {p1}')

for i in range(len(owns)):
    use = set(keys) & set(owns[i])
    print(keys, use)
    for starter in use:
        compute_all_paths([starter])
print(f'Part 2: {p2}')
