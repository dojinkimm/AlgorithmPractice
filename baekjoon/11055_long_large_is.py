# BOJ 11055 - 가장 큰 증가 부분 수열 - DP
import sys
r = sys.stdin.readline

N = int(r())
seq = list(map(int, r().split()))
ans = [0] * N


for i in range(N):
    ans[i] = seq[i]
    for j in range(i):
        if seq[i] > seq[j] and ans[i] < ans[j] + seq[i]:
            ans[i] = ans[j] + seq[i]

print(max(ans))