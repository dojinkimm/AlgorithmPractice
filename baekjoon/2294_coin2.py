# BOJ 2294 - 동전 2
import sys
r = sys.stdin.readline

N, K = map(int, r().split())
coins = sorted([int(r()) for _ in range(N)])

arr = [10001] * (K+1)
arr[0] = 0

for i in range(N):
    for j in range(coins[i], K+1):
        arr[j] = min(arr[j], arr[j-coins[i]] + 1)

arr[-1] = arr[-1] if arr[-1] != 10001 else -1
print(arr[-1])
