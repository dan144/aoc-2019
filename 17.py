#!/usr/bin/env python3

from intcode import Intcode

inp = []
with open('17', 'r') as f:
    inp = list(map(int, f.readline().split(',')))

p1 = 0
p2 = 0

def disp(values):
    board = ''.join(map(chr, values)).split('\n')
    for r in range(len(board)):
        board[r] = list(board[r])
    for line in board:
        print(''.join(line))
    return board

comp = Intcode(inp)
values = comp.run_collect_output()
board = disp(values)

for r in range(len(board)):
    for c in range(len(board[r])):
        if board[r][c] == '#':
            sur = 0
            for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
                try:
                    if board[r+dx][c+dy] == '#':
                        sur += 1
                except:
                    pass
            if sur == 4: # intersection
                board[r][c] = 'O'
                p1 += r*c

print(f'Part 1: {p1}')

COMMA = 44
NL = 10
A = 65
B = 66
C = 67
L = 76
R = 82
n = 110
y = 121
ONE = ord('1')
TWO = ord('2')
SIX = ord('6')
EIGHT = ord('8')
ZERO = ord('0')

#A       A       C          B         C          B         C          B         C          A
#R6L12R6 R6L12R6 L12R6L8L12 R12L10L10 L12R6L8L12 R12L10L10 L12R6L8L12 R12L10L10 L12R6L8L12 R6L12R6

ROUTINES = [A, COMMA, A, COMMA, C, COMMA, B, COMMA, C, COMMA, B, COMMA, C, COMMA, B, COMMA, C, COMMA, A]
RA = [R, COMMA, SIX, COMMA, L, COMMA, ONE, TWO, COMMA, R, COMMA, SIX]
RB = [R, COMMA, ONE, TWO, COMMA, L, COMMA, ONE, ZERO, COMMA, L, COMMA, ONE, ZERO]
RC = [L, COMMA, ONE, TWO, COMMA, R, COMMA, SIX, COMMA, L, COMMA, EIGHT, COMMA, L, COMMA, ONE, TWO]

cmds = ROUTINES + [NL] + RA + [NL] + RB + [NL] + RC + [NL, n, NL]
comp = Intcode(inp, inputs=cmds)
comp.reg[0] = 2
values = comp.run_collect_output()
p2 = values[-1]

print(f'Part 2: {p2}')
