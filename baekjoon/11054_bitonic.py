# BOJ 11054 - 가장 큰 바이토닉 부분 수열 - DP
import sys
r = sys.stdin.readline

N = int(r())
seq = list(map(int, r().split()))
dp1 = [1] * N
dp2 = [1] * N

for i in range(1, N):
    for j in range(i):
        if seq[i] > seq[j] and dp1[i] < dp1[j] + 1:
            dp1[i] = dp1[j] + 1

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if seq[i] > seq[j] and dp2[i] < dp2[j] + 1:
            dp2[i] = dp2[j] + 1


ans = 0
for i in range(N):
    if ans < dp1[i] + dp2[i] - 1:
        ans = dp1[i] + dp2[i] - 1
print(ans)