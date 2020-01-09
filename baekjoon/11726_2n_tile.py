# BOJ 11726 - 2xn 타일링 - DP
import sys
MOD = 10007

N = int(sys.stdin.readline())
arr = [0] * 1001

arr[1] = 1
arr[2] = 2
for i in range(3, N+1):
    arr[i] = (arr[i-1] + arr[i-2]) % MOD

print(arr[N] % MOD)