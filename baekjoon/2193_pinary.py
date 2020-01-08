# BOJ 2193 - 이친수 - DP
import sys

N = int(sys.stdin.readline())
arr = [0] * (N+1)
arr[1] = 1
for i in range(2, N+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[-1])
