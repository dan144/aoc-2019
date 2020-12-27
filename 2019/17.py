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
            for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
                try:
                    if board[r+dx][c+dy] != '#':
                        break
                except:
                    break
            else:
                board[r][c] = 'O'
                p1 += r*c

print(f'Part 1: {p1}')

#R6L12R6 R6L12R6 L12R6L8L12 R12L10L10 L12R6L8L12 R12L10L10 L12R6L8L12 R12L10L10 L12R6L8L12 R6L12R6
#A       A       C          B         C          B         C          B         C          A

ROUTINES = 'A,A,C,B,C,B,C,B,C,A'
RA = 'R,6,L,12,R,6'
RB = 'R,12,L,10,L,10'
RC = 'L,12,R,6,L,8,L,12'
NL = '\n'

cmd_str = ROUTINES + NL + RA + NL + RB + NL + RC + NL + 'n' + NL
cmds = list(map(ord, cmd_str))

comp = Intcode(inp, inputs=cmds)
comp.reg[0] = 2
p2 = comp.run_collect_output()[-1]

print(f'Part 2: {p2}')
