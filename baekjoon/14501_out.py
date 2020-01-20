# BOJ 14501 - 퇴사 - DP
import sys
r = sys.stdin.readline

N = int(r())
counsel = [list(map(int, r().split())) for _ in range(N)]
dp = [0] * (N+1)
counsel.insert(0, [0,0])
for i in range(1, N+1):
    d, p = counsel[i]
    if i + d <= N+1:
        dp[i + d - 1] = max(dp[i + d - 1], p)
        dp[i + d - 1] = max(dp[i + d - 1], max(dp[:i]) + p)
print(max(dp))
