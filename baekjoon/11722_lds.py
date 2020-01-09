# BOJ 11722 - 가장 큰 감소하는 부분 수열 - DP
import sys
r = sys.stdin.readline

N = int(r())
seq = list(map(int, r().split()))
ans = [1] * N

for i in range(1, N):
    for j in range(i):
        if seq[i] < seq[j] and ans[i] < ans[j]+1:
            ans[i] = ans[j] + 1
print(max(ans))