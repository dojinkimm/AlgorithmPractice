# BOJ 11047 - 동전 0
import sys


N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
coins.sort(reverse=True)

answer = 0
for c in coins:
    if K >= c:
        num = K // c
        answer += num
        K -= (num * c)

    if K == 0:
        break

print(answer)

