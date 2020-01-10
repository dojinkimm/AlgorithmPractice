# BOJ 2529 - 부등호 - Greedy
import sys
from itertools import permutations

r = sys.stdin.readline

N = int(r())
inequality = list(map(str, r().strip().split()))
inc = [i for i in range(N+1)]
dec = [i for i in range(9, 9-N-1, -1)]
inequality.append(" ")

result = 0
flag = False
for perm in permutations(dec):
    for i in range(N):
        if inequality[i] == '>' and perm[i] > perm[i+1]:
            result += 1
        elif inequality[i] == '<' and perm[i] < perm[i+1]:
            result += 1
        else:
            break

        if result == N:
            flag = True
            break
    if flag:
        print("".join(map(str,perm)))
        break
    result = 0

result = 0
flag = False
for perm in permutations(inc):
    for i in range(N):
        if inequality[i] == '>' and perm[i] > perm[i+1]:
            result += 1
        elif inequality[i] == '<' and perm[i] < perm[i+1]:
            result += 1
        else:
            break

        if result == N:
            flag = True
            break
    if flag:
        print("".join(map(str, perm)))
        break
    result = 0

