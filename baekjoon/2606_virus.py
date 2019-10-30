# BOJ 2606 - 바이러스
import sys
r = sys.stdin.readline


def dfs(v, egs, ans):
    for i in egs[v]:
        if i not in ans:
            ans.append(i)
            dfs(i, egs, ans)
    return ans


N = int(r())
edges = [[] for _ in range(N+1)]
for _ in range(1, int(r())+1):
    e1, e2 = map(int, r().split())
    edges[e1].append(e2)
    edges[e2].append(e1)

print(len(dfs(1, edges, [1]))-1)

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7