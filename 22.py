#!/usr/bin/env python3

from copy import copy

inp = []
with open('22', 'r') as f:
    for line in f:
        inp.append(line)

p1 = 0
p2 = 0

def deal_into_new(inc, off):
    inc *= -1
    off += inc
    return inc, off

def cut(inc, off, N):
    off += inc * N
    return inc, off

def deal_with_inc(inc, off, N):
    inc *= pow(N, CARDS-2, CARDS)
    return inc, off

def shuffle():
    inc = 1
    off = 0
    for line in inp:
        if line.startswith('deal into'):
            inc, off = deal_into_new(inc, off)
        elif line.startswith('cut'):
            inc, off = cut(inc, off, int(line.split()[-1]))
        elif line.startswith('deal with'):
            inc, off = deal_with_inc(inc, off, int(line.split()[-1]))
    return inc, off

CARDS = 10007
inc, off = shuffle()
off = off * (1 - pow(inc, 1, CARDS)) * pow(1 - inc, CARDS-2, CARDS)
inc = pow(inc, 1, CARDS)

for i in range(CARDS):
    if (off + i * inc) % CARDS == 2019:
        p1 = i
        break

print(f'Part 1: {p1}')

CARDS = 119315717514047
SHUFFLES = 101741582076661

inc, off = shuffle()
off = off * (1 - pow(inc, SHUFFLES, CARDS)) * pow(1 - inc, CARDS-2, CARDS)
inc = pow(inc, SHUFFLES, CARDS)

p2 = (off + 2020 * inc) % CARDS
print(f'Part 2: {p2}')
