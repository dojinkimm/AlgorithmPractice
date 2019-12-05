# BOJ 1261 - 알고스팟
import sys
from heapq import *
r = sys.stdin.readline
INF = 1e9
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dijkstra(n, m, al):
    dist = [[INF]*n for _ in range(m)]
    dist[0][0] = 0
    q = []
    heappush(q, [0, 0, 0])

    while q:
        x, y, w = heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < m) and (0 <= ny < n):
                wall = w + al[nx][ny]
                if dist[nx][ny] > wall:
                    dist[nx][ny] = wall
                    heappush(q, [nx, ny, wall])
    return dist[m-1][n-1]


N, M = map(int, r().split())
algo = [list(map(int, list(r().strip()))) for _ in range(M)]

print(dijkstra(N, M, algo))
