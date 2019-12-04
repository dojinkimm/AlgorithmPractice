# BOJ 1916 - 최소비용 구하기
import sys
import heapq
r = sys.stdin.readline
INF = 1e9


def dijkstra(n, s, e, edg):
    q = []
    dist = [INF] * n
    dist[s-1] = 0
    heapq.heappush(q, [s-1, 0])

    while q:
        pos, cost = heapq.heappop(q)

        for p, c in edg[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heapq.heappush(q, [p, c])
    return dist[e-1]


N = int(r())
M = int(r())
edges = [[] for _ in range(N)]
for i in range(M):
    u, v, w = list(map(int, r().split()))
    edges[u-1].append([v-1, w])

st, end = map(int, r().split())

print(dijkstra(N, st, end, edges))
# distance = [[i, INF] for i in range(N)]
# distance[st-1][1] = 0
# heap = [st-1]
#
# while len(heap) < N:
#     for e in edges[heap[-1]]:
#         distance[e[0]][1] = min(distance[e[0]][1], distance[heap[-1]][1] + e[1])
#
#     for d in sorted(distance, key=lambda x: x[1]):
#         if d[0] not in heap:
#             heap.append(d[0])
#             break
#
#     if heap[-1] == end-1:
#         break
#
# print(distance[end-1][1])
