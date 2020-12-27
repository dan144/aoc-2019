#!/usr/bin/env python3

import math

from copy import copy, deepcopy

inp = []
with open('14', 'r') as f:
    for line in f:
        inp.append(line.strip())

p1 = 0
p2 = 0

convs = {}
for line in inp:
    i, o = line.split(' => ')
    oq, o = o.split(' ')
    oq = int(oq)
    convs[o] = (oq, {})
    for x in i.split(', '):
        q, n = x.split(' ')
        convs[o][1][n]  = int(q)


def all_needs(reqs):
    nest = set(reqs.keys())
    while True:
        n_nest = copy(nest)
        for l in nest:
            if l == 'ORE':
                continue
            n_nest.update(convs[l][1].keys())
        if nest == n_nest:
            break
        nest = n_nest
    return nest


def make_x(x):
    reqs = deepcopy(convs['FUEL'][1])
    for k in reqs.keys():
        reqs[k] *= x
    i = 0
    while list(reqs.keys()) != ['ORE']:
        k = list(reqs.keys())[i]
        if k == 'ORE':
            i = (i + 1) % len(list(reqs.keys()))
            continue
        r = reqs.pop(k)
        q, n = convs[k]
        if k in all_needs(reqs):
            reqs[k] = r
            continue
        for need, n_q in n.items():
            quan = math.ceil(r / q) * n_q
            if need in reqs:
                reqs[need] += quan
            else:
                reqs[need] = quan
    return reqs

reqs = make_x(1)
p1 = reqs['ORE']
print(f'Part 1: {p1}')

def search(n):
    marg = 1
    up = True
    while n * marg >= .1:
        while True:
            reqs = make_x(n)
            if up:
                if reqs['ORE'] > TRL:
                    break
            else:
                if reqs['ORE'] <= TRL:
                    break
            n = int(n * (1 + marg * (1 if up else -1)))
        up = not up
        marg /= 10
    return n


TRL = 1000000000000
p2 = search(TRL)
print(f'Part 2: {p2}')
