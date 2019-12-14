#!/usr/bin/env python3

import math

from copy import copy

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

def all_needs():
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


#print(convs)
reqs = convs['FUEL'][1]
#print(reqs)
i = 0
while list(reqs.keys()) != ['ORE']:
    k = list(reqs.keys())[i]
    if k == 'ORE':
        i = (i + 1) % len(list(reqs.keys()))
        continue
    r = reqs.pop(k)
    q, n = convs[k]
    #print(k, r, q, n)
    #print(reqs)
    if k in all_needs():
        reqs[k] = r
        continue
    #s = set(n.keys()) & set(reqs.keys())
    #if s and s != {'ORE'}:
    #    reqs[k] = r
    #    continue
    for need, n_q in n.items():
        #print(f'N: {all_needs()}')
        if False: #need in all_needs():
            quan = r / q * n_q
        else:
            quan = math.ceil(r / q) * n_q
        #print(need, quan)
        if need in reqs:
            reqs[need] += quan
        else:
            reqs[need] = quan
    #print(f'R: {reqs}')


p1 = reqs['ORE']
print(f'Part 1: {p1}')



print(f'Part 2: {p2}')
