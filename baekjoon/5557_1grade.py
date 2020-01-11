# BOJ 5557 - 1학년 - DP
import sys
r = sys.stdin.readline

N = int(r())
eq = list(map(int,r().split()))
dp = [[0]*(21) for _ in range(N-1)]
dp[0][eq[0]] = 1
for i in range(1, N-1):
    for j in range(21):
        # 이전 단계에 도달했으면
        if dp[i-1][j] != 0:
            if j - eq[i] >= 0:
                dp[i][j-eq[i]] += dp[i-1][j]
            if j + eq[i] <= 20:
                dp[i][j+eq[i]] += dp[i-1][j]

print(dp[N-2][eq[N-1]])
