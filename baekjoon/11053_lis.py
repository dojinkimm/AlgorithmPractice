# BOJ 11053 - 가장 긴 증가하는 부분 수열 - DP
import sys
r = sys.stdin.readline

N = int(r())
arr = list(map(int, r().split()))
cnt = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j] and cnt[i] < cnt[j] + 1:
            cnt[i] = cnt[j] + 1

print(max(cnt))
