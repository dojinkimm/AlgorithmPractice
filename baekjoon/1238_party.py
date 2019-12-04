# BOJ 1238 - 파티
import sys
from heapq import heappush, heappop
r = sys.stdin.readline
INF = 1e9


def dijkstra(n, x, ro):
    dist = [INF] * n
    dist[x] = 0
    q = []
    heappush(q, [0, x])

    while q:
        cost, pos = heappop(q)

        for p, c in ro[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])

    return dist


N, M, X = map(int, r().split())
road = [[] for _ in range(N)]
for _ in range(M):
    u, v, t = map(int, r().split())
    road[u-1].append([v-1, t])

answer = [0] * N
for i in range(N):
    ret = dijkstra(N, i, road)

    if i == X-1:
        for idx, r in enumerate(ret):
            answer[idx] += r
    else:
        answer[i] += ret[X-1]
print(max(answer))
# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3

# import sys
# from heapq import *
# input = sys.stdin.readline
# n, m, x = map(int, input().split())
# home = [[] for _ in range(n+1)]
# home2 = [[] for _ in range(n+1)]
# for _ in range(m):
#     s, e, t = map(int, input().split())
#     home[s].append((e, t))
#     home2[e].append((s, t))
#
# def dijkstra(g, start):
#     d=[9876543210]*(n+1)
#     d[start] = 0
#     heap = [(0,start)]
#     while heap:
#         total, node = heappop(heap)
#         if d[node]<total:continue
#         for nxt, cost in g[node]:
#             if d[nxt]>d[node]+cost:
#                 d[nxt] = d[node]+cost
#                 heappush(heap, (d[nxt],nxt))
#     return d[1:]
#
# print(max([a+b for a, b in zip(dijkstra(home, x), dijkstra(home2,x))]))