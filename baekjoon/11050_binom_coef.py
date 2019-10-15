# BOJ 11051 - 이항계수 2
import sys

N, K = map(int, sys.stdin.readline().split())
arr = [[1 for _ in range(i)] for i in range(1, N+2)]

for i in range(2, N+1):
    for j in range(len(arr[i])):
        if 0 < j < (len(arr[i])-1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

print(arr[-1][K]%10007)


