#!/usr/bin/python3.6

inp = []
with open('4', 'r') as f:
    inp = f.readline()

p1 = 0
p2 = 0

l, h = inp.split('-')

for x in range(int(l), int(h)+1):
    s = str(x)
    p1_adj = False
    p2_adj = False
    adj_c = 0
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            break
        if s[i] == s[i+1]:
            p1_adj = True
            adj_c += 1
        else:
            if adj_c == 1:
                p2_adj = True
            else:
                adj_c = 0
    else:
        if p1_adj:
            p1 += 1
        if p2_adj is True or adj_c == 1:
            # this edge case bit me hard
            p2 += 1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
