# BOJ 12865 - 평범한 배낭
import sys

r = sys.stdin.readline
N, W = map(int, r().split())
bag = [tuple(map(int, r().split())) for _ in range(N)]

knap = [0 for _ in range(W+1)]

for i in range(N):
    for j in range(W, 1, -1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])

print(knap[-1])


# 4 7
# 6 13
# 4 8
# 3 6
# 5 12


# 4 5
# 2 3
# 3 4
# 4 5
# 5 6