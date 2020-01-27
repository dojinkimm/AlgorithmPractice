# 네트워크 - DFS/BFS
def solution(n, computers):
    cnt = 0
    visited = [False] * n

    def dfs(idx):
        for j in range(n):
            if j != idx and computers[idx][j] is 1 and not visited[j]:
                visited[j] = True
                dfs(j)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            cnt += 1

    return cnt