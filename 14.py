#!/usr/bin/env python3

import math

from copy import copy, deepcopy

inp = []
with open('14', 'r') as f:
    for line in f:
        inp.append(line.strip())

p1 = 0
p2 = 0

def make_convs():
    convs = {}
    for line in inp:
        i, o = line.split(' => ')
        oq, o = o.split(' ')
        oq = int(oq)
        convs[o] = (oq, {})
        for x in i.split(', '):
            q, n = x.split(' ')
            convs[o][1][n]  = int(q)
    return convs

def all_needs(convs, reqs):
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
    convs = deepcopy(o_conv)
    reqs = convs['FUEL'][1]
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
        if k in all_needs(convs, reqs):
            reqs[k] = r
            continue
        for need, n_q in n.items():
            if False:
                quan = r / q * n_q
            else:
                quan = math.ceil(r / q) * n_q
            if need in reqs:
                reqs[need] += quan
            else:
                reqs[need] = quan
    return reqs

o_conv = make_convs()
reqs = make_x(1)
p1 = reqs['ORE']
print(f'Part 1: {p1}')

TRL = 1000000000000
p2 = TRL // p1
while True:
    reqs = make_x(p2)
    if reqs['ORE'] > TRL:
        p2 -= 1
        break
    p2 = int(p2 * 1.0006)
while True:
    reqs = make_x(p2)
    if reqs['ORE'] <= TRL:
        break
    p2 -= 1

print(f'Part 2: {p2}')
