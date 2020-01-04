# BOJ 1912 - 연속합
import sys
r = sys.stdin.readline

N = int(r())
arr = list(map(int, r().split()))
ans = [0] * N
ans[0] = arr[0]
for i in range(1, N):
    ans[i] = max(arr[i], arr[i]+ans[i-1])
print(max(ans))

