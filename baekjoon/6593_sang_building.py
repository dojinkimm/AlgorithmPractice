# BOJ 6593 - 상범빌딩
import sys
from heapq import heappush, heappop
r = sys.stdin.readline
INF = 1e9
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [0, 0, -1, 1, 0, 0]


def dijkstra(Z, X, Y, s, e, g):
    dist = [[[INF]*Y for _ in range(X)] for _ in range(Z)]
    dist[s[0]][s[1]][s[2]] = 0
    q = []
    heappush(q, [s[0], s[1], s[2], 0])

    while q:
        z, x, y, c = heappop(q)

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if (0 <= nx < X) and (0 <= ny < Y) and (0 <= nz < Z) and g[nz][nx][ny] != "#":
                cost = c + 1
                if dist[nz][nx][ny] > cost:
                    dist[nz][nx][ny] = cost
                    heappush(q, [nz, nx, ny, cost])

    return dist[e[0]][e[1]][e[2]]


while True:
    Z, X, Y = map(int, r().split())
    if Z == 0 and X == 0 and Y == 0:
        break

    graph = []
    for i in range(Z):
        graph.append([])
        for j in range(X+1):
            row = list(r().strip())
            if row:
                graph[i].append(row)
                if 'S' in row:
                    S = [i, j, row.index('S')]
                elif 'E' in row:
                    E = [i, j, row.index('E')]

    dij = dijkstra(Z, X, Y, S, E, graph)
    if dij != INF:
        print("Escaped in %d minute(s)." % dij)
    else:
        print("Trapped!")




# 3 4 5
# S....
# .###.
# .##..
# ###.#
#
# #####
# #####
# ##.##
# ##...
#
# #####
# #####
# #.###
# ####E
#
# 1 3 3
# S##
# #E#
# ###
#
# 0 0 0