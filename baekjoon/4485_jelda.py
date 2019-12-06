# BOJ 4485 - 녹색 옷 입은 애가 젤다지?
import sys
from heapq import heappush, heappop
r = sys.stdin.readline
INF = 1e9
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dijkstra(n, g):
    dist = [[INF]*n for _ in range(n)]
    dist[0][0] = g[0][0]
    q = []
    heappush(q, [0, 0, g[0][0]])

    while q:
        x, y, c = heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n):
                cost = g[nx][ny] + c
                if dist[nx][ny] > cost:
                    dist[nx][ny] = cost
                    heappush(q, [nx, ny, cost])

    return dist[n-1][n-1]


cnt = 0
while True:
    N = int(r())
    if N == 0:
        break
    cnt += 1
    graph = [list(map(int, r().split())) for _ in range(N)]

    print("Problem %d: %d" % (cnt, dijkstra(N, graph)))

# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 0