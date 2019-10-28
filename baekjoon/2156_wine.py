# BOJ 2156 - 포도주 시식
import sys
r = sys.stdin.readline

N = int(r())
cup = [int(r()) for _ in range(N)]
maxi = [0] * (N+1)
cup.insert(0, 0)
maxi[1] = cup[1]
if N > 1:
    maxi[2] = cup[1] + cup[2]

for i in range(3, N+1):
    maxi[i] = max(maxi[i-1], max(maxi[i-2]+cup[i], maxi[i-3]+cup[i-1]+cup[i]))

print(maxi[-1])
