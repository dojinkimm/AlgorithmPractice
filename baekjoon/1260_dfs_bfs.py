# BOJ 1260 - DFS와 BFS
import sys
from collections import deque
r = sys.stdin.readline


def dfs(ans, v, g):
    for ele in g[v]:
        if ele not in ans:
            ans.append(ele)
            dfs(ans, ele, g)
    return ans


def bfs(ans, q, g):
    while q:
        x = q.popleft()
        ans.append(x)

        for ele in g[x]:
            if ele not in ans and ele not in q:
                q.append(ele)
    return ans


N, M, V = map(int, r().split())
graph = dict()
que = deque()
for i in range(1, N+1):
    graph[i] = []

for i in range(M):
    edge = list(map(int, r().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for j in graph.keys():
    graph[j] = sorted(graph[j])
    if j == V:
        que.extend(graph[j])

print(" ".join(map(str, dfs([V], V, graph))))
print(" ".join(map(str, bfs([V], que, graph))))
