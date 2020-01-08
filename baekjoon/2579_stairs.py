# BOJ 2579 - 계단 오르기
import sys
r = sys.stdin.readline

N = int(r())
stairs = [int(r()) for _ in range(N)]
maxnum = [0] * N

maxnum[0] = stairs[0]
maxnum[1] = stairs[0] + stairs[1]
maxnum[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3, N):
    maxnum[i] = max(maxnum[i-2] + stairs[i], maxnum[i-3] + stairs[i-1] + stairs[i])
print(maxnum[-1])

# 1,3 or 0,2,3