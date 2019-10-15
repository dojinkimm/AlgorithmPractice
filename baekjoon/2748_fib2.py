# BOJ 2748 - 피보나치 2
import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(N+1)]
arr[1] = 1

for i in range(2, N+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[-1])