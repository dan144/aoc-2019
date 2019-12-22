#!/usr/bin/env python3

from copy import copy

inp = []
with open('22', 'r') as f:
    for line in f:
        inp.append(line)

p1 = 0
p2 = 0

def deal_into_new(deck):
    deck = deck[::-1]
    return deck

def cut(deck, N):
    deck = deck[N:] + deck[:N]
    return deck

def deal_with_inc(deck, N):
    cards = copy(deck)
    deck = [0] * len(cards)
    i = 0
    for card in cards:
        deck[i] = card
        i = (i + N) % len(cards)
    return deck

def shuffle(deck):
    for line in inp:
        if line.startswith('deal into'):
            deck = deal_into_new(deck)
        elif line.startswith('cut'):
            deck = cut(deck, int(line.split()[-1]))
        elif line.startswith('deal with'):
            deck = deal_with_inc(deck, int(line.split()[-1]))
    return deck

CARDS = 10007
deck = list(range(CARDS))

deck = shuffle(deck)
if CARDS < 100:
    print(deck)

for i in range(CARDS):
    if deck[i] == 2019:
        p1 = i
        break
print(f'Part 1: {p1}')

print(f'Part 2: {p2}')
