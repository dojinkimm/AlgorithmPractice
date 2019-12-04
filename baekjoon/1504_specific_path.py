# BOJ 1504 - 특정한 최단 경로
import sys
from heapq import *
r = sys.stdin.readline
INF = 1e9


def dijkstra(n, x, g):
    dist = [INF] * n
    dist[x] = 0
    q = []
    heappush(q, [0, x])

    while q:
        cost, pos = heappop(q)

        for p, c in g[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])

    return dist


N, E = map(int, r().split())
graph = [[] for _ in range(N)]
for _ in range(E):
    u, v, w = map(int, r().split())
    graph[u-1].append([v-1, w])
    graph[v-1].append([u-1, w])

one, two = map(int, r().split())

answer = []
for idx, i in enumerate([1, one, two]):
    answer.append(dijkstra(N, i-1, graph))

first = answer[0][one-1] + answer[1][two-1] + answer[2][N-1]
second = answer[0][two-1] + answer[1][N-1] + answer[2][one-1]
ans = min(first, second)
if ans >= INF or ans < 0:
    print(-1)
else:
    print(ans)


# 4 6
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 4 5
# 1 4 4
# 2 3