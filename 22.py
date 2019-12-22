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

def deal_with_inc(inc, off, N, cards):
    inc *= pow(N, cards-2, cards)
    return inc, off

def shuffle(cards):
    inc = 1
    off = 0
    for line in inp:
        if line.startswith('deal into'):
            inc, off = deal_into_new(inc, off)
        elif line.startswith('cut'):
            inc, off = cut(inc, off, int(line.split()[-1]))
        elif line.startswith('deal with'):
            inc, off = deal_with_inc(inc, off, int(line.split()[-1]), cards)
    return inc, off

def f_vals(inc, off, iters, cards):
    off = off * (1 - pow(inc, iters, cards)) * pow(1 - inc, cards-2, cards)
    inc = pow(inc, iters, cards)
    return inc, off

def nth_card(inc, off, n, cards):
    return (off + n * inc) % cards

CARDS = 10007
SHUFFLES = 1
inc, off = shuffle(CARDS)
inc, off = f_vals(inc, off, SHUFFLES, CARDS)

for i in range(CARDS):
    if nth_card(inc, off, i, CARDS) == 2019:
        p1 = i
        break
print(f'Part 1: {p1}')

CARDS = 119315717514047
SHUFFLES = 101741582076661
inc, off = shuffle(CARDS)
inc, off = f_vals(inc, off, SHUFFLES, CARDS)

p2 = nth_card(inc, off, 2020, CARDS)
print(f'Part 2: {p2}')
