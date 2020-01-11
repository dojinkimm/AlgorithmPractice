# BOJ 2960 - 에라토스테네스
import sys

N, K = map(int, sys.stdin.readline().split())

isPrime = [False, False] + [True] * (N-1)
cnt = 0
for i in range(2, N+1):
    for j in range(i, N+1, i):
        if isPrime[j]:
            isPrime[j] = False
            cnt += 1
            if cnt == K:
                print(j)
                sys.exit(0)