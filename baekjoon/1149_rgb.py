# BOJ 1149 - RGB 거리 - DP
import sys
r = sys.stdin.readline
INF = 987654321

N = int(r())
home = [list(map(int, r().split())) for _ in range(N)]
cost = [[INF]*3 for _ in range(N)]
cost[0] = home[0][:]

for i in range(1, N):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + home[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + home[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + home[i][2]

print(min(cost[N-1]))