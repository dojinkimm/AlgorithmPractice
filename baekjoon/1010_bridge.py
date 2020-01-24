# BOJ 1010 - 다리놓기 - DP
import sys
r = sys.stdin.readline

T = int(r())
for _ in range(T):
    N, M = map(int, r().split())
    if N == M:
        print(1)
    elif N == 1:
        print(M)
    else:
        dp = [[0] * M for _ in range(N)]
        # 1 1 / 2 2 / 3 3같은 경우는 항상 1이다
        for i in range(N):
            dp[i][i] = 1
        for j in range(1, M):
            dp[0][j] = j+1

        for i in range(1, N):
            for j in range(i+1, M):
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        print(dp[-1][-1])

